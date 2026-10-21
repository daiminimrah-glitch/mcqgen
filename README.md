
# QuizForge — AI-Powered Study Assistant
[Live Demo](http://3.146.88.232:8501)

QuizForge is an AI-powered study application built with Python, Streamlit, LangChain, and OpenAI. It currently allows users to upload PDF documents and generate customizable multiple-choice questions from their content.

The project is evolving into a **multi-agent, RAG-powered adaptive learning system** designed to provide personalized, document-grounded study experiences.

The planned system will coordinate specialized AI agents to generate quizzes, explain concepts, create study materials, evaluate student performance, and adapt learning activities based on individual progress.

---

## Features

### Current Features
- Upload PDF documents and extract text.
- Generate multiple-choice questions using OpenAI and LangChain.
- Customize subject, difficulty level, and number of questions.
- View generated questions and correct answers through a Streamlit interface.

### In Development
- **AI Study Agent:** Interpret natural-language study requests and automatically select and execute study tools.
- **Retrieval-Augmented Generation (RAG):** Retrieve relevant information from uploaded documents to support grounded study materials.
- **Document-Based Learning:** Generate quizzes, summaries, and explanations with chapter and page references.

### Planned Features
- **Multi-Agent Collaboration:** Coordinate specialized Planner, Tutor, Quiz, and Evaluator agents.
- **Adaptive Learning:** Analyze quiz performance, identify weak concepts, and generate targeted follow-up activities.
- **Chat with PDF:** Ask questions about uploaded study materials.
- **Learning Progress Tracking:** Save quiz results and monitor improvement over time.
- **Interactive Quiz Interface:** Answer questions directly and receive scores and feedback.
- **React + FastAPI:** Build a dedicated frontend and Python API for the expanded application.

---

## Project Structure
mcqgen/
├── StreamlitApp.py
├── response.json
├── requirements.txt
├── README.md
├── experiment/
│   └── mcq.ipynb
└── src/
    └── mcqgenerator/
        ├── __init__.py
        ├── utils.py
        ├── logger.py
        ├── agent/
        │   ├── __init__.py
        │   ├── planner.py
        │   ├── plan.py
        │   ├── executor.py
        │   ├── tools.py
        │   ├── prompts.py
        │   └── study_agent.py
        └── rag/
            ├── __init__.py
            ├── loader.py
            ├── chunker.py
            ├── embeddings.py
            ├── retriever.py
            └── vector_store.py
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

## Development Roadmap

- [x] PDF upload and text extraction
- [x] AI-powered MCQ generation
- [x] Customizable question difficulty and quantity
- [x] Streamlit-based interface
- [ ] Complete the Study Agent's planning and tool-execution workflow
- [ ] Integrate RAG with chapter and page references
- [ ] Implement specialized Tutor, Quiz, and Evaluator agents
- [ ] Add interactive quizzes and automated scoring
- [ ] Develop adaptive learning with performance-based feedback
- [ ] Implement persistent study progress tracking
- [ ] Add conversational PDF interaction
- [ ] Develop a React frontend and FastAPI backend
- [ ] Support additional document formats and quiz exports

---

## Author

**Syeda Namrah Daimi**

Master's Student, Computer Science  
Roosevelt University
