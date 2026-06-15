# MCQ Generator

An AI-powered MCQ Generator built with Streamlit, LangChain, and OpenAI.

Users can upload a PDF, extract its content, and automatically generate multiple-choice questions based on the uploaded material.

---

## Features

- Upload PDF documents
- Extract text from PDFs
- Generate MCQs using OpenAI
- Select subject name
- Choose difficulty level (Easy, Medium, Hard)
- Configure number of questions
- Streamlit-based user interface

---

## Project Structure

```text
mcqgen/
│
├── StreamlitApp.py          # Streamlit UI
├── response.json            # Expected MCQ JSON format
├── requirements.txt
├── README.md
|
│
├── experiment/
│   ├── mcq.ipynb            # Development notebook
│   └── data.txt
│
└── src/
    └── mcqgenerator/
        ├── utils.py         # PDF extraction & quiz generation
        ├── logger.py
        ├── test.py
        └── __init__.py
```

---

## Installation

Clone the repository:

```bash
 git clone https://github.com/daiminimrah-glitch/mcqgen.git
cd mcqgen
```

Create a virtual environment:

```bash
python -m venv env
```

Activate the environment:

### Windows

```bash
env\Scripts\activate
```

### Git Bash

```bash
source env/Scripts/activate
```

## Install dependencies:

```bash
pip install -r requirements.txt
```

## Configuration

This project uses the OpenAI API to generate multiple-choice questions. To run the application, create a `.env` file in the project directory and add your OpenAI API key:

```env
OPENAI_API_KEY=your_api_key_here
```

## Run the Application

Start Streamlit:

```bash
streamlit run StreamlitApp.py
```

The application will open automatically in your browser.

---

## Usage

1. Upload a PDF document.
2. Enter the subject name.
3. Select the number of questions.
4. Choose a difficulty level.
5. Click **Generate Quiz**.
6. View the generated MCQs.

---

## Technologies Used

- Python
- Streamlit
- OpenAI API
- LangChain
- PyPDF
- Python Dotenv

---

## Future Improvements

- Interactive quiz interface
- Quiz scoring system
- Export generated MCQs to CSV
- Support for DOCX and TXT files
- Question review and editing

---

## Author

**Syeda Namrah Daimi**

Master's Student, Computer Science  
Roosevelt University
