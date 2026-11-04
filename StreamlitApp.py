"""
StreamlitApp.py

- Creates the QuizForge user interface using Streamlit.
- Allows students to upload PDFs and select quiz settings.
- Calls utils.py to extract PDF text and generate a quiz.
- Receives the Pydantic-validated quiz.
- Displays questions, multiple-choice options, correct answers, and explanations.

This file handles the frontend, NOT the LLM generation or validation.
"""

import streamlit as st
import base64
from pathlib import Path

from src.mcqgenerator.utils import (
    extract_text_from_pdf,
    generate_quiz
)

# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="QuizForge",
    page_icon="src/mcqgenerator/assets/favicon.png",
    layout="wide",
    initial_sidebar_state="expanded"
)
    
DOODLE_PATH = Path(__file__).resolve().parent / "src" / "mcqgenerator" / "assets" / "corner_doodles.png"

doodle_base64 = base64.b64encode(
    DOODLE_PATH.read_bytes()
).decode("utf-8")

# ==========================================
# QUIZFORGE STYLING
# ==========================================

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;500;600;700;800;900&family=Pacifico&display=swap');

/* Main background */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(
        135deg,
        #0f172a 0%,
        #1e293b 50%,
        #334155 100%
    );
}

/* Default font */
html, body,
[data-testid="stApp"],
[data-testid="stApp"] p,
[data-testid="stApp"] label,
[data-testid="stApp"] input,
[data-testid="stApp"] button {
    font-family: 'Nunito', sans-serif !important;
}

/* Main content */
.main > div {
    background: rgba(255, 255, 255, 0.12);
    backdrop-filter: blur(15px);
    border: 1px solid rgba(255,255,255,0.15);
}

/* Header */
[data-testid="stHeader"] {
    background: transparent;
}

/* Text colors */
h1, h2, h3, h4, p, label {
    color: white !important;
}

/* Headings */
h1, h2, h3, h4 {
    font-family: 'Nunito', sans-serif !important;
    font-weight: 900 !important;
}

/* QuizForge title only */
.quizforge-title {
    font-family: 'Pacifico', cursive !important;
    font-size: 3rem;
    font-weight: 400 !important;
    line-height: 1.7;
    color: white;
    margin-bottom: 0;
}


/* Generate Quiz button */
.stButton > button {
    background: linear-gradient(
        135deg,
        #c084fc,
        #a78bfa
    ) !important;
    color: white !important;
    border: none !important;
    border-radius: 16px !important;
    font-weight: 800 !important;
    padding: 0.6rem 1.5rem !important;
}

