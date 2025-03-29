https://huggingface.co/spaces/SpRaay/Nyaya-Mitra


# Nyaya Mitra - Indian Legal Assistant

## Overview
**Nyaya Mitra** is a comprehensive legal assistant designed to help users with various legal services, including:
- **Legal Research & Analysis**
- **Legal Consultation**
- **Contract Drafting**
- **Legal Document Review**
- **Case Outcome Prediction**

Built using **Streamlit** and **CrewAI**, it integrates multiple AI-powered agents to assist users in understanding and managing legal matters efficiently.

## Features
### 1. Legal Research 📚
- Generate structured legal research reports on any topic.
- AI-driven summarization of legal findings.
- Downloadable research reports in markdown format.

### 2. Legal Advice 💬
- Get personalized legal advice based on queries.
- AI analyzes and provides detailed legal insights.
- Results are available for viewing and downloading.

### 3. Contract Drafting 📝
- Generate customized legal contracts.
- Specify contract type and requirements.
- AI drafts contracts based on input details.

### 4. Legal Document Review 🔍
- Upload and analyze legal documents (PDF, TXT, DOCX).
- Identify potential risks and improvements.
- AI-powered document assessment.

### 5. Legal Case Prediction ⚖️
- Predict potential case outcomes based on legal precedents.
- AI-driven case analysis based on user inputs.

## Installation
### Prerequisites
Ensure you have Python installed (version 3.8+ recommended). Install dependencies using:
```bash
pip install -r requirements.txt
```

### Running the Application
To start the Streamlit app, run:
```bash
streamlit run app.py
```

## File Structure
```
NyayaMitra/
│-- app.py               # Main Streamlit application
│-- agents.py            # AI Agents for various legal tasks
│-- tasks.py             # Tasks executed by agents
│-- requirements.txt     # Dependencies
│-- outputs/             # Folder for storing generated reports
│-- image.png            # Sidebar logo
```

## Usage
1. Select the required legal service from the sidebar.
2. Enter relevant details or upload documents.
3. Submit your request.
4. View and download AI-generated results.

## Technologies Used
- **Streamlit** - For the web interface.
- **CrewAI** - To manage AI-powered agents.
- **PyPDF2** - For PDF document processing.
- **Python-Docx** - For DOCX file analysis.
- **OpenAI GPT / Gemini API** - AI-driven legal analysis.

## Disclaimer
This legal assistant is for informational purposes only and does not constitute legal advice. Consult a qualified legal professional for specific legal concerns.

---
**Made with ❤️ by Atharva**

