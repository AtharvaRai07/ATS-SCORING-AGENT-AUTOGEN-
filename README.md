# AI-Powered ATS Resume Analyzer

![Project Banner]([https://raw.githubusercontent.com/sunnysavita10/Meow-Meow-1.0/main/Screenshot%202024-07-26%20120148.png](https://microsoft.github.io/autogen/stable//_static/logo.svg))

[View Technical Documentation](docs/documentation.md)

This project is an advanced Applicant Tracking System (ATS) that leverages a team of AI agents to analyze resumes, score them against job descriptions, and provide actionable feedback for improvement. Built with Streamlit and powered by Autogen, this tool streamlines the recruitment process by automating resume screening and evaluation.

## ✨ Features

- **📄 Multi-Format Resume Parsing**: Upload resumes in PDF or DOCX format.
- **🤖 Multi-Agent System**: Utilizes a team of specialized AI agents for different tasks:
  - `Text Extractor Agent`: Parses and extracts text from resumes.
  - `Job Description Agent`: Fetches and processes job descriptions.
  - `ATS Scoring Agent`: Scores resumes based on relevance to the job description.
  - `Improvement Agent`: Provides suggestions to improve the resume score.
- **💾 Database Integration**: Saves parsed resume data, job descriptions, and scores to a database for tracking and analysis.
- **🐳 Dockerized Environment**: Ensures consistent and reliable execution of agent tasks in a sandboxed environment.
- **📊 Interactive UI**: A user-friendly web interface built with Streamlit for easy file uploads and interaction.

## 🛠️ Tech Stack

- **Frontend**: Streamlit
- **AI Agents**: Microsoft Autogen ![AutoGen Logo](https://raw.githubusercontent.com/microsoft/autogen/main/website/static/img/autogen_agent_light.svg)
- **Database**: PostgreSQL (via `psycopg2`)
- **File Parsing**: `pymupdf`, `python-docx`
- **Containerization**: Docker

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- Docker
- An account with a database provider (e.g., Supabase, ElephantSQL)

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/your-repo-name.git
    cd your-repo-name
    ```

2.  **Create a virtual environment and activate it:**
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
    ```

3.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up environment variables:**
    Create a `.env` file in the root directory and add your database credentials and API keys:
    ```env
    DB_NAME="your_db_name"
    DB_USER="your_db_user"
    DB_PASSWORD="your_db_password"
    DB_HOST="your_db_host"
    DB_PORT="your_db_port"
    OPENAI_API_KEY="your_openai_api_key"
    GROQ_API_KEY="your_groq_api_key"
    ```

### Usage

There are two ways to run this application:

#### 1. Running Locally

1.  **Ensure Docker is running** (required for the agent environment).

2.  **Run the Streamlit application:**
    ```bash
    streamlit run main.py
    ```

3.  Open your web browser and navigate to the local URL provided by Streamlit (usually `http://localhost:8501`).

4.  **Upload a resume** (PDF or DOCX) and select a use case to start the analysis.

#### 2. Running with Docker

Alternatively, you can run the entire application using the pre-built Docker image.

1.  **Pull the Docker image from Docker Hub:**
    ```bash
    docker pull atharvarai07/ats-agent:latest
    ```

2.  **Run the Docker container:**
    ```bash
    docker run -p 8501:8501 atharvarai07/ats-agent:latest
    ```

3.  Open your web browser and navigate to `http://localhost:8501`.

## 🤝 Contact

For any questions or feedback, please reach out to:

- **Atharva Rai**
- **Email**: [atharvarai07@gmail.com](mailto:atharvarai07@gmail.com)
