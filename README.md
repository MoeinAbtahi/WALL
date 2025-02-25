# WALL: A Web Application for Automated Quality Assurance using Large Language Models

**WALL** is a web-based tool designed to help developers improve software quality by resolving code issues, revising them using Large Language Models (LLMs), and comparing code versions. This application integrates with SonarQube to fetch unresolved issues and uses advanced AI models for automated code revision.

## Project Structure
```bash
WALL/
├── Code Issues Reviser Module - Processing All Files.py
├── README.md
├── Test.Dataset
│   ├── open-instruct-main.Revised
│   ├── open-instruct-main.zip
│   └── open-instruct.Issues.csv
├── app.py
├── requirements.txt
├── static
│   ├── Code_Comparison.css
│   ├── Code_Issue_Reviser.css
│   ├── Wall-Logo.png
│   ├── index.css
│   └── sonarqube.css
└── templates
    ├── Code_Comparison.html
    ├── Code_Issue_Reviser.html
    ├── index.html
    └── sonarqube.html
```
### **Prerequisites**

# 1. SonarQube Installation and Usage Guide

SonarQube is an open-source platform for continuous inspection of code quality, enabling developers to detect bugs, vulnerabilities, and code smells in their projects.

---

## Prerequisites

Before installing SonarQube, ensure your system meets the following requirements:

- **Operating System**: Windows, macOS, or Linux
- **Java**: JDK 11 or higher (required to run SonarQube)
- **Database**: 
  - PostgreSQL 9.6–15
  - MySQL 5.7/8.0
  - Oracle 12c/19c/21c
  - Microsoft SQL Server 2017/2019/2022
- **Memory**: At least 2GB of free RAM
- **Disk Space**: 1GB for SonarQube installation (additional space may be needed for the database)

---

## Installation

Follow these steps to install SonarQube:

