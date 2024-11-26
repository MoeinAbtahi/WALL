from flask import Flask, render_template, request, redirect, url_for
import os
import csv
import base64
import openai
import difflib
import requests
from sklearn.metrics import precision_score, recall_score, f1_score
from nltk.translate.bleu_score import sentence_bleu
from rouge_score import rouge_scorer

app = Flask(__name__)

# Ensure uploads directory exists
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
csv_lines = []
current_line_index = 0

# Global variables for managing user preferences and state
csv_lines = []
current_line_index = 0
current_font_size = 14
original_code_color = "#000000"
background_color = "#FFFFFF"
selected_font = "Courier"
output_directory = ""

### Function Definitions ###

def get_all_issues(sonar_url, api_token, project_key):
    page_size = 500  # Number of issues per page
    page_number = 1  # Starting page number
    all_issues = []  # List to store all retrieved issues

    while True:
        # Construct the API endpoint and query parameters
        url = f"{sonar_url}/api/issues/search"
        params = {
            'componentKeys': project_key,  # Filter issues by project key
            'resolved': 'false',           # Only fetch unresolved issues
            'ps': page_size,               # Number of issues per page
            'p': page_number               # Current page number
        }

        # Encode API token in base64 for basic authentication
        token = base64.b64encode(f"{api_token}:".encode('utf-8')).decode('utf-8')
        headers = {
            'Authorization': f'Basic {token}'  # Add authentication header
        }

        # Make the API request to fetch issues
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()  # Raise an error for bad responses
        data = response.json()  # Parse the JSON response

        # Extract issues from the response
        issues = data.get('issues', [])
        if not issues:
            break  # Exit the loop if no issues are returned

        # Add the current batch of issues to the list
        all_issues.extend(issues)

        # Increment the page number to fetch the next batch
        page_number += 1

        # Stop if the current page has fewer issues than the page size
        if len(issues) < page_size:
            break

    return all_issues  # Return the complete list of issues


def modify_file_path(original_path, to_remove, to_add):
    # Step 1: Remove the specified prefix if it exists at the start of the path
    if to_remove and original_path.startswith(to_remove):
        original_path = original_path[len(to_remove):]

    # Step 2: Replace ':' and '\' with '/' to standardize the path
    modified_path = original_path.replace(':', '').replace('\\', '/')
    
    # Step 3: Normalize double slashes to single slashes
    modified_path = modified_path.replace('//', '/')
    
    # Step 4: Prepend the `to_add` path and normalize the result
    # Step 5: Convert any remaining backslashes to forward slashes for uniformity
    return os.path.normpath(to_add + modified_path).replace('\\', '/')

def save_csv_file(issues, file_path, to_remove, to_add):
    # Step 1: Prepare issue data with modified paths and selected fields
    issue_data = [{
        # Modify the file path and remove/add segments as specified
        'file_Location': modify_file_path(issue['component'], to_remove, to_add),
        # Extract the base file name, optionally prefixed with "Revised."
        # Uncomment the next line if a "Revised." prefix is required:
        # 'file_name': "Revised." + os.path.basename(issue['component']),
        'file_name': os.path.basename(issue['component']),
        # Retrieve the line number, or mark as 'N/A' if not present
        'line': issue.get('line', 'N/A'),
        # Include the issue's message and type
        'message': issue['message'],
        'type': issue['type']
    } for issue in issues]

    # Step 2: Sort issue data by file location
    issue_data.sort(key=lambda x: x['file_Location'])

    # Step 3: Write data to a CSV file
    with open(file_path, mode='w', newline='', encoding='utf-8') as file:
        # Define CSV columns and write header row
        writer = csv.DictWriter(file, fieldnames=['file_Location', 'file_name', 'line', 'message', 'type'])
        writer.writeheader()
        # Write each issue's data row
        writer.writerows(issue_data)

def read_file_contents(file_path):
    # Step 1: Open the file in read mode
    with open(file_path, 'r') as file:
        # Step 2: Read all lines into a list
        lines = file.readlines()
        
        # Step 3 & 4: Enumerate lines and join them with line numbers prefixed
        return ''.join(f"{i + 1}: {line}" for i, line in enumerate(lines))

