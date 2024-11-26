import openai
import tkinter as tk
from tkinter import filedialog
import csv
import os

# Set up the OpenAI API key
openai.api_key = 'your-openai-api-key'  # Insert your OpenAI API key here

# Global variables to store code and bug details
original_code = ""
prompt = ""
file_location = ""
file_name = ""

# Function to read the contents of a file
def read_file_contents(file_path):
    # Reads the contents of the provided file path and stores it in the global variable `original_code`.
    global original_code
    with open(file_path, 'r') as file:
        original_code = file.read()

# Function to process each line of the CSV file
def process_csv_lines(lines):
    # Processes each line of the CSV to collect bug details and generate the prompt for the AI model.
    # It also handles the file reading and bug issue extraction from the CSV.

    global prompt, file_location, file_name
    last_file_location = None
    bug_details = []
    
    # Loop through each line in the CSV file
    for line in lines:
        current_file_location = line.get('file_Location')
        
        # Check if we need to read a new file based on file location changes
        if current_file_location != last_file_location and last_file_location is not None:
            if os.path.exists(last_file_location):
                # Read the contents of the last file location
                read_file_contents(last_file_location)
                
                # Prepare the bug details for the prompt
                all_bugs = "\n".join([f"\nCode issue {i+1} detected by SonarQube is on line {bug[0]}, Description of how to solve the code issue is:{bug[1]}" for i, bug in enumerate(bug_details)])
                
                # Formulate the AI prompt with the original code and bug details
                prompt = (
                    f"""Please fix the issues and send back the corrected code without any additional details or descriptions.
                    Ensure that the edited parts are included in the complete code, and all the original lines of code are preserved.
                    The programming language used in the provided code is important for fixing the issues. It may include JavaScript (JSX), YAML, or JavaScript for testing purposes.
                    Here is the original code:

                    {original_code}

                    The code issues detected by SonarQube are:
                    {all_bugs}

                    If the same code issue is present on other lines, please fix those as well.
                    Resolve this bug based on the SonarQube database, and send the corrected code back to me as specified.
                    Ensure the code format matches the original code file.
                    Please only send the code file itself, without any additional details or descriptions (such as the file type or other information).
                    """
                )
                print(prompt)  # For debugging purposes
                
                # Call the main function to send the prompt to the AI for resolution
                main() 
            
            bug_details = []  # Reset the bug details for the new file
            
        # Update the file location and bug details
        file_location = current_file_location
        file_name = line.get('file_name')
        bug_line = line.get('line')
        bug_message = line.get('message')
        bug_details.append((bug_line, bug_message))  # Add the bug details to the list
        
        last_file_location = file_location  # Update the last file location

    # If file location exists, process the remaining bugs
    if file_location and os.path.exists(file_location):
        read_file_contents(file_location)  # Read the last file
        all_bugs = "\n".join([f"\nCode issue {i+1} detected by SonarQube is on line {bug[0]}, Description of how to solve the code issue is:{bug[1]}" for i, bug in enumerate(bug_details)])
        
        # Generate the prompt with the remaining bugs
        prompt = (
            f"""Please fix the issues and send back the corrected code without any additional details or descriptions.
            Ensure that the edited parts are included in the complete code, and all the original lines of code are preserved.
            The programming language used in the provided code is important for fixing the issues. It may include JavaScript (JSX), YAML, or JavaScript for testing purposes.
            Here is the original code:

            {original_code}

            The code issues detected by SonarQube are:
            {all_bugs}

            If the same code issue is present on other lines, please fix those as well.
            Resolve this bug based on the SonarQube database, and send the corrected code back to me as specified.
            Ensure the code format matches the original code file.
            Please only send the code file itself, without any additional details or descriptions (such as the file type or other information).
            """
        )
    # Call the main function to send the prompt to the AI for resolution
    main()

# Function to open and process the CSV file
def open_files_from_csv(csv_file):
    # Opens and processes the CSV file to extract bug information and generate the AI prompt.
    with open(csv_file, 'r') as file:
        csv_reader = csv.DictReader(file)  # Read CSV as a dictionary
        lines = list(csv_reader)  # Convert CSV rows to a list of dictionaries
        process_csv_lines(lines)  # Process the CSV data

# Function to open a file chooser dialog for selecting a CSV file
def open_csv_with_chooser():
    # Opens a file dialog to allow the user to select a CSV file.
    root = tk.Tk()  # Create a root window
    root.withdraw()  # Hide the root window
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])  # Open file chooser dialog
    if file_path:
        open_files_from_csv(file_path)  # Process the selected CSV file

# Function to save the AI response to a file
def save_response_to_file(content, file_location):
    # Saves the AI-generated response to a file in a revised directory.
    global file_name
    # Define the source directory to remove from the file path (e.g., the location of your original project)
    # Example: to_remove = r"D:\Documents\Project\WALL"
    to_remove = r"Please enter your project location here"  # Replace with the path where your original project files are located

    # Define the destination directory where the revised files will be saved
    # Example: to_add = r"C:\Documents\Project\WALL.Revised"
    to_add = r"Please specify the destination for the revised files here."  # Replace with the path where you want the revised files to be saved


    # Adjust the file path for saving the revised file
    Revised_location = to_add + file_location[len(to_remove):]
    output_file_path = os.path.join(Revised_location, file_name)
    
    try:
        # Create directories as necessary and save the content to the output file
        os.makedirs(os.path.dirname(output_file_path), exist_ok=True)
        with open(output_file_path, 'w') as output_file:
            output_file.write(content)
        print(f"Response saved to {output_file_path}")
    except Exception as e:
        print(f"Failed to save the file: {e}")

# Main function to interact with OpenAI and generate the revised code
def main():
    global prompt, file_location
    # Send the prompt to OpenAI's Chat API and get the response
    completion = openai.ChatCompletion.create(
    # Example for changing the model to GPT-4o
    model="gpt-3.5 Turbo",  # Change this to gpt-4o for more advanced capabilities
    # Alternatively, you could use other models as well:
    # model="gpt-3.5-turbo-1106" for a different variant of GPT-3.5, if needed.
        temperature=0.0,
        messages=[
            {
                "role": "system",
                "content": "You are a code developer and code assistant. Ensure that in output you should just generate the revised code without additional texts. DO NOT ADD ``` that shows the type of file language at the beginning of the file."
            },
            {"role": "user", "content": prompt}
        ]
    )
    # Extract the generated content from the response
    generated_content = completion.choices[0].message.content
    
    # Save the generated content to the appropriate file location
    if file_location:
        directory = os.path.dirname(file_location)
        save_response_to_file(generated_content, directory)

# Function to start the process of choosing and opening a CSV file
open_csv_with_chooser()
