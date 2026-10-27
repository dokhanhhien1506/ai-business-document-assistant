```markdown
# AI Business Document Assistant

An AI-powered prototype for analyzing business documents,
generating summaries, answering document-based questions,
and extracting actionable tasks.

## Overview

Business professionals often spend time reviewing meeting minutes,
internal reports, and operational documents to identify decisions
and follow-up activities.

This project explores how generative AI can support these workflows
through a simple web interface built with Python and Streamlit.

## Features

- Upload PDF, DOCX, and TXT documents.
- Extract readable text from supported document formats.
- Generate structured executive summaries.
- Ask questions about uploaded document content.
- Extract action items, owners, deadlines, statuses, and evidence.
- Export extracted action items to CSV.
- Flag missing information instead of intentionally filling gaps
  with invented owners or deadlines.

## Technology Stack

- Python
- Streamlit
- OpenAI API
- pandas
- pypdf
- python-docx

## Project Structure

```text
ai-business-document-assistant
+-- app.py
+-- document_processor.py
+-- ai_assistant.py
+-- requirements.txt
+-- .gitignore
+-- .env.example
+-- README.md
```

## Getting Started

### 1. Clone the repository

```bash
git clone httpsgithub.comYOUR-USERNAMEai-business-document-assistant.git
cd ai-business-document-assistant
```

Replace `YOUR-USERNAME` with your GitHub username.

### 2. Create a virtual environment

Windows

```bash
python -m venv .venv
.venvScriptsactivate
```

macOS or Linux

```bash
python3 -m venv .venv
source .venvbinactivate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure your API key

Create a local file named `.env` in the project directory.

Add your own API key

```dotenv
OPENAI_API_KEY=your_actual_api_key
OPENAI_MODEL=gpt-4.1-mini
```

Never commit `.env` or publish your API key.

API usage may incur charges depending on your account and usage.

### 5. Run the application

```bash
streamlit run app.py
```

Streamlit will provide a local URL where you can open the app
in your browser.

## Example Use Cases

- Summarize a business meeting report.
- Ask what decisions were recorded in a document.
- Identify tasks that require follow-up.
- Organize action items into a CSV file for further review.

## Limitations

- Scanned PDFs may require OCR before text can be extracted.
- The prototype limits document input length.
- AI-generated summaries and extracted tasks may contain errors.
- Answers should be checked against the original document.
- The application does not replace professional review.
- Confidential documents should not be uploaded without appropriate
  authorization and an approved data-handling process.

## Evaluation Plan

The next development stage is to test the application against
representative business documents.

Evaluation criteria include

1. Summary relevance and coverage of key information.
2. Accuracy of extracted tasks, owners, and deadlines.
3. Whether answers are supported by document content.
4. Handling of missing, ambiguous, or unavailable information.
5. Usability and clarity of exported action items.

## Development Status

Personal learning project -- prototype in development.

Features should be considered complete only after implementation
and testing.

## Author

Do Khanh Hien

Interests Business Analysis, Generative AI, Data Analytics,
and AI-enabled business workflows.
```
