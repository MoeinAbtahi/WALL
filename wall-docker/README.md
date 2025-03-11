# WALL Docker Setup

This repository provides a Dockerized setup for the WALL application (Web Application for Automated Quality Assurance using Large Language Models) and its dependency, SonarQube. WALL integrates with SonarQube to detect code issues and uses AI (via OpenAI) to suggest fixes. This README guides you through setting up and running the application using Docker on Windows (adaptable to macOS/Linux).

## Prerequisites

- **Docker Desktop**: Installed and running. Download from [Docker's official site](https://www.docker.com/products/docker-desktop/).
- **Git**: Installed for cloning repositories (optional). Download from [Git's official site](https://git-scm.com/).
- **OpenAI API Key**: Required for AI-powered code revision. Sign up at [OpenAI](https://platform.openai.com/signup) and generate an API key.
- **Text Editor**: Notepad or [Visual Studio Code](https://code.visualstudio.com/) for editing files.
- **Command Prompt or PowerShell**: For running Docker commands.

## Directory Structure

```
wall-docker/
├── Dockerfile           # Dockerfile for WALL app
├── docker-compose.yml   # Docker Compose configuration
├── requirements.txt     # Python dependencies for WALL
├── project/             # Directory for your project files (e.g., open-instruct-main)
└── output/              # Directory for output CSV files
```

## Setup Instructions

### Step 1: Clone or Prepare the Repository

1. **Create the Directory**:
   - Open File Explorer (`Win + E`).
   - Navigate to a location (e.g., `C:\Users\YourUsername\Documents`).
   - Create a folder named `wall-docker`.
   - Inside `wall-docker`, create subfolders `project` and `output`.

2. **Copy `requirements.txt`**:
   - Download `requirements.txt` from [WALL GitHub](https://github.com/MoeinAbtahi/WALL/blob/main/requirements.txt).
   - Save it in `C:\Users\YourUsername\Documents\wall-docker`.

3. **Add Project Files (Optional)**:
   - To use the `open-instruct-main` test dataset:
     - Open Command Prompt (`cmd`).
     - Navigate to the `project` folder:
       ```cmd
       cd C:\Users\YourUsername\Documents\wall-docker\project
       ```
     - Clone the repository:
       ```cmd
       git clone https://github.com/allenai/open-instruct.git open-instruct-main
       ```

### Step 2: Create Docker Files

1. **Create `Dockerfile`**:
   - Open Notepad or VS Code.
   - Paste the following content:
     ```dockerfile
     FROM python:3.12-slim

     WORKDIR /app

     RUN apt-get update && apt-get install -y \
         git \
         && rm -rf /var/lib/apt/lists/*

     RUN git clone https://github.com/MoeinAbtahi/WALL.git .

     COPY requirements.txt .
     RUN pip install --no-cache-dir -r requirements.txt

     EXPOSE 5000

     ENV SONAR_URL=http://sonarqube:9099
     ENV SONAR_API_TOKEN=your_sonar_api_token
     ENV SONAR_PROJECT_KEY=your_project_key
     ENV PROJECT_LOCATION=/app/project
     ENV CSV_SAVE_PATH=/app/output/sonarqube_issues.csv
     ENV OPENAI_API_KEY=your_openai_api_key

     CMD ["python", "app.py"]
     ```
   - Save as `Dockerfile` (no extension) in `C:\Users\YourUsername\Documents\wall-docker`.

2. **Create `docker-compose.yml`**:
   - Open Notepad or VS Code.
   - Paste the following content:
     ```yaml
     version: '3.8'

     services:
       sonarqube:
         image: sonarqube:community
         ports:
           - "9099:9000"
         environment:
           - SONAR_WEB_PORT=9000
         volumes:
           - sonarqube_data:/opt/sonarqube/data
           - sonarqube_logs:/opt/sonarqube/logs
           - sonarqube_extensions:/opt/sonarqube/extensions
         networks:
           - wall-network

       wall:
         build:
           context: .
           dockerfile: Dockerfile
         ports:
           - "5000:5000"
         environment:
           - SONAR_URL=http://sonarqube:9000
           - SONAR_API_TOKEN=your_sonar_api_token
           - SONAR_PROJECT_KEY=your_project_key
           - PROJECT_LOCATION=/app/project/open-instruct-main
           - CSV_SAVE_PATH=/app/output/sonarqube_issues.csv
           - OPENAI_API_KEY=your_openai_api_key
         volumes:
           - ./project:/app/project
           - ./output:/app/output
         depends_on:
           - sonarqube
         networks:
           - wall-network

     networks:
       wall-network:
         driver: bridge

     volumes:
       sonarqube_data:
       sonarqube_logs:
       sonarqube_extensions:
     ```
   - Save as `docker-compose.yml` in `C:\Users\YourUsername\Documents\wall-docker`.

3. **Configure Environment Variables**:
   - Open `docker-compose.yml` in your editor.
   - Replace placeholders:
     - `SONAR_API_TOKEN`: Your SonarQube API token (generate from SonarQube after setup).
     - `SONAR_PROJECT_KEY`: Your project key (e.g., `open-instruct-main`).
     - `OPENAI_API_KEY`: Your OpenAI API key.
     - `PROJECT_LOCATION`: Path to your project (e.g., `/app/project/open-instruct-main`).
   - Save the file.

### Step 3: Build and Run

1. **Open Command Prompt**:
   - `Win + R` > `cmd` > Enter.
   - Navigate to the directory:
     ```cmd
     cd C:\Users\YourUsername\Documents\wall-docker
     ```

2. **Build and Start Containers**:
   - Run:
     ```cmd
     docker-compose up --build
     ```
   - Wait for SonarQube to start (may take a few minutes).

3. **Access Services**:
   - **SonarQube**: `http://localhost:9099` (default credentials: `admin`/`admin`).
   - **WALL**: `http://localhost:5000`.

### Step 4: Configure SonarQube

1. Open `http://localhost:9099`.
2. Log in with `admin`/`admin` and change the password.
3. Create a project:
   - Project Key: Match the `SONAR_PROJECT_KEY` in `docker-compose.yml`.
   - Generate a token and update `SONAR_API_TOKEN` in `docker-compose.yml`.
4. Restart if updated:
   ```cmd
   docker-compose down
   docker-compose up --build
   ```

### Step 5: Use WALL

1. Open `http://localhost:5000`.
2. **Issue Extractor Tool**:
   - Use the preconfigured settings from `docker-compose.yml`.
   - Extract issues to a CSV saved in `output/`.
3. **Code Issues Reviser** & **Code Compare Tool**:
   - Follow the WALL interface to revise and compare code.

## Stopping the Containers

- Press `Ctrl + C` in the Command Prompt.
- Remove containers (preserves volumes):
  ```cmd
  docker-compose down
  ```

## Troubleshooting

- **Build Fails**:
  - Ensure `requirements.txt` matches the WALL repo (no `tkinter`).
  - Clear Docker cache:
    ```cmd
    docker builder prune
    ```
- **Port Conflicts**:
  - Check ports 9099 or 5000:
    ```cmd
    netstat -aon | findstr :9099
    taskkill /PID <pid_number> /F
    ```
  - Or edit `docker-compose.yml` ports (e.g., `9098:9000`).
- **SonarQube Slow Start**:
  - Check logs:
    ```cmd
    docker logs wall-docker_sonarqube_1
    ```
- **Permission Issues**:
  - Run Command Prompt as Administrator.

## Notes

- The `output/` folder on your host contains the generated CSV files.
- Adjust `PROJECT_LOCATION` in `docker-compose.yml` if using a different project.
- Ensure Docker Desktop is running before executing commands.