### Step 1: Download SonarQube
1. Visit the [SonarQube Download Page](https://www.sonarqube.org/downloads/).
2. Download the latest **Community Edition** or your preferred edition.

### Step 2: Install Java
1. Download and install [JDK 11 or higher](https://jdk.java.net/).
2. Verify the installation by running:
   ```bash
   java -version
   ```

### Step 3: Configure SonarQube
1. Extract the downloaded SonarQube ZIP file.
2. Navigate to the `sonarqube-x.x/bin/<OS>/` directory (replace `<OS>` with your system, e.g., `windows-x86-64` or `linux-x86-64`).
3. Edit the `sonar.properties` file in the `conf` directory:
   - Configure the database connection.
   - Set any additional server properties as needed.

### Step 4: Start SonarQube
1. Open a terminal or command prompt.
2. Navigate to the `bin/<OS>/` directory.
3. Run the startup script:
   - On Linux/macOS:
     ```bash
     ./sonar.sh start
     ```
   - On Windows:
     ```cmd
     StartSonar.bat
     ```
4. Check if SonarQube started successfully by visiting:  
   [http://localhost:9000](http://localhost:9000)

---

## Using SonarQube

### Step 1: Access the Dashboard
1. Open your web browser and go to [http://localhost:9000](http://localhost:9000).
2. Login using the default credentials:
   - Username: `admin`
   - Password: `admin`

### Step 2: Change Default Password
1. After logging in for the first time, you'll be prompted to change the default password.
2. Update the password for enhanced security.

### Step 3: Analyze a Project
1. Create a new project in SonarQube by clicking **"Create Project"**.
2. Provide a **project key** and **name**.
3. Generate a token to authenticate the analysis.

### Step 4: Configure Your Code for Analysis
1. Download and install the SonarQube Scanner for your build system:
   - **Maven**: Use the SonarQube Maven plugin.
   - **Gradle**: Use the SonarQube Gradle plugin.
   - **CLI**: Use the SonarQube Scanner CLI.
2. Add the token and project details to the configuration file for your scanner (e.g., `sonar-project.properties` for CLI).

### Example Configuration:
```properties
sonar.projectKey=your_project_key
sonar.host.url=http://localhost:9000
sonar.login=your_generated_token
```

3. Run the scanner to analyze your code.

### Step 5: View Results
1. Once the analysis is complete, view the results in the SonarQube dashboard.
2. Inspect issues, bugs, and vulnerabilities, and prioritize fixes.

---

## Troubleshooting

### Common Issues:
1. **SonarQube Fails to Start**:  
   - Check `logs/sonar.log` for detailed error messages.
   - Ensure the database connection is properly configured.
2. **Browser Access Issues**:  
   - Verify that port `9000` is not blocked or used by another application.

### Log Files:
- Logs are located in the `logs` directory of the SonarQube installation:
  - `sonar.log`: General logs
  - `web.log`: Web server logs
  - `ce.log`: Compute Engine logs
  - `es.log`: Elasticsearch logs

---

## Additional Resources

- [SonarQube Documentation](https://docs.sonarqube.org/)
- [SonarQube Community](https://community.sonarsource.com/)

---

# 2. WALL Installation and Usage Guide

Before using the WALL application, ensure the following setup steps are completed:

1. **Install Python**:
   - Make sure Python is installed on your machine. You can download the latest version of Python from [python.org](https://www.python.org/downloads/).

2. **Install Required Dependencies**:
   - Navigate to the project directory and run the following command to install the required libraries:
     ```bash
     pip install -r ./requirements.txt
     ```
   - This will install all necessary dependencies for the application as listed in the `requirements.txt` file.

3. **Verify Python and Pip Installation**:
   - Ensure both Python and Pip are correctly installed by running the following commands:
     ```bash
     python --version
     pip --version
     ```
   - If these commands return the respective version numbers, the installation is complete.

4. **Check OpenAI API Access**:
   - Confirm that you have a valid OpenAI API key to enable the code revision functionality.

5. **Optional Tools**:
   - Install a code editor like VS Code or PyCharm for better script editing and management.

## Application Overview

The application is designed to:

1. Fetch unresolved code issues from SonarQube.
2. Provide a platform for uploading and revising issues using AI models.
3. Enable code comparison between original and revised versions with detailed metrics.

## Key Functions in App.py

### 1. `get_all_issues(sonar_url, api_token, project_key)`

This function fetches unresolved issues from a SonarQube project using the API.

#### Parameters:
- **sonar_url** (str): The URL of the SonarQube server.
- **api_token** (str): Authentication token for accessing the SonarQube API.
- **project_key** (str): The SonarQube project key to retrieve issues from.

#### Description:
- Retrieves unresolved issues from SonarQube.
- Handles paginated responses to fetch all issues.

### 2. `modify_file_path(original_path, to_remove, to_add)`

This function modifies a file path by removing a prefix and adding a new segment.

#### Parameters:
- **original_path** (str): The initial file path.
- **to_remove** (str): A prefix to be removed.
- **to_add** (str): A new prefix to be added.

#### Description:
- Ensures compatibility across platforms by using forward slashes.
- Adjusts file paths for code revisions.

### 3. `save_csv_file(issues, file_path, to_remove, to_add)`

This function saves a list of code issues to a CSV file after modifying the file paths.

#### Parameters:
- **issues** (list): A list of code issue details.
- **file_path** (str): The destination path for the CSV file.
- **to_remove** (str): A prefix to remove from file paths.
- **to_add** (str): A new prefix to add to the file paths.

#### Description:
- Organizes and saves issue data into a CSV file.
- Allows for file path customization before saving.

### 4. `read_file_contents(file_path)`

Reads the contents of a file and returns them as a string, with each line numbered.

#### Parameters:
- **file_path** (str): The path to the file.

#### Description:
- Reads and formats the file’s contents with line numbers for easier analysis.

### 5. `generate_prompt(file_location, bug_lines, bug_messages, bug_types)`

Generates a prompt for an AI model to fix code issues.

#### Parameters:
- **file_location** (str): The file with issues.
- **bug_lines** (list of int): Line numbers where issues occur.
- **bug_messages** (list of str): Descriptions of the issues.
- **bug_types** (list of str): Types of issues (e.g., Bug, Vulnerability).

#### Description:
- Combines the code with bug descriptions to create a prompt for an AI model.
- Provides a few-shot example to guide the model’s revision.

### 6. `highlight_differences(diff)`

Highlights the differences between two versions of a file in HTML format.

#### Parameters:
- **diff** (list of str): The diff output, showing the differences between the two versions.

#### Description:
- Highlights added and removed lines in the code.
- Displays differences using color-coded HTML for easy comparison.

### 7. `calculate_all_metrics(original_lines, revised_lines)`

Calculates various evaluation metrics comparing original and revised code lines.

#### Parameters:
- **original_lines** (list of str): The original code.
- **revised_lines** (list of str): The revised code.

#### Description:
- Computes metrics like precision, recall, F1 score, BLEU, and ROUGE.
- Provides a detailed assessment of how closely the revised code matches the original.

## Routes

### 1. `/sonarqube`

This route handles fetching issues from SonarQube and saving them to a CSV file.

- **Methods**: GET, POST
- **Steps**: 
  1. Provides a form to enter SonarQube details.
  2. Fetches unresolved issues from SonarQube based on the provided details.
  3. Allows saving the issues in a CSV file.

### 2. `/Code_Issue_Reviser`

This route handles the process of uploading a CSV file, interacting with OpenAI’s API to revise code issues, and updating the UI with results.

- **Methods**: GET, POST
- **Steps**:
  1. Upload and process a CSV file containing code issues.
  2. Generate a prompt for the OpenAI API based on selected issues.
  3. Send the prompt to OpenAI and retrieve the revised code.

### 3. `/Code_Comparer`

This route compares the original and revised versions of a file, calculating and displaying differences and evaluation metrics.

- **Methods**: GET, POST
- **Steps**:
  1. Upload a CSV file with file details.
  2. Select files for comparison.
  3. Highlight code differences and display comparison metrics.

## How to Use

1. **SonarQube Integration**: Start by fetching issues from your SonarQube project via the `/sonarqube` route.
2. **Issue Revision**: Once issues are retrieved, upload the CSV to the `/Code_Issue_Reviser` route to revise the issues using the LLM.
3. **Code Comparison**: After revising the code, use the `/Code_Comparer` route to compare the original and revised code, and evaluate the changes.

## Web Pages

### **Home**
- This page provides users with instructions on how to use MASQA, including descriptions of each action and step-by-step guidance for interacting with the tools.

![Home](https://github.com/user-attachments/assets/e13cad7d-28a8-443c-834a-9217c2af5013)

---

### **Issue Extractor Tool**
- **Purpose**: This page allows users to fetch unresolved issues from SonarQube and save them as a CSV file for further processing.

#### **Steps**:
1. Users can either **preset** or **manually enter** the following details:
   - **SonarQube Server URL**: The address of the SonarQube server.
   - **Project API Token**: Authentication token for accessing SonarQube.
   - **Project Key**: The unique identifier for the SonarQube project.
   - **Project Location**: Path to the original project files.
   - **Save Location**: Path to save the generated CSV file.

![Issue Extractor Tool](https://github.com/user-attachments/assets/47134e8a-8bc6-47a2-8262-b6b65c268cef)

#### **Output CSV Format**:
The extracted data is saved as a CSV file in the following format:

| **file_Location** | **file_name** | **line** | **message** | **type** |
|--------------------|--------------|----------|-------------|----------|
| D:/.../Dockerfile | Dockerfile | 1 | Replace `as` with upper case format `AS`. | CODE_SMELL |
| D:/.../App.css    | App.css    | 30 | Remove this commented-out code.           | CODE_SMELL |

![image](https://github.com/user-attachments/assets/3a5de9d9-9630-4525-9a0f-d556e3f054de)

---

### **Code Issues Reviser**

#### **Part 1: Interactive Revision**
- **Purpose**: Allows users to upload the CSV file generated from the **Issue Extractor Tool** and interactively revise the code issues.

#### **Steps**:

1. **Upload CSV File**:
   - Users upload the CSV file generated in the **Issue Extractor Tool** section.

2. **Select Issues**:
   - From the uploaded CSV file, users can browse and select individual files with issues.

3. **View & Edit**:
   - View the content of the selected file along with its associated issues.
   - A **preset prompt** is automatically generated based on the file content and issue description.
   - Users can **edit the prompt** to refine the instructions before sending it to the GPT API.

4. **Choose GPT Model**:
   - Select the desired GPT model (e.g., GPT-3.5 Turbo or GPT-4o) for processing the prompt.

5. **Send Prompt**:
   - Send the customized or preset prompt to the OpenAI API for code revision.

6. **View & Save Revised Code**:
   - Review the revised version of the file generated by the AI.
   - Save the revised file to a preferred location.

7. **Prepare for Code Comparison** *(Optional)*:
   - If users intend to use the **Code Compare Tool**, they need to organize the revised files in a specific format:
     - Ensure that the **original folder** and the **revised folder** are in the same directory.
     - The **revised folder name** should have `.Revised` appended to the original folder name.
       - Example:
         - **Original Folder**: `D:\Documents\Project\WALL`
         - **Revised Folder**: `D:\Documents\Project\WALL.Revised`
   - Place the revised files in the same relative paths as the original project structure. For example:
     - If the original file is located at:
       ```plaintext
       D:\Documents\Project\WALL\src\app\sample.py
       ```
     - The revised file should be saved as ` Revised.sample.py ` in:

       ```plaintext
       D:\Documents\Project\WALL.Revised\src\app\Revised.sample.py
       ```
8. **Set Up OpenAI API Key**:
   - To enable the code revision feature, insert a valid OpenAI API key by modifying **Line 484** in the script:
     ```python
     openai.api_key = 'your-openai-api-key'  # Insert your OpenAI API key here
     ```
   - Replace `'your-openai-api-key'` with a valid key to avoid API errors.

9. **Proceed to Code Compare Tool** *(Optional)*:
   - After organizing the files, proceed to the **Code Compare Tool** section to compare the original and revised versions for further validation.

![Code Issues Reviser](https://github.com/user-attachments/assets/c50ff09c-f967-4c83-aba3-07445820a0c4)

---

#### **Part 2: Batch Processing**
- **Purpose**: Enables users to revise all files in the CSV at once using the `Code Issues Reviser Module - Processing All Files.py` script.

#### **Setup**:
1. **Set Up OpenAI API Key**:
   - To enable the code revision feature, insert a valid OpenAI API key by modifying **Line 8** in the script:
     ```python
         openai.api_key = 'your-openai-api-key'  # Insert your OpenAI API key here
     ```
   - Replace `'your-openai-api-key'` with a valid key to avoid API errors.

2. Open the Python script and adjust the following lines:
   - **Line 128**: Replace the placeholder with the path to your **original project files**:
     ```python
     to_remove = r"Please enter your project location here"
     ```
   - **Line 132**: Replace the placeholder with the **destination path** for saving the revised files:
     ```python
     to_add = r"Please specify the destination for the revised files here."
     ```
3. **Select GPT Model**:
   - Change the model in **Line 154**:
     ```python
     model="gpt-3.5 Turbo"
     ```
   - For advanced capabilities, update this to another model listed on the OpenAI [Models Documentation](https://platform.openai.com/docs/models).

4. Run the script to process and revise all files at once.

5. **Prepare for Code Comparison**:
   - To use the **Code Compare Tool**, ensure the following:
     - The **original folder** and the **revised folder** must be in the same location.
     - The revised folder name should have `.Revised` appended to the original folder name.
     - Example paths:
       - **Original Folder**: `D:\Documents\Project\WALL`
       - **Revised Folder**: `D:\Documents\Project\WALL.Revised`
---

### Notes
- For batch processing, ensure the script’s paths and model settings are correctly updated.
- While Part 1 is interactive and user-driven, Part 2 offers automation for users needing quick processing of multiple files.

### **Code Compare Tool**

The **Code Compare Tool** enables users to evaluate and compare the original and revised versions of their code for quality and improvements.

![Code Compare Tool](https://github.com/user-attachments/assets/d37124de-b5eb-43b8-9b64-3e8aec5ddc77)

---

#### **Steps**:

1. **Upload CSV File**:
   - Users upload the CSV file created in the **Issue Extractor Tool** section. This file contains details of the original files and their issues.

2. **Select File for Comparison**:
   - From the uploaded CSV, users can browse and select a specific file for comparison.

3. **View Original and Revised Code**:
   - **Original Code**: Displayed on the **left side** of the screen, showing the file with the highlighted issues.
   - **Revised Code**: Displayed on the **right side** of the screen. If the file was revised (using the **Code Issues Reviser** section or manually), the revised version is shown here. If no revised file is available, a message will prompt the user to revise the file first.

4. **Revision Metrics**:
   - The tool generates metrics based on the comparison between the original and revised files. These metrics include:
     - **Change Quality**: An assessment of how well the revisions address the identified issues.
     - **Code Difference Highlighting**: Displays changes made between the original and revised versions, such as additions, deletions, and modifications.
     - **Revision Coverage**: Shows the percentage of issues resolved in the revised file.

5. **Prepare for Final Submission**:
   - Based on the comparison and metrics, users can validate whether the revisions meet quality standards and proceed with finalizing the updated code.

---

# 3. Test Dataset and WALL Application Usage

As shown in **Table II** of the paper, the results are based on the dataset from **Team Eagle Ltd.** ([https://www.team-eagle.ca/](https://www.team-eagle.ca/)). However, I tested the WALL application using the publicly available **open-instruct** GitHub repository ([https://github.com/allenai/open-instruct](https://github.com/allenai/open-instruct)). Below are the step-by-step instructions for using this test dataset with the WALL application.

## 1. Clone the Repository

First, clone the **open-instruct** repository using the following command:

```bash
git clone https://github.com/allenai/open-instruct.git
```

You can clone the repository to any location, but for this example, we will use the following path:

```plaintext
C:\Users\100909323\Desktop\open-instruct-main
```

## 2. Add the Project to SonarQube

Next, install **SonarQube** locally and configure it to use the following server address: `http://localhost:9099/`. After that, create a project in SonarQube called **"WALL"** and add the project files using the following command:

```bash
sonar-scanner.bat -D"sonar.projectKey=WALL" -D"sonar.sources=." -D"sonar.host.url=http://localhost:9099" -D"sonar.token=sqp_b9bd769589a5525f4bfe6774ff71c9724b754565"
```

Where:
- **Project API Token**: `sqp_b9bd769589a5525f4bfe6774ff71c9724b754565`
- **Project Key**: `WALL`

![Screenshot_28-11-2024_12758_localhost](https://github.com/user-attachments/assets/78446b44-a9d7-4a91-ad07-9012b7534c28)

These credentials will be used in the **Issue Extraction** section of the WALL application.

## 3. Issue Extraction in WALL

Once you have your SonarQube credentials, you can extract the issues from SonarQube into a CSV file using the **Issue Extraction** section in the WALL application. Enter the following credentials manually:

- **SonarQube Server URL**: `http://localhost:9099/`
- **SonarQube API Token**: `sqp_b9bd769589a5525f4bfe6774ff71c9724b754565`
- **SonarQube Project Key**: `WALL`
- **Project Location**: `C:\Users\100909323\Desktop\open-instruct-main`
- **CSV File Save Location**: `C:\Users\100909323\Desktop\open-instruct.Issues.csv`

After running the extraction, the issues will be saved in the `open-instruct.Issues.csv` file, located in the `Test.Dataset` directory.

![Screenshot of Issue Extraction](https://github.com/user-attachments/assets/27a66140-5a74-44b4-9830-5f8a76e96425)

## 4. Code Issues Reviser in WALL

Once the issues are extracted, we can proceed to use the **Code Issues Reviser** section.

### 4.1 Code Issues Reviser in the WALL Application

In this section, upload the `open-instruct.Issues.csv` file. You will see the files with issues, and for example, the original and revised versions of the `Dockerfile` using **GPT-4o** are shown below.

![Screenshot of Dockerfile Revision](https://github.com/user-attachments/assets/889928c7-e49a-416c-bbb1-c4da213d8b4d)
![Screenshot of Revised Dockerfile](https://github.com/user-attachments/assets/0c4d40d7-76f5-4339-a111-4dadb48d8e74)

Once the revision is complete, save the revised `Dockerfile` manually.

### 4.2 Code Issues Reviser Script for Revising All Files

To revise all files at once, we used the Python script **Processing All Files.py**. In the script, update the following lines:

- Line 127:
  ```python
  to_remove = r"C:\Users\100909323\Desktop\open-instruct-main"  # Path to the original project files
  ```

- Line 130:
  ```python
  to_add = r"C:\Users\100909323\Desktop\open-instruct-main.Revised"  # Path to save the revised files
  ```

- Define the GPT model (e.g., `gpt-3.5-turbo`) in Line 154:
  ```python
  model="gpt-3.5-turbo",  # Change this to gpt-4o for more advanced capabilities
  ```
![Screenshot 2024-11-28 131709](https://github.com/user-attachments/assets/21470398-1d66-409d-b457-9de7dd711bfd)

***Note that only 25 files with issues in the `open-instruct-main` project were revised. The revised files can be found in the `Test.Dataset/open-instruct-main.Revised` directory.***

## 5. Code Comparison Section in WALL

With the original files, revised files, and CSV file, you can compare the revised files with the original files using the **Code Compare Tool**. To enable this, modify Line 451 of **app.py** as follows:

```python
revised_directory = original_directory.replace("open-instruct-main", "open-instruct-main.Revised")
```
After making the necessary changes, you can use the **Code Compare Tool** to compare the original files with the revised files and assess the quality of the revisions.

### Example: Comparing `mbpp.py` with `Revised.mbpp.py`

In the screenshot below, we compared `mbpp.py` with `Revised.mbpp.py`. The original file (`mbpp.py`) is located at:

```plaintext
C:/Users/100909323/Desktop/open-instruct-main/eval/mbpp/mbpp.py
```

While the revised file (`Revised.mbpp.py`) is located at:

```plaintext
C:/Users/100909323/Desktop/open-instruct-main.Revised/eval/mbpp/Revised.mbpp.py
```

![Screenshot of Code Comparison](https://github.com/user-attachments/assets/cf84146a-fe6f-4780-8ab1-b2bf31c66215)

By using the **Code Compare Tool**, you can visualize the differences between the original and revised files, helping you evaluate the effectiveness of the revisions made by the WALL application.

---