def generate_prompt(file_location, bug_lines, bug_messages, bug_types):
    # Step 1: Read the original code from the file
    original_code = read_file_contents(file_location)
    
    # Step 2: Create the initial prompt with general instructions
    prompt = (
        f"""Please fix the issues and send back the corrected code without any additional details or descriptions.\n"""
        f"""Ensure that the edited parts are included in the complete code, and all the original lines of code are preserved.\n"""
        f"""The programming language used in the provided code is important for fixing the issues. It may include JavaScript (JSX), YAML, or JavaScript for testing purposes.\n"""
        f"""Here is the original code:\n\n{original_code}\n"""
    )

    # Step 3: Add information about each detected issue
    for bug_line, bug_message, bug_type in zip(bug_lines, bug_messages, bug_types):
        prompt += (
            f"""\nThe detected "{bug_type}" issue by SonarQube is on line: {bug_line}. """
            f"""Description of how to solve this code issue: "{bug_message}"."""
        )

    # Step 4: Include additional instructions for similar issues
    prompt += (
        f"""\nIf the same code issue is present on other lines, please fix those as well.\n"""
        f"""Resolve this bug based on the SonarQube database, and send the corrected code back to me as specified. """
        f"""Ensure the code format matches the original code file.\n"""
        f"""Please only send the code file itself, without any additional details or descriptions (such as the file type or other information).\n"""
    )

    # Step 5: Add few-shot learning examples for guidance
    prompt += f"""\n\n### Few-Shot Learning Examples ###\n"""

    # Example 1: Bug fix for JSX file
    prompt += (
        f"""Example 1 (Bug): Detected issue: 'Visible, non-interactive elements with click handlers must have at least one keyboard listener' in a JSX file.\n"""
        f"""<div onClick={{handleClick}}>...</div>\n"""
        f"""Corrected Code:\n"""
        f"""<div onClick={{handleClick}} onKeyDown={{handleKeyDown}} tabIndex="0">...</div>\n"""
    )

    # Example 2: Vulnerability fix for YAML file
    prompt += (
        f"""\nExample 2 (Vulnerability): Detected issue: 'Set automountServiceAccountToken to false for this specification of kind Deployment' in a YAML file.\n"""
        f"""automountServiceAccountToken: true\n"""
        f"""Corrected Code:\n"""
        f"""automountServiceAccountToken: false\n"""
    )

    # Example 3: Code smell fix for JS test file
    prompt += (
        f"""\nExample 3 (Code smell): Detected issue: 'Remove this commented out code' in a JavaScript test file.\n"""
        f"""// TODO: Add end-to-end tests\n"""
        f"""Corrected Code:\n"""
        f"""<code is removed>\n"""
    )

    # Step 6: Conclude with a reminder of the expected format
    prompt += (
        f"""\n### End of Examples ###\n"""
        f"""Please follow the examples provided and send back only the corrected code sections. """
        f"""Ensure the format matches the original code file without extra descriptions or details.\n"""
    )

    return prompt

def highlight_differences(diff):
    # Initialize an empty list to store the highlighted HTML lines
    highlighted_html = []
    
    # Step 2: Iterate through each line in the diff
    for line in diff:
        if line.startswith('-'):
            # Highlight removed lines in yellow (background color)
            highlighted_html.append(f'<span style="background-color: yellow;">{line}</span>')
        elif line.startswith('+'):
            # Highlight added lines in light green (background color)
            highlighted_html.append(f'<span style="background-color: lightgreen;">{line}</span>')
        else:
            # No change, no highlight. Just add the line as is
            highlighted_html.append(f'<span>{line}</span>')
    
    # Step 3: Join the list of highlighted HTML lines with line breaks (<br>)
    return '<br>'.join(highlighted_html)

