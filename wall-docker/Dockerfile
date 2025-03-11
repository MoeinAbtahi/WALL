# Dockerfile for WALL Application
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Install system dependencies, including Tk for tkinter
RUN apt-get update && apt-get install -y \
    git \
    tk-dev \
    && rm -rf /var/lib/apt/lists/*

# Clone the WALL repository
RUN git clone https://github.com/MoeinAbtahi/WALL.git .

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Expose the Flask app port
EXPOSE 5000

# Environment variables (to be overridden in docker-compose.yml)
ENV SONAR_URL=http://sonarqube:9099
ENV SONAR_API_TOKEN=your_sonar_api_token
ENV SONAR_PROJECT_KEY=your_project_key
ENV PROJECT_LOCATION=/app/project
ENV CSV_SAVE_PATH=/app/output/sonarqube_issues.csv
ENV OPENAI_API_KEY=your_openai_api_key

# Command to run the Flask app
CMD ["python", "app.py"]