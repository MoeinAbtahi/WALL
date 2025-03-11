# WALL: A Web Application for Automated Quality Assurance using Large Language Models

**WALL** is a web-based tool designed to help developers improve software quality by resolving code issues, revising them using Large Language Models (LLMs), and comparing code versions. This application integrates with SonarQube to fetch the unresolved problems and uses advanced AI models for automated code revision.

# 1. Prerequisites

Before installing SonarQube, ensure your system meets the following requirements:

## 1.1. **Operating System**
Windows, macOS, or Linux
## 1.2. **Memory**
At least 2GB of free RAM
## 1.3. **Disk Space** 
1GB for SonarQube installation
## 1.4. **Java** 
Obtain the appropriate JDK 17 installer from [Oracle's official website](https://www.oracle.com/java/technologies/javase/jdk17-archive-downloads.html). This version has been confirmed as compatible with SonarQube based on the [SonarQube Scanner Environment Requirements](https://docs.sonarsource.com/sonarqube-server/10.8/analyzing-source-code/scanners/scanner-environment/general-requirements/).

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
## 1.5. **Node.js®** 
Obtain the appropriate Node.js installer from [Node.js's official website](https://nodejs.org/en/download).
   
   Download Node.js® for your operating system and follow the installation instructions provided by the installer.
 
   After installing Node.js®, open a terminal or command prompt and run the following command to verify the installation:  

   ```bash
   node --version
   ```  

   If the installation was successful, you should see an output similar to the following:  

   ```
    v18.16.0
   ```
   
## 1.6. **Python** 
Obtain the appropriate Python installer from the [official Python website](https://www.python.org/downloads/).  

   Download Python for your operating system and follow the installation instructions provided by the installer.  
    
   After installing Python, open a terminal or command prompt and run the following command to verify the installation:  
 
 ```bash
 python --version
 ```  
 
 If the installation was successful, you should see an output similar to the following:  
 
 ```
 Python 3.12.9
 ```  

## 1.7. **Visual Studio Code** 
Obtain the appropriate **VS Code** installer from the [official Visual Studio Code website](https://code.visualstudio.com/Download).  

 Download **VS Code** for your operating system and follow the installation instructions provided by the installer.  
 
 After installing VS Code, open a terminal or command prompt and run the following command to verify the installation:  
 
 ```bash
 code --version
 ```  
 
 If the installation was successful, you should see an output similar to the following:  
 
 ```
 1.97.2
 e54c774e0add60467559eb0d1e229c6452cf8447
 x64
 ```
    
## 1.8. **Git** 
Download and install Git from the [official Git website](https://git-scm.com/downloads).
    
  After installing Git, open a terminal or command prompt and run the following command to verify the installation:   

  ```bash
  git --version
  ```

 If the installation was successful, you should see an output similar to the following: 

  ```
  git version 2.48.1.windows.1
  ```

## 1.9. **OpenAI API Key** 
To use OpenAI’s API for the **Code Issue Reviser** section in **WALL**, follow these steps: 

 Visit the [OpenAI playground website](https://platform.openai.com/playground/chat) and sign up.
 
 OpenAI's API is **not free**. You need to add a payment method and buy API credits.
 
 Visit the [billing page](https://platform.openai.com/account/billing) to check pricing and add funds.
  
 Go to the [API Keys page](https://platform.openai.com/api-keys).
 
 Click on **Create new secret key** to generate a new key.
  
 ![image](https://github.com/user-attachments/assets/76c8ae49-a8c7-4fa2-8cb5-762d9f27a2a5)

 Once generated, copy the API key.
 
 **Important:** Store it securely, as OpenAI won’t show it again.  

 ---

# 2. SonarQube

## 2.1. Download SonarQube

   Visit the [SonarQube Download Page](https://www.sonarqube.org/downloads/) to obtain the latest Community Edition. For example, the [sonarqube-25.2.0.102705](https://binaries.sonarsource.com/Distribution/sonarqube/sonarqube-25.2.0.102705.zip) release has been successfully installed and is actively used in the WALL project.

## 2.2. Extract and Configure SonarQube  
 
   Unzip the downloaded SonarQube archive to your desired installation directory.  

   Open the `sonarqube-x.x/conf` directory and edit the `sonar.properties` file using a text editor. For example, if you downloaded **SonarQube 25.2.0.102705** and are using Windows, navigate to `sonarqube-25.2.0.102705\conf`, Open `sonar.properties` with **Notepad** or any text editor of your choice.
   In `sonar.properties`, search for the setting:
  
  ```
  sonar.web.port
  ```
     
   Locate **line 111** (or search for the line that contains `#sonar.web.port=9000`).  
   Uncomment this line by removing the `#` and change the port from `9000` to `9099` (as `9099` is less commonly used).  
   Before modification:
       
   ```
     #sonar.web.port=9000
   ```
     
   After modification:
      
   ```
     sonar.web.port=9099
   ```
     
   Save the changes and close the file.
     
## 2.3. Download SonarScanner CLI

   Visit [the SonarScanner](https://docs.sonarsource.com/sonarqube-server/10.8/analyzing-source-code/scanners/sonarscanner/) to obtain the latest SonarScanner. For example, the [sonar-scanner-cli-7.0.2.4839-windows-x64](https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-7.0.2.4839-windows-x64.zip?_gl=1*1x9i4t6*_gcl_aw*R0NMLjE3NDEwNTkyMDEuQ2p3S0NBaUF3NVctQmhBaEVpd0FwdjRnb093dEx6dVFkNnR0Sl9OcTlRQU1CajZpUmdZTWVlU0JRbDl0anBBcHQweXloTmt4NnJoRVNCb0N6ZVVRQXZEX0J3RQ..*_gcl_au*ODU4NDI5Mzk3LjE3NDEwMjcwMzc.*_ga*Njc3MzQwOTE0LjE3NDEwMjcwMzU.*_ga_9JZ0GZ5TC6*MTc0MTA1OTA4Mi4zLjEuMTc0MTA1OTIwNi41My4wLjA.) release has been successfully installed and is actively used in the WALL project.

## 2.4. Extract and Configure SonarScanner CLI 

   Unzip the downloaded SonarQube archive to your desired installation directory.  
   
   Add SonarScanner to Your System Path: For example, if you downloaded **sonar-scanner-7.0.2.4839-windows-x64** and are using Windows,
   - Open the Start Menu and search for Environment Variables.
   - Click on Edit the system environment variables.
   - In the System Properties window, click on the Environment Variables button.
   - Under System variables, find and select Path, then click Edit.
   - Click New and add the path to your SonarScanner bin directory (e.g., C:\sonar-scanner-7.0.2.4839-windows-x64\bin).
   - Click OK to save and exit the Environment Variables window.

   ![image](https://github.com/user-attachments/assets/9adbd161-8d24-432d-bc10-ea20d922eb1d)

   Open a new Command Prompt and run:
     
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
     
   For other operating systems, refer to the following guide for detailed installation instructions: [How to Install SonarScanner CLI on Windows, Linux, and macOS](https://medium.com/novai-devops-101/how-to-install-sonarscanner-cli-client-on-windows-linux-and-macos-94b033f719c4).

## 2.5. Start SonarQube

  Open a terminal or command prompt.
  Navigate to the `sonarqube-x.x/bin/<OS>/` directory, replacing `<OS>` with your operating system (e.g., `windows-x86-64` or `linux-x86-64`). For example, if you downloaded **SonarQube 25.2.0.102705** and are using Windows, go to `sonarqube-25.2.0.102705\bin\windows-x86-64`.
  Run the startup script:
  
   On `Linux/macOS`:
     
   ```bash
   ./sonar.sh start
   ```
     
   On `Windows`:
     
   ```cmd
   StartSonar.bat
   ```
     
 ![image](https://github.com/user-attachments/assets/2bec0c01-1a56-49ad-b4f9-c8b9907d88c4)

 After seeing the **"SonarQube is operational"** message in the command prompt, verify that SonarQube has started successfully by opening the following URL in your web browser: [http://localhost:9099](http://localhost:9099). If the page loads correctly, SonarQube is running and ready for use.

 ![image](https://github.com/user-attachments/assets/0f4d5f90-e616-4d58-a083-08079e338093)


## 2.6. Using SonarQube

Open your web browser and go to [http://localhost:9099](http://localhost:9099).
Login using the default credentials:
  
   ```bash
   - Username: `admin`
   - Password: `admin`
   ```
   
After logging in for the first time, you will be prompted to change the default password.
Update the password for enhanced security.

Create a new project in SonarQube by clicking **Create a local project**.

![image](https://github.com/user-attachments/assets/df05c532-7271-4469-b8ed-9428f6d8c1d9)

Provide a **project display name** and **project key**.

![image](https://github.com/user-attachments/assets/f497919c-3e0a-451b-8ee1-20c0cff602ee)

Select **Use the global setting** for the project baseline.

![image](https://github.com/user-attachments/assets/61e0a20d-c8b1-4011-b560-2c9ea47dfe7c)

For the analysis method, choose **Locally**.

![image](https://github.com/user-attachments/assets/994a2d52-be68-444c-ab76-7131f380d163)

Select a **token name** and **expiration date**, then generate a token to authenticate the analysis process.

![image](https://github.com/user-attachments/assets/48735916-10a4-4c20-bfcb-701e62e2a1c7)

Click on **Maven, Gradle, .NET, or Others** (for other programming languages) and then select your operating system to download the appropriate version. Copy the provided command and run it in your terminal or command prompt. Navigate to your project folder and execute the command. **Be sure to keep this command handy—it will be needed later in the [Set Up SonarQube API Token](#3312-set-up-sonarqube-api-token) and [Set Up SonarQube Project Key](#3313-set-up-sonarqube-project-key) sections.**

   - **For example, if you are using Windows:** Open a **command prompt (cmd)**, navigate to your project folder, and run a command similar to this: 
     
   ```bash
   sonar-scanner.bat -D"sonar.projectKey=open-instruct-main" -D"sonar.sources=." -D"sonar.host.url=http://localhost:9099" -D"sonar.token=sqp_aae99670a14a47375503d78c86e1ddf933780ea6" 
   ```
          
![image](https://github.com/user-attachments/assets/ba1fb05f-a4de-485d-9033-de08e6a48c81)

![image](https://github.com/user-attachments/assets/2457b01e-0147-46f5-88b5-4cd022c5435c)

The time required to add a project to SonarQube varies based on the number of files in the project. For example, adding the **`open-instruct-main`** project takes approximately **1 minute**.

![image](https://github.com/user-attachments/assets/8a3ede89-295f-4896-9aad-a11fddbd0059)

Once the analysis is complete, open [http://localhost:9090](http://localhost:9090) and:
   - Click on your project name.
   - Navigate through:
       - **Issues:** Shows bugs, vulnerabilities, and code smells.
       - **Security Hotspots:** Highlights security concerns.
       - **Code Coverage:** Displays test coverage (if configured).
       - **Duplications:** Identifies duplicate code sections.
       - Etc.
     
![image](https://github.com/user-attachments/assets/db132b2e-9041-4d24-bee5-110c01e791a1)


## 2.7. SonarQube Troubleshooting
   
### 2.7.1. SonarQube Fails to Start
      
Check `sonarqube-x.x/logs/sonar.log` for detailed error messages.
Verify that port `9099` is not blocked or used by another application.
    
### 2.7.2. Log Files
    
Logs are located in the `logs` directory of the SonarQube installation:
      - `sonar.log`: General logs
      - `web.log`: Web server logs
      - `ce.log`: Compute Engine logs
      - `es.log`: Elasticsearch logs

## 2.8. Supporting Documents & Resources

[SonarQube Documentation](https://docs.sonarqube.org/)

[SonarQube Community](https://community.sonarsource.com/)

---

# 3. WALL

The application is designed to:  

**Code Issue Detection & Analysis**  
   - Fetches unresolved issues from **SonarQube** (e.g., code smells, security vulnerabilities, bugs).  
   - Provides a structured **issue dashboard** for developers to review problems in their code.  

**AI-Powered Code Revision**  
   - Uses **LLMs (e.g., GPT-4o)** to suggest fixes for detected issues.  
   - Supports **Few-Shot Prompt Learning (FSPL)** to improve issue detection and reasoning.  
   - Allows manual review and refinement of AI-generated code suggestions.  

**Code Comparison & Validation**  
   - Compares the **original and AI-revised code** side by side.  
   - Provides **metrics on accuracy, efficiency, readability, and compliance** with best practices. 


## 3.1. Clone WALL and Install Required Dependencies

Open a terminal or command prompt, navigate to the directory where you want to clone the repository, and run:  

   ```bash
   git clone https://github.com/MoeinAbtahi/WALL.git
   ```

Move into the newly cloned **WALL** directory:  

   ```bash
   cd WALL
   ```

Run the following command to install all necessary dependencies for the WALL application, as listed in the `requirements.txt` file:  

   ```bash
   pip install -r requirements.txt
   ```
 
## 3.2. WALL Overview

### 3.2.1. Project Structure

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

### 3.2.2. **app.py**  

This section explains key functions in `app.py`.  

#### `get_all_issues(sonar_url, api_token, project_key)`  

Fetches unresolved issues from a SonarQube project using the API.  

- **Parameters:**  
  - `sonar_url` (*str*): URL of the SonarQube server.  
  - `api_token` (*str*): Authentication token for accessing the SonarQube API.  
  - `project_key` (*str*): SonarQube project key to retrieve issues from.  

- **Description:**  
  - Retrieves unresolved issues from SonarQube.  
  - Handles paginated responses to fetch all issues.
  
#### `modify_file_path(original_path, to_remove, to_add)`  

Modifies a file path by removing a prefix and adding a new segment.  

- **Parameters:**  
  - `original_path` (*str*): The initial file path.  
  - `to_remove` (*str*): Prefix to be removed.  
  - `to_add` (*str*): New prefix to be added.  

- **Description:**  
  - Ensures compatibility across platforms by using forward slashes.  
  - Adjusts file paths for code revisions.  

#### `save_csv_file(issues, file_path, to_remove, to_add)`  

Saves a list of code issues to a CSV file after modifying file paths.  

- **Parameters:**  
  - `issues` (*list*): List of code issue details.  
  - `file_path` (*str*): Destination path for the CSV file.  
  - `to_remove` (*str*): Prefix to remove from file paths.  
  - `to_add` (*str*): New prefix to add to file paths.  

- **Description:**  
  - Organizes and saves issue data into a CSV file.  
  - Allows for file path customization before saving.  

#### `read_file_contents(file_path)`  

Reads the contents of a file and returns them as a string, with each line numbered.  

- **Parameters:**  
  - `file_path` (*str*): Path to the file.  

- **Description:**  
  - Reads and formats the file’s contents with line numbers for easier analysis.  

#### `generate_prompt(file_location, bug_lines, bug_messages, bug_types)`  

Generates a prompt for an AI model to fix code issues.  

- **Parameters:**  
  - `file_location` (*str*): File containing issues.  
  - `bug_lines` (*list of int*): Line numbers where issues occur.  
  - `bug_messages` (*list of str*): Descriptions of the issues.  
  - `bug_types` (*list of str*): Types of issues (e.g., Bug, Vulnerability).  

- **Description:**  
  - Combines code with bug descriptions to create a structured AI prompt.  
  - Provides a few-shot example to guide the model’s revision.  

#### `highlight_differences(diff)`  

Highlights the differences between two versions of a file in HTML format.  

- **Parameters:**  
  - `diff` (*list of str*): The diff output showing differences between file versions.  

- **Description:**  
  - Highlights added and removed lines in the code.  
  - Displays differences using color-coded HTML for easy comparison.  

#### `calculate_all_metrics(original_lines, revised_lines)`  

Calculates evaluation metrics by comparing original and revised code lines.  

- **Parameters:**  
  - `original_lines` (*list of str*): The original code.  
  - `revised_lines` (*list of str*): The revised code.  

- **Description:**  
  - Computes metrics like precision, recall, F1 score, BLEU, and ROUGE.  
  - Provides a detailed assessment of how closely the revised code matches the original.

#### **`/sonarqube` Route**  

This route handles fetching unresolved issues from SonarQube and saving them to a CSV file.  

- **Methods**: `GET`, `POST`  
- **Functionality**: 
  - Displays a form for entering SonarQube details.  
  - Retrieves unresolved issues from SonarQube based on the provided details.  
  - Saves the fetched issues into a structured CSV file for further processing.  

#### **`/Code_Issue_Reviser` Route**  

This route facilitates the process of uploading a CSV file containing code issues, interacting with OpenAI’s API for revision, and updating the UI with results.  

- **Methods**: `GET`, `POST`  
- **Functionality**:  
  - Uploads and processes a CSV file containing code issues.  
  - Extracts relevant issues and generates a structured prompt for OpenAI’s API.  
  - Sends the prompt to OpenAI, retrieves the revised code, and updates the interface with improved code suggestions.  

#### **`/Code_Comparer` Route**  

This route compares the original and revised versions of a file, providing visual differences and evaluation metrics to assess code improvements.  

- **Methods**: `GET`, `POST`  
- **Functionality**:  
  - Upload a CSV file containing file details.  
  - Selects files for comparison and extracts their contents.  
  - uses a color-coded HTML format to display added and removed lines.    
  - Calculates precision, recall, F1 score, BLEU, and ROUGE scores.  
  - Provides a quantitative assessment of the similarity between the original and revised code versions.

## 3.3. Configuring `app.py` and `Code Issues Reviser Module - Processing All Files`

### 3.3.1. app.py
To properly configure WALL, update the following settings in `app.py` by replacing placeholder values with actual values.  

   #### 3.3.1.1. Set Up SonarQube URL
   To configure the connection to SonarQube, insert a valid SonarQube URL by modifying **Line 260** in `app.py`:  

   ```python
   preset_sonar_urls = ["<Replace with your SonarQube URL>"]
   ```
   Replace `"<Replace with your SonarQube URL>"` with the actual SonarQube server URL to ensure proper connectivity.  
   
   Example:  
   ```python
   preset_sonar_urls = ["http://localhost:9000"]
   ```
      
   #### 3.3.1.2. Set Up SonarQube API Token
   To authenticate API requests, insert a valid SonarQube API token by modifying **Line 261** in `app.py`:  

   ```python
   preset_api_tokens = ["<Replace with your SonarQube API Token>"]
   ```
   Replace `"<Replace with your SonarQube API Token>"` with a valid API token to enable SonarQube issue fetching.  
   
   Example:  
   ```python
   preset_api_tokens = ["sqp_aae99670a14a47375503d78c86e1ddf933780ea6"]
   ```

   #### 3.3.1.3. Set Up SonarQube Project Key 
   To specify the project being analyzed, insert the correct project key by modifying **Line 262** in `app.py`:  

   ```python
   preset_project_keys = ["<Replace with your SonarQube Project Key>"]
   ```
   Replace `"<Replace with your SonarQube Project Key>"` with the actual project key to retrieve issues related to your project.  
   
   Example:  
   ```python
   preset_project_keys = ["open-instruct-main"]
   ```

   #### 3.3.1.4. Set Up Project Location
   To properly analyze the project files, specify the project’s location by modifying **Line 263** in `app.py`:  

   ```python
   preset_project_locations = ["<Replace with the project location on your system>"]
   ```
   Replace `"<Replace with the project location on your system>"` with the absolute path of your project directory.  
   
   *Example (Windows):*
   ```python
   preset_project_locations = ["C:\\Users\\YourUsername\\Projects\\YourProject"]
   ```
   
  *Example (macOS/Linux):* 
   ```python
   preset_project_locations = ["/Users/YourUsername/Projects/YourProject"]
   ```
   
   #### 3.3.1.5. Set Up CSV Save Path
   To store the extracted issues, define a valid save path by modifying **Line 264** in `app.py`:  

   ```python
   preset_save_paths = ["<Replace with the path where you want to save the CSV file>"]
   ```
   Replace `"<Replace with the path where you want to save the CSV file>"` with a valid directory path to store the CSV file containing SonarQube issues.  
   
   *Example (Windows):*
   ```python
   preset_save_paths = ["C:\\Users\\YourUsername\\Documents\\sonarqube_issues.csv"]
   ```
   
   *Example (macOS/Linux):*
   ```python
   preset_save_paths = ["/Users/YourUsername/Documents/sonarqube_issues.csv"]
   ```
   #### 3.3.1.6. Set Up Revised File Path 
   To correctly locate the revised versions of files generated by the LLM, update **Line 451** in `app.py` with the following code:
   
   ```python
   revised_file_path = os.path.join(original_directory.replace("WALL", "WALL.Revised"), revised_file_name)
   ```
   
   **Explanation:**  
   - **`original_directory`**: This variable holds the path to the directory containing the original files with detected issues (e.g., `"WALL"`).  
   - **`.replace("WALL", "WALL.Revised")`**: This method substitutes `"WALL"` with `"WALL.Revised"` in the directory path, indicating that the file has been revised.  
   - **`os.path.join(...)`**: This function combines the modified directory path with `revised_file_name`, resulting in the full path to the revised file.  
   - **Purpose**: This code ensures that the application accesses the revised file from the corresponding `WALL.Revised` directory instead of the original `WALL` directory.
   
   Example on a Windows system: If the original file is located at:  
   ```python
   original_directory = "C:\\Users\\YourUsername\\Projects\\WALL"
   original_file_name = "app.py"
   ```
   Then the complete original file path is:  
   ```python
   original_file_path = "C:\\Users\\YourUsername\\Projects\\WALL\\app.py"
   ```
   After applying the replacement, the variables will update as follows:  
   ```python
   revised_file_path = "C:\\Users\\YourUsername\\Projects\\WALL.Revised"
   revised_file_name = "revised.app.py"
   ```
   Thus, the full revised file path becomes:  
   ```python
   revised_file_full_path = "C:\\Users\\YourUsername\\Projects\\WALL.Revised\\revised.app.py"
   ```
   
   Example on a macOS and linux system: If the original file is located at:  
   ```python
   original_directory = "/Users/YourUsername/Projects/WALL"
   original_file_name = "app.py"
   ```
   Then the complete original file path is:  
   ```python
   original_file_path = "/Users/YourUsername/Projects/WALL/app.py"
   ```
   After applying the replacement, the revised file path will be:  
   ```python
   revised_file_path = "/Users/YourUsername/Projects/WALL.Revised/app.py"
   ```
   
   This configuration ensures that the application correctly accesses the revised files in the `WALL.Revised` directory while preserving the original directory structure.

   #### 3.3.1.7. Set Up OpenAI API Key
   To enable the AI-powered code revision feature, insert a valid OpenAI API key by modifying **Line 484** in `app.py`:  

   ```python
   openai.api_key = 'your-openai-api-key'  # Insert your OpenAI API key here
   ```
   Replace `'your-openai-api-key'` with a valid OpenAI API key to avoid API errors.  
   
   Example:  
   ```python
   openai.api_key = 'sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
   ```

**Finally, save your updated `app.py` file.**

### 3.3.2. Code Issues Reviser Module - Processing All Files

To properly configure the Code Issues Reviser Module, update the following settings in the script by replacing placeholder values with actual values.

#### 3.3.2.1. Set Up OpenAI API Key  
To enable the code revision feature, insert a valid OpenAI API key by modifying **Line 8** in the script:

```python
openai.api_key = 'your-openai-api-key'  # Insert your OpenAI API key here
```
Replace `'your-openai-api-key'` with a valid OpenAI API key to avoid API errors.  

Example:  
```python
openai.api_key = 'sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
```

#### 3.3.2.2. Set Up Original Project Files Path  
Open the Python script and adjust **Line 128** by replacing the placeholder with the absolute path to your original project files:

```python
to_remove = r"Please enter your project location here"
```

Replace `r"Please enter your project location here"` with the correct path where your original project files are located. 

*Example (Windows):*
```python
to_remove = r"C:\Users\YourUsername\Projects\WALL"
```
*Example (macOS/Linux):*
```python
to_remove = r"/Users/YourUsername/Projects/WALL"
```

#### 3.3.2.3. Set Up Revised Files Destination Path  
Adjust **Line 132** in the script by replacing the placeholder with the destination path where the revised files should be stored:

```python
to_add = r"Please specify the destination for the revised files here."
```

Replace the placeholder with the actual destination path for your revised files. 

*Example (Windows):*
```python
to_add = r"C:\Users\YourUsername\Projects\WALL.Revised"
```
*Example (macOS/Linux):*
```python
to_add = r"/Users/YourUsername/Projects/WALL.Revised"
```

#### 3.3.2.4. Select GPT Model  
To select the GPT model for code revision, modify **Line 154** in the script:

```python
model = "gpt-3.5 Turbo"
```

For advanced capabilities, update this to another model as listed on the [OpenAI Models Documentation](https://platform.openai.com/docs/models).

## 3.4. Run WALL

Open a terminal and navigate to the root directory of the **WALL** project.

Then, execute the following command to start the application:

```bash
python app.py
```

After a brief moment, you should see an output similar to this, indicating that the Flask server is running:

```cmd
Running on http://127.0.0.1:5000
```

Finally, open your web browser and go to [http://127.0.0.1:5000](http://127.0.0.1:5000) to access the WALL application.
   
![image](https://github.com/user-attachments/assets/af204cd1-63cb-4bec-8ff6-a26229eadb27)

## 3.5. Pages in WALL

### 3.5.1. **Home**

![Home](https://github.com/user-attachments/assets/e13cad7d-28a8-443c-834a-9217c2af5013)

This page provides users with instructions on how to use WALL, including descriptions of each action and step-by-step guidance for interacting with the tools.

### 3.5.2. **Issue Extractor Tool**

![Issue Extractor Tool](https://github.com/user-attachments/assets/47134e8a-8bc6-47a2-8262-b6b65c268cef)

This page allows users to fetch unresolved issues from SonarQube and save them as a CSV file for further processing.

**Steps**:
Users can either **preset** or **manually enter** the following details:
   - **SonarQube Server URL**: The address of the SonarQube server.
   - **Project API Token**: Authentication token for accessing SonarQube.
   - **Project Key**: The unique identifier for the SonarQube project.
   - **Project Location**: Path to the original project files.
   - **Save Location**: Path to save the generated CSV file.

**Output CSV Format**:
By entering or selecting all of the required details and clicking **Extract the issues**, the extraction process will begin. Please note that this process may take a few moments. Once complete, the extracted data is automatically saved as a CSV file in the specified location, following the format below:

| **file_Location** | **file_name** | **line** | **message** | **type** |
|--------------------|--------------|----------|-------------|----------|
| D:/.../Dockerfile | Dockerfile | 1 | Replace `as` with upper case format `AS`. | CODE_SMELL |
| D:/.../App.css    | App.css    | 30 | Remove this commented-out code.           | CODE_SMELL |

### 3.5.3. **Code Issues Reviser**

#### **Part 1: Interactive Revision**

![Code Issues Reviser](https://github.com/user-attachments/assets/c50ff09c-f967-4c83-aba3-07445820a0c4)

This section allows you to interactively revise code issues by uploading a CSV file generated from the **Issue Extractor Tool**. Follow the steps below:

**Steps:**

1. **Upload CSV File:**  
   - Begin by uploading the CSV file generated from the **Issue Extractor Tool**.

2. **Select Issues:**  
   - Browse through the CSV file and select individual files that have reported issues.

3. **View & Edit:**  
   - **View:** Examine the contents of the selected file along with its associated issues.  
   - **Edit:** A preset prompt is automatically generated based on the file content and the issue description. You have the option to edit this prompt to refine the instructions before sending it to the GPT API.

4. **Choose GPT Model:**  
   - Select the desired GPT model (e.g., GPT-3.5 Turbo or GPT-4) that will process the prompt.

5. **Send Prompt:**  
   - Submit the customized or preset prompt to the OpenAI API for code revision.

6. **View & Save Revised Code:**  
   - **Review:** Check the revised version of the file generated by the AI.
   - **Save:** Save the revised file to your preferred location.

7. **Prepare for Code Comparison (Optional):**  
   If you plan to use the **Code Compare Tool**, ensure the following:
   - **Directory Structure:** The original folder and the revised folder must reside in the same parent directory.
   - **Folder Naming Convention:** The revised folder name should have `.Revised` appended to the original folder name.
     
     **Example:**
     - **Original Folder:**  
       `D:\Documents\Project\WALL`
     - **Revised Folder:**  
       `D:\Documents\Project\WALL.Revised`

   - **Maintain Relative Paths:**  
     Place the revised files in the same relative paths as in the original project structure.  
     
     **For instance:**  
     If the original file is located at:
     ```plaintext
     D:\Documents\Project\WALL\src\app\sample.py
     ```
     Then, the revised file should be saved as `Revised.sample.py` in:
     ```plaintext
     D:\Documents\Project\WALL.Revised\src\app\Revised.sample.py
     ```

8. **Proceed to Code Compare Tool (Optional):**  
   - Once the files are organized, navigate to the **Code Compare Tool** section to compare the original and revised versions for further validation.

This interactive revision process enables a detailed review and refinement of code issues, ensuring that the final revised files meet your quality standards before further processing or deployment.

#### **Part 2: Batch Processing**

**Purpose:**  
This module enables users to revise all files listed in a CSV simultaneously using the `Code Issues Reviser Module - Processing All Files.py` script.


**Setup:**

1. **Open Terminal:**  
   - Navigate to the root directory of the **WALL** project.

2. **Run the Batch Processing Script:**  
   - Execute the following command to start the application:

   ```bash
   python "Code Issues Reviser Module - Processing All Files.py"
   ```
3. **Select CSV File:**  
   - Choose the CSV file generated by the **Issue Extractor Tool**.

![image](https://github.com/user-attachments/assets/b510ad01-6f03-437a-b7c1-0fcd7ed68971)

4. **File Revision Process**

   - After opening the CSV file, the application will automatically begin revising the files according to the modifications you specified in the **Code Issues Reviser Module - Processing All Files.py** script. These revisions follow the configuration changes outlined in the [Set Up OpenAI API Key](#3321-set-up-openai-api-key) section.

5. **Prepare for Code Comparison:**
Before using the **Code Compare Tool**, ensure that:
- The **original folder** and the **revised folder** are located in the same parent directory.
- The revised folder's name is derived from the original folder by appending `.Revised`.

**Example Paths:**
- **Original Folder:**  
  `D:\Documents\Project\WALL`
- **Revised Folder:**  
  `D:\Documents\Project\WALL.Revised`


**Notes:**
- For successful batch processing, verify that the script’s paths and model settings are correctly configured.
- While Part 1 offers an interactive, user-driven approach, Part 2 automates the processing, providing a quick solution for revising multiple files at once.

### 3.5.4. **Code Compare Tool**

The **Code Compare Tool** enables users to evaluate and compare the original and revised versions of their code for quality and improvements.

![Code Compare Tool](https://github.com/user-attachments/assets/d37124de-b5eb-43b8-9b64-3e8aec5ddc77)

**Steps**:

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



















1. **SonarQube Integration**: Start by fetching issues from your SonarQube project via the `/sonarqube` route.
2. **Issue Revision**: Once issues are retrieved, upload the CSV to the `/Code_Issue_Reviser` route to revise the issues using the LLM.
3. **Code Comparison**: After revising the code, use the `/Code_Comparer` route to compare the original and revised code, and evaluate the changes.

## Web Pages




























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