def calculate_all_metrics(original_lines, revised_lines):
    # Step 1: Tokenize the original and revised lines by stripping extra spaces
    original_tokens = [line.strip() for line in original_lines]
    revised_tokens = [line.strip() for line in revised_lines]

    # Step 2: Convert tokenized lines into sets for comparison
    original_set = set(original_tokens)
    revised_set = set(revised_tokens)

    # Step 3: Calculate true positives, false positives, and false negatives
    true_positives = original_set & revised_set
    false_positives = revised_set - original_set
    false_negatives = original_set - revised_set

    # Step 4: Calculate precision, recall, and F1 score
    precision = len(true_positives) / (len(true_positives) + len(false_positives)) if (len(true_positives) + len(false_positives)) > 0 else 0
    recall = len(true_positives) / (len(true_positives) + len(false_negatives)) if (len(true_positives) + len(false_negatives)) > 0 else 0
    f1 = (2 * precision * recall) / (precision + recall) if (precision + recall) > 0 else 0

    # Step 5: Calculate exact match (ratio of true positives to original tokens)
    exact_match = len(true_positives) / len(original_tokens) if original_tokens else 0

    # Step 6: Calculate BLEU score
    bleu = sentence_bleu([original_tokens], revised_tokens)

    # Step 7: Calculate ROUGE scores
    rouge_scorer_instance = rouge_scorer.RougeScorer(['rouge1', 'rougeL'], use_stemmer=True)
    rouge_scores = rouge_scorer_instance.score("\n".join(original_tokens), "\n".join(revised_tokens))

    # Step 8: Convert all metrics to percentages and return them as a dictionary
    return {
        'precision': precision * 100,  # Precision as percentage
        'recall': recall * 100,        # Recall as percentage
        'f1_score': f1 * 100,          # F1 score as percentage
        'exact_match': exact_match * 100,  # Exact match as percentage
        'bleu_score': bleu * 100,      # BLEU score as percentage
        'rouge1_fmeasure': rouge_scores['rouge1'].fmeasure * 100,  # ROUGE-1 F-measure as percentage
        'rougeL_fmeasure': rouge_scores['rougeL'].fmeasure * 100   # ROUGE-L F-measure as percentage
    }

### App Routes###

@app.route('/', methods=['GET'])
def index():
    # This function is mapped to the root URL ('/') of your application.
    # When a GET request is made to the root URL, the server will render the 'index.html' template.
    return render_template('index.html')

@app.route('/sonarqube', methods=['GET', 'POST'])
def sonarqube():
    # Define placeholder values and instructions for the form
    preset_sonar_urls = ["<Replace with your SonarQube URL>"]
    preset_api_tokens = ["<Replace with your SonarQube API Token>"]
    preset_project_keys = ["<Replace with your SonarQube Project Key>"]
    preset_project_locations = ["<Replace with the project location on your system>"]
    preset_save_paths = ["<Replace with the path where you want to save the CSV file>"]

    if request.method == 'POST':
        # Capture form data sent via POST request
        sonar_url = request.form.get('sonar_url_manual') or request.form.get('sonar_url')
        api_token = request.form.get('api_token_manual') or request.form.get('api_token')
        project_key = request.form.get('project_key_manual') or request.form.get('project_key')
        original_project_location = request.form.get('original_project_location_manual') or request.form.get('original_project_location')
        save_path = request.form.get('save_path_manual') or request.form.get('save_path')

        # Ensure required fields are provided
        if not original_project_location or not save_path:
            return "Please fill in all required fields.", 400

        # Fetch issues from SonarQube
        all_issues = get_all_issues(sonar_url, api_token, project_key)

        # Save the fetched issues to a CSV file
        if save_path:
            save_csv_file(all_issues, save_path, project_key, original_project_location + "/")

    # Render the HTML form for both GET and POST requests
    return render_template('sonarqube.html',
                           preset_sonar_urls=preset_sonar_urls,
                           preset_api_tokens=preset_api_tokens,
                           preset_project_keys=preset_project_keys,
                           preset_project_locations=preset_project_locations,
                           preset_save_paths=preset_save_paths)

