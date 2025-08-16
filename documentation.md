# AI-Powered ATS Resume Analyzer: Technical Documentation

## 1. Introduction

This document provides a detailed technical overview of the AI-Powered Applicant Tracking System (ATS). The system is designed to automate the process of resume screening by leveraging a sophisticated multi-agent architecture. It can parse resumes, score them against job descriptions, and provide actionable feedback for improvement, all through an intuitive web interface.

## 2. System Architecture

The core of this application is a multi-agent system built with Microsoft Autogen. Each agent is a specialized AI model responsible for a specific task. The agents collaborate to process a resume and provide a comprehensive analysis.

### Agent Descriptions

- **`UserProxyAgent`**: Represents the user in the conversation, capturing initial input (like the resume file).

- **`TextExtractorAgent`**: Receives the resume file and extracts the raw text content. It is responsible for handling different file formats (PDF, DOCX) and preparing the text for further processing.

- **`JobDescriptionAgent`**: Fetches relevant job descriptions using the `JSearch` API. It takes the extracted resume content as input to find matching job roles.

- **`ATS_ScoringAgent`**: This is the core analysis agent. It takes the extracted resume text and the job description, then scores the resume based on how well it matches the job requirements. It identifies key skills, experiences, and qualifications.

- **`ImprovementAgent`**: After the `ATS_ScoringAgent` provides a score, this agent analyzes the results and provides specific, actionable suggestions for how the user can improve their resume to better match the job description.

- **`SummaryAgent`**: Creates a concise summary of the overall analysis, including the ATS score and key improvement areas.

- **`RAGAgent` (Retrieval-Augmented Generation)**: This agent leverages a memory tool to provide context-aware responses or answer specific user queries based on the ongoing analysis.

- **`VisualizationAgent`**: Generates visualizations (e.g., charts, graphs) to represent the ATS score, skill gaps, or other relevant metrics, making the analysis easier to understand.

- **`CodeExecutorAgent`**: A critical security component that executes code within a sandboxed Docker environment. This is used for any tasks that require code execution, such as running analysis scripts or generating visualizations, ensuring that no arbitrary code runs on the host machine.

### Agent Interaction Flow

1.  The **`UserProxyAgent`** initiates the process with a user's resume.
2.  The **`TextExtractorAgent`** parses the resume.
3.  The **`JobDescriptionAgent`** finds a relevant job description.
4.  The **`ATS_ScoringAgent`** scores the resume against the job description.
5.  The **`ImprovementAgent`** provides feedback.
6.  The **`SummaryAgent`** summarizes the findings.
7.  The **`VisualizationAgent`** may be called to create charts.
8.  Throughout the process, the **`RAGAgent`** can provide additional information, and the **`CodeExecutorAgent`** ensures safe execution of any required scripts.

## 3. Core Components

- **`main.py`**: The entry point of the Streamlit web application. It handles the user interface, file uploads, and orchestrates the agent team.

- **`src/team/`**: This directory contains the logic for creating and managing the team of agents.

- **`src/models/`**: Contains the configurations for the different language models used by the agents (e.g., OpenAI, Groq).

- **`src/tools/`**: Includes tools that agents can use, such as the `JSearch` API wrapper and the database tools for saving and retrieving data.

- **`src/config/`**: Manages configuration details, such as loading prompts for the agents and Docker settings.

## 4. API Reference

Each agent class in `src/agents/` follows a similar pattern:

- **`__init__(self)`**: Initializes the agent, loads its system prompt, and sets up the required model client.
- **`get_agent(self)`**: Returns an instance of the `AssistantAgent` (or other Autogen agent type) configured with the system message, model, and any specific tools.

## 5. Developer Guide

### Setting Up the Environment

1.  Follow the installation steps in the `README.md` to set up the project, including installing dependencies and setting up environment variables.
2.  Ensure Docker is installed and running, as it is essential for the `CodeExecutorAgent`.

### Running Tests

(To be added: Instructions on how to run tests for the project, e.g., using `pytest`.)

### Contributing

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Make your changes and ensure all tests pass.
4.  Submit a pull request with a clear description of your changes.
