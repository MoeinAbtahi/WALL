# WALL: A Web Application for Automated Quality Assurance using Large Language Models

**WALL** is a web-based tool designed to help developers improve software quality by resolving code issues, revising them using Large Language Models (LLMs), and comparing code versions. This application integrates with SonarQube to fetch the unresolved problems and uses advanced AI models for automated code revision.

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

## Prerequisites

Before installing SonarQube, ensure your system meets the following requirements:

1. **Operating System**: Windows, macOS, or Linux
2. **Memory**: At least 2GB of free RAM
3. **Disk Space**: 1GB for SonarQube installation
4. **Java**: Obtain the appropriate JDK 17 installer from [Oracle's official website](https://www.oracle.com/java/technologies/javase/jdk17-archive-downloads.html). This version has been confirmed as compatible with SonarQube based on the [SonarQube Scanner Environment Requirements](https://docs.sonarsource.com/sonarqube-server/10.8/analyzing-source-code/scanners/scanner-environment/general-requirements/).

   Download JDK 17 for your operating system and follow the installation instructions provided by the installer.

   After installing JDK 17, open a terminal or command prompt and run the following command to verify the installation:  

   ```bash
   java -version
   ```  

   If the installation was successful, you should see an output similar to the following:  

   ```
   java version "17.0.8" 2023-07-18 LTS
   Java(TM) SE Runtime Environment (build 17.0.8+9-LTS-211)
   Java HotSpot(TM) 64-Bit Server VM (build 17.0.8+9-LTS-211, mixed mode, sharing)
   ```
5. **Node.js®**: Obtain the appropriate Node.js installer from [Node.js's official website](https://nodejs.org/en/download).
   
   Download Node.js® for your operating system and follow the installation instructions provided by the installer.
 
   After installing Node.js®, open a terminal or command prompt and run the following command to verify the installation:  

   ```bash
   node --version
   ```  

   If the installation was successful, you should see an output similar to the following:  

   ```
    v18.16.0
   ```


---

## SonarQube

### Step 1: Download SonarQube

   Visit the [SonarQube Download Page](https://www.sonarqube.org/downloads/) to obtain the latest Community Edition. For example, the [sonarqube-25.2.0.102705](https://binaries.sonarsource.com/Distribution/sonarqube/sonarqube-25.2.0.102705.zip) release has been successfully installed and is actively used in the WALL project.

### Step 2: Extract and Configure SonarQube  

1. **Extract the SonarQube ZIP File**:  
   Unzip the downloaded SonarQube archive to your desired installation directory.  

2. **Navigate to the Configuration Directory**:  
   Open the `sonarqube-x.x/conf` directory and edit the `sonar.properties` file using a text editor.  
   - For example, if you downloaded **SonarQube 25.2.0.102705** and are using Windows, navigate to `sonarqube-25.2.0.102705\conf`
     Open `sonar.properties` with **Notepad** or any text editor of your choice.
     
3. **Modify the SonarQube Web Port**:
   
   - In `sonar.properties`, search for the setting:  
     ```
     sonar.web.port
     ```
   - Locate **line 111** (or search for the line that contains `#sonar.web.port=9000`).  
   - Uncomment this line by removing the `#` and change the port from `9000` to `9099` (as `9099` is less commonly used).  
   - Before modification:
       
     ```
     #sonar.web.port=9000
     ```
   - After modification:
      
     ```
     sonar.web.port=9099
     ```
   - Save the changes and close the file.
     
### Step 3:  Download SonarScanner CLI

   Visit [the SonarScanner](https://docs.sonarsource.com/sonarqube-server/10.8/analyzing-source-code/scanners/sonarscanner/) to obtain the latest SonarScanner. For example, the [sonar-scanner-cli-7.0.2.4839-windows-x64](https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-7.0.2.4839-windows-x64.zip?_gl=1*1x9i4t6*_gcl_aw*R0NMLjE3NDEwNTkyMDEuQ2p3S0NBaUF3NVctQmhBaEVpd0FwdjRnb093dEx6dVFkNnR0Sl9OcTlRQU1CajZpUmdZTWVlU0JRbDl0anBBcHQweXloTmt4NnJoRVNCb0N6ZVVRQXZEX0J3RQ..*_gcl_au*ODU4NDI5Mzk3LjE3NDEwMjcwMzc.*_ga*Njc3MzQwOTE0LjE3NDEwMjcwMzU.*_ga_9JZ0GZ5TC6*MTc0MTA1OTA4Mi4zLjEuMTc0MTA1OTIwNi41My4wLjA.) release has been successfully installed and is actively used in the WALL project.

### Step 4: Extract and Configure SonarScanner CLI 

1. **Extract the SonarScanner CLI ZIP File**:  
   Unzip the downloaded SonarQube archive to your desired installation directory.  

2. **Add SonarScanner to Your System Path**:
   For example, if you downloaded **sonar-scanner-7.0.2.4839-windows-x64** and are using Windows,
   - Open the Start Menu and search for Environment Variables.
   - Click on Edit the system environment variables.
   - In the System Properties window, click on the Environment Variables button.
   - Under System variables, find and select Path, then click Edit.
   - Click New and add the path to your SonarScanner bin directory (e.g., C:\sonar-scanner-7.0.2.4839-windows-x64\bin).
   - Click OK to save and exit the Environment Variables window.

      ![image](https://github.com/user-attachments/assets/9adbd161-8d24-432d-bc10-ea20d922eb1d)

    - Open a new Command Prompt and run:
     
     ```cmd
     sonar-scanner -v
     ```
     If the installation was successful, you should see an output similar to the following:

     ```
        22:44:36.006 INFO  Scanner configuration file: C:\Users\100909323\Moein\SonarQube\sonar-scanner-7.0.2.4839-windows-x64\bin\..\conf\sonar-scanner.properties
        22:44:36.012 INFO  Project root configuration file: NONE
        22:44:36.026 INFO  SonarScanner CLI 7.0.2.4839
        22:44:36.028 INFO  Java 17.0.13 Eclipse Adoptium (64-bit)
        22:44:36.029 INFO  Windows 11 10.0 amd64
    ```
     
   - For other operating systems, refer to the following guide for detailed installation instructions: [How to Install SonarScanner CLI on Windows, Linux, and macOS](https://medium.com/novai-devops-101/how-to-install-sonarscanner-cli-client-on-windows-linux-and-macos-94b033f719c4).

### Step 4: Start SonarQube
1. Open a terminal or command prompt.
2. Navigate to the `sonarqube-x.x/bin/<OS>/` directory, replacing `<OS>` with your operating system (e.g., `windows-x86-64` or `linux-x86-64`).  
   For example, if you downloaded **SonarQube 25.2.0.102705** and are using Windows, go to `sonarqube-25.2.0.102705\bin\windows-x86-64`.
3. Run the startup script:
   - On Linux/macOS:
     
     ```bash
     ./sonar.sh start
     ```
     
   - On Windows:
     
     ```cmd
     StartSonar.bat
     ```
     
![image](https://github.com/user-attachments/assets/2bec0c01-1a56-49ad-b4f9-c8b9907d88c4)

4. After seeing the **"SonarQube is operational"** message in the command prompt, verify that SonarQube has started successfully by opening the following URL in your web browser: [http://localhost:9099](http://localhost:9099). If the page loads correctly, SonarQube is running and ready for use.

![image](https://github.com/user-attachments/assets/0f4d5f90-e616-4d58-a083-08079e338093)


### Step 4: Using SonarQube

1. **Access the Dashboard**:
   - Open your web browser and go to [http://localhost:9099](http://localhost:9099).
   - Login using the default credentials:
  
   ```bash
   - Username: `admin`
   - Password: `admin`
   ```
   
2. **Change Default Password**:
   - After logging in for the first time, you will be prompted to change the default password.
   - Update the password for enhanced security.

3. **Add a Project**:
   - Create a new project in SonarQube by clicking **Create a local project**.

![image](https://github.com/user-attachments/assets/df05c532-7271-4469-b8ed-9428f6d8c1d9)

   - Provide a **project display name** and **project key**.

![image](https://github.com/user-attachments/assets/f497919c-3e0a-451b-8ee1-20c0cff602ee)

   - Selet **Use the global setting** for the project baseline.

![image](https://github.com/user-attachments/assets/61e0a20d-c8b1-4011-b560-2c9ea47dfe7c)

   - For the analysis method, choose **Locally**.

![image](https://github.com/user-attachments/assets/994a2d52-be68-444c-ab76-7131f380d163)

   - Select a **token name** and **expiration date**, then generate a token to authenticate the analysis process.

![image](https://github.com/user-attachments/assets/48735916-10a4-4c20-bfcb-701e62e2a1c7)

   - Click on **Maven, Gradle, .NET, or Others** (for other programming languages), then select your operating system to download the appropriate version.
   - Copy the provided command and run it in the **terminal** or **command prompt**.
   - Navigate to your project folder and execute the copied command.
     **For example, if you are using Windows:** Open a **command prompt (cmd)**, navigate to your project folder, and run a command similar to this: 
     
     ```bash
      sonar-scanner.bat -D"sonar.projectKey=open-instruct-main" -D"sonar.sources=." -D"sonar.host.url=http://localhost:9099" -D"sonar.token=sqp_aae99670a14a47375503d78c86e1ddf933780ea6"
     
     ```
          
1. ![image](https://github.com/user-attachments/assets/ba1fb05f-a4de-485d-9033-de08e6a48c81)

2. ![image](https://github.com/user-attachments/assets/2457b01e-0147-46f5-88b5-4cd022c5435c)

3. The time required to add a project to SonarQube varies based on the number of files in the project. For example, adding the **`open-instruct-main`** project takes approximately **1 minute**.

   ![image](https://github.com/user-attachments/assets/8a3ede89-295f-4896-9aad-a11fddbd0059)

4. **Analyze a Project**:
Once the analysis is complete, open [http://localhost:9090](http://localhost:9090) and:
1. Click on your project name.
2. Navigate through:
   - **Issues:** Shows bugs, vulnerabilities, and code smells.
   - **Security Hotspots:** Highlights security concerns.
   - **Code Coverage:** Displays test coverage (if configured).
   - **Duplications:** Identifies duplicate code sections.
   - Etc.

---

## Troubleshooting

### Common Issues:
1. **SonarQube Fails to Start**:  
   - Check `sonarqube-x.x/logs/sonar.log` for detailed error messages.
   - Ensure the database connection is properly configured.
2. **Browser Access Issues**:  
   - Verify that port `9099` is not blocked or used by another application.

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