@app.route('/Code_Issue_Reviser', methods=['GET', 'POST'])
def Code_Issue_Reviser():
    # Global variables to store CSV lines and the current line index
    global csv_lines, current_line_index
    api_response = None  # Initialize api_response as None

    # Step 1: Handle CSV file upload if a file is provided in the request
    if 'csv_file' in request.files:
        csv_file = request.files['csv_file']
        if csv_file:
            # Save the uploaded CSV file to a specified location
            csv_file_path = os.path.join(UPLOAD_FOLDER, csv_file.filename)
            csv_file.save(csv_file_path)

            # Process the CSV file: Read and convert it into a list of lines
            with open(csv_file_path, 'r') as file:
                csv_reader = csv.DictReader(file)
                csv_lines = list(csv_reader)
                current_line_index = 0  # Start at the first line

            # Redirect to avoid form resubmission on page refresh
            return redirect(url_for('Code_Issue_Reviser'))

    # Step 2: Handle form submission and perform actions based on the button clicked
    if request.method == 'POST':
        # Check for the "save_prompt" button in the form to redirect for saving
        if 'save_prompt' in request.form:
            return redirect(url_for('select_save_location'))

        # Check for the "send_to_api" button to call the API with the edited prompt
        elif 'send_to_api' in request.form:
            edited_prompt = request.form.get('edited_prompt', '')  # Get the edited prompt from form
            file_name = request.form.get('file_name', '')  # Get the file name from form
            save_directory = request.form.get('save_directory', '')  # Get the save directory from form
            file_path = os.path.join(save_directory, file_name) if save_directory and file_name else None  # Create full file path if provided
            
            # Capture the selected API model from the form (default is 'gpt-4o-mini')
            selected_model = request.form.get('api_model', 'gpt-4o-mini')

            try:
                # Step 3: Make the API call to OpenAI with the selected model and prompt
                response = openai.ChatCompletion.create(
                    model=selected_model,  # Use the selected model
                    messages=[
                        {"role": "system", "content": "You are a code developer assistant."},
                        {"role": "user", "content": edited_prompt}
                    ],
                    max_tokens=1600
                )
                # Extract the response from the API
                api_response = response.choices[0].message['content'].strip()

                # Step 4: Optionally save the API response to a file if a path is provided
                if file_path:
                    with open(file_path, 'w') as file:
                        file.write(api_response)

            except Exception as e:
                print(f"API request failed: {e}")  # Print error if API request fails
                api_response = f"API request failed: {e}"

        # Step 5: Handle changes to UI preferences such as font size, font, background color, and code color
        elif 'font_size' in request.form:
            global current_font_size
            current_font_size = int(request.form.get('font_size', 10))  # Update font size
        elif 'font' in request.form:
            global selected_font
            selected_font = request.form.get('font', 'Courier')  # Update font style
        elif 'bg_color' in request.form:
            global background_color
            background_color = request.form.get('bg_color', '#FFFFFF')  # Update background color
        elif 'code_color' in request.form:
            global original_code_color
            original_code_color = request.form.get('code_color', '#000000')  # Update code color
        elif 'next_line' in request.form:
            current_line_index += 1  # Move to the next line in the CSV
        elif 'file_selection' in request.form:
            selected_file_name = request.form.get('file_selection', '')  # Get the selected file name
            current_line_index = next(
                (i for i, line in enumerate(csv_lines) if line.get('file_name') == selected_file_name), 0)  # Find the line index for the selected file
            return redirect(url_for('Code_Issue_Reviser'))  # Redirect to update the page with the selected file

    # Step 6: If CSV lines exist, process them and generate the prompt for the API
    if csv_lines:
        # Get the list of unique file names in the CSV for the file selection dropdown
        files = sorted(set(line.get('file_name') for line in csv_lines))
        line = csv_lines[current_line_index]  # Get the current line based on the index
        file_location = line.get('file_Location')
        file_name = line.get('file_name')

        if file_location and os.path.exists(file_location):  # If the file location exists, process the bugs
            bug_lines = [line.get('line')]
            bug_messages = [line.get('message')]
            bug_type = [line.get('type')]

            # Step 7: Handle multiple lines with the same file and group them
            next_line_index = current_line_index + 1
            while next_line_index < len(csv_lines) and csv_lines[next_line_index].get('file_name') == file_name:
                bug_lines.append(csv_lines[next_line_index].get('line'))
                bug_messages.append(csv_lines[next_line_index].get('message'))
                bug_type.append(csv_lines[next_line_index].get('type'))
                next_line_index += 1

            # Step 8: Generate a prompt based on the selected issues and code file
            prompt = generate_prompt(file_location, bug_lines, bug_messages, bug_type)
            return render_template('Code_Issue_Reviser.html', prompt=prompt, font_size=current_font_size,
                                   font=selected_font, bg_color=background_color,
                                   code_color=original_code_color, file_name=file_name, files=files, api_response=api_response)

    # Step 9: Get the list of unique files from the uploaded CSV lines if no issues are processed yet
    files = sorted(set(line.get('file_name') for line in csv_lines))
    file_name = csv_lines[current_line_index].get('file_name') if csv_lines else None
    prompt = generate_prompt(file_name) if file_name else ""  # Generate an empty prompt if no file is selected
    
    return render_template('Code_Issue_Reviser.html', prompt=prompt, files=files, api_response=api_response)