/* Button hover */
.stButton > button:hover {
    background: linear-gradient(135deg, #d8b4fe, #c084fc) !important;
    color: white !important;
}

/* Inputs */
.stTextInput input,
.stNumberInput input {
    border-radius: 10px;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background: #1e293b;
}

[data-testid="stSidebar"] * {
    color: white !important;
}

/* File uploader */
[data-testid="stFileUploader"] {
    background: rgba(255,255,255,0.10);
    border: 1px solid rgba(255,255,255,0.15);
    border-radius: 15px;
    padding: 12px;
}

[data-testid="stFileUploader"] button {
    background: rgba(255,255,255,0.12) !important;
    color: white !important;
    border: 1px solid rgba(255,255,255,0.15) !important;
    border-radius: 12px !important;
}

[data-testid="stFileUploader"] button:hover {
    background: rgba(255,255,255,0.20) !important;
}

/* Answer choices */
[data-testid="stRadio"] label {
    font-family: 'Nunito', sans-serif !important;
    font-weight: 600 !important;
}

/* Streamlit icons */
.material-symbols-rounded,
.material-icons,
[data-testid="stSidebarCollapseButton"],
[data-testid="stSidebarCollapseButton"] * {
    font-family: "Material Symbols Rounded" !important;
}


# ==================================
#  QUIZFORGE SIDEBAR
#================================== 

[data-testid="stSidebar"] {
    background: linear-gradient(
        180deg,
        #1e1b4b 0%,
        #25204d 55%,
        #172033 100%
    ) !important;

    border-right: 1px solid rgba(192, 132, 252, 0.25);
}

/* Sidebar text */
[data-testid="stSidebar"] p,
[data-testid="stSidebar"] label,
[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3 {
    font-family: 'Nunito', sans-serif !important;
    color: #f5f3ff !important;
}

/* Sidebar headings */
[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3 {
    font-weight: 800 !important;
    color: #ddd6fe !important;
}

/* Sidebar logo */
[data-testid="stSidebar"] img {
    border-radius: 20px;
    width: 450px;
}

/* Sidebar dividers */
[data-testid="stSidebar"] hr {
    border-color: rgba(192, 132, 252, 0.3);
}

/* Sidebar heading */
[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3 {
    font-family: 'Pacifico', cursive !important;
    font-weight: 400 !important;
    color: #e9c5ff !important;
}

</style>
""", unsafe_allow_html=True)

# Upper-right doodle decoration

st.markdown(
    """
    <style>
    [data-testid="stAppViewContainer"] {
        background-image:
            url("data:image/png;base64,DOODLE_IMAGE"),
            linear-gradient(
                135deg,
                #0f172a 0%,
                #1e293b 50%,
                #334155 100%
            ) !important;

        background-repeat: no-repeat, no-repeat !important;
        background-position: right top, center !important;
        background-size: 850px auto, cover !important;
    }
    </style>
    """.replace("DOODLE_IMAGE", doodle_base64),
    unsafe_allow_html=True
)

# ==========================================
# QUIZFORGE SIDEBAR
# ==========================================

with st.sidebar:
    st.image(
        "src/mcqgenerator/assets/favicon.png",
        width=85
    )

    st.header("About QuizForge")

    st.write(
        "Upload a PDF and generate AI-powered quizzes instantly."
    )


# ==========================================
# QUIZFORGE TITLE
# ==========================================

st.markdown(
    '<h1 class="quizforge-title">QuizForge</h1>',
    unsafe_allow_html=True
)

st.markdown(
    "Transform PDFs into AI-generated quizzes in seconds."
)

st.write("")



# ==========================================
# PDF UPLOAD AND SETTINGS
# ==========================================

col1, col2 = st.columns(2)

with col1:
    uploaded_file = st.file_uploader(
        "Upload PDF",
        type=["pdf"]
    )

    difficulty = st.selectbox(
        "Difficulty",
        ["Easy", "Medium", "Hard"]
    )

with col2:
    num_questions = st.number_input(
        "Number of Questions",
        min_value=1,
        max_value=20,
        value=5
    )


# ==========================================
# GENERATE QUIZ
# ==========================================

if "quiz" not in st.session_state:
    st.session_state.quiz = None

if st.button("Generate Quiz"):

    if uploaded_file is None:
        st.error("Please upload a PDF first.")

    else:
        with st.spinner("Generating quiz..."):
            try:
                text = extract_text_from_pdf(uploaded_file)

                quiz = generate_quiz(
                    text,
                    num_questions,
                    difficulty=difficulty.lower()
                )

                st.session_state.quiz = quiz

            except Exception as e:
                st.session_state.quiz = None
                st.error(f"Quiz generation failed: {e}")


# ==========================================
# DISPLAY GENERATED QUIZ
# ==========================================

if st.session_state.quiz is not None:

    quiz = st.session_state.quiz

    st.subheader("Generated Quiz")

    for q_num, question in enumerate(
        quiz.questions, start=1
    ):

        with st.container(border=True):

            st.markdown(f"### Question {q_num}")

            st.write(question.question)

            selected_answer = st.radio(
            "Choose your answer:",
             options=list(question.options.keys()),
             format_func=lambda key: f"{key}. {question.options[key]}",
             index=None,
             key=f"question_{q_num}"
          )

            correct = question.correct_answer
            answer_text = question.options[correct]

            with st.expander("Show Answer"):

                st.success(
                    f"Correct Answer: {correct} — {answer_text}"
                )

                st.write(
                    f"**Explanation:** {question.explanation}"
                )

                if question.source_page is not None:
                    st.caption(
                        f"Source: Page {question.source_page}"
                    )