@app.route('/Code_Comparer', methods=['GET', 'POST'])
def compare_files():
    # Global variables to store CSV lines and other data related to the code comparison
    global csv_lines
    original_file_path = ""  # Initialize original file path
    revised_file_path = ""  # Initialize revised file path
    original_code = ""  # Initialize original code content
    revised_code = ""  # Initialize revised code content
    original_file_name = ""  # Initialize original file name
    revised_file_name = ""  # Initialize revised file name
    diff_output = ""  # Initialize difference output
    metrics = {}  # Initialize metrics dictionary

    # Step 1: Handle CSV file upload if a file is provided in the request
    if request.method == 'POST':
        csv_file = request.files.get('csv_file')  # Get the uploaded CSV file
        if csv_file:
            # Save the uploaded CSV file to a specified location
            csv_file_path = os.path.join(UPLOAD_FOLDER, csv_file.filename)
            csv_file.save(csv_file_path)

            # Process the CSV file: Read and convert it into a list of lines
            with open(csv_file_path, 'r') as file:
                csv_reader = csv.DictReader(file)
                csv_lines = list(csv_reader)

            # Redirect to avoid form resubmission on page refresh
            return redirect(url_for('compare_files'))

        # Step 2: Handle file selection for comparison
        selected_file_name = request.form.get('file_selection')  # Get the selected file name from the form
        if selected_file_name and csv_lines:  # Proceed if a file is selected and CSV lines exist
            for line in csv_lines:
                # Find the matching line for the selected file
                if line['file_name'] == selected_file_name:
                    original_file_path = line['file_Location']  # Set the original file path
                    original_file_name = line['file_name']  # Set the original file name

                    # Step 3: Generate the revised file path by modifying the original directory
                    original_directory = os.path.dirname(original_file_path)
                    revised_file_name = f"{line['file_name']}"  # Set the revised file name
                    revised_file_path = os.path.join(original_directory.replace("EIS", "EIS.Revised"), revised_file_name)

                    # Step 4: Normalize file paths for different operating systems (Windows vs Unix)
                    revised_file_path = revised_file_path.replace("\\", "/")

                    # Step 5: Read the contents of both the original and revised files
                    original_code = read_file_contents(original_file_path)
                    revised_code = read_file_contents(revised_file_path)

                    # Step 6: Generate the diff output by comparing the original and revised code
                    diff = difflib.unified_diff(
                        original_code.splitlines(),
                        revised_code.splitlines(),
                        fromfile=original_file_name,
                        tofile=revised_file_name,
                        lineterm=''
                    )
                    diff_output = highlight_differences(diff)  # Highlight the differences

                    # Step 7: Calculate metrics based on the original and revised code
                    metrics = calculate_all_metrics(original_code.splitlines(), revised_code.splitlines())
                    break  # Exit the loop once the correct file is found

    # Step 8: Get the list of unique file names from the CSV lines for file selection dropdown
    files = sorted(set(line.get('file_name') for line in csv_lines)) if csv_lines else []

    # Step 9: Render the comparison results in the HTML template
    return render_template('Code_Comparison.html', files=files, original_code=original_code,
                           revised_code=revised_code, original_file_name=original_file_name,
                           original_file_path=original_file_path, revised_file_name=revised_file_name,
                           revised_file_path=revised_file_path, diff_output=diff_output, metrics=metrics)

if __name__ == '__main__':
    # Step 1: Set up the OpenAI API key
    openai.api_key = 'your-openai-api-key'  # Insert your OpenAI API key here
    # Step 2: Run the Flask application
    # The app will run in debug mode, which is useful during development
    # Replace 'debug=True' with 'debug=False' for production deployment
    app.run(debug=True)  # Replace with `debug=False` for production
