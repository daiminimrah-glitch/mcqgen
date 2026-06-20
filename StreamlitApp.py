import streamlit as st
import json 

from src.mcqgenerator.utils import  (
    extract_text_from_pdf,
    generate_quiz
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Space Grotesk', sans-serif;
}
</style>
""", unsafe_allow_html=True)

st.set_page_config(
    page_title="QuizForge",
    page_icon="🧠",
    layout="wide"
)
with st.sidebar:
    st.header("🧠 About QuizForge")
    st.write(
        "Upload a PDF and generate AI-powered quizzes instantly."
    )

st.markdown("""
<style>

/* Main background */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(
        135deg,
        #0f172a 0%,
        #1e293b 50%,
        #334155 100%
    );
}

/* Main content area */
.main > div {
    background: rgba(255, 255, 255, 0.12);
    backdrop-filter: blur(15px);
    border: 1px solid rgba(255,255,255,0.15);
            }

/* Header */
[data-testid="stHeader"] {
    background: rgba(0,0,0,0);
}

/* Text colors */
h1, h2, h3, p, label {
    color: white !important;
}

/* Generate Quiz button */

    .stButton > button {
    background: linear-gradient(
        135deg,
        #22c55e,
        #16a34a
    ) !important;

    color: white !important;
    border: none !important;
    border-radius: 12px;
    font-weight: 600;
    padding: 0.6rem 1.5rem;
}
}

/* Hover */
    .stButton > button:hover {
    background: linear-gradient(
        135deg,
        #16a34a,
        #15803d
    ) !important;

    color: white !important;
}


/* Focus */
.stButton > button:focus {
    color: white !important;
}



/* Input boxes */
.stTextInput input,
.stNumberInput input {
    border-radius: 10px;
}

              /* Sidebar */
[data-testid="stSidebar"] {
    background: #1e293b;
}

/* Sidebar text */
[data-testid="stSidebar"] * {
    color: white !important;
}
            
/* Select box */
.stSelectbox {
    border-radius: 10px;
}

            /* File uploader */
[data-testid="stFileUploader"] {
    background: rgba(255,255,255,0.10);
    border: 1px solid rgba(255,255,255,0.15);
    border-radius: 15px;
    padding: 12px;
}
            /* File uploader button */
[data-testid="stFileUploader"] button {
    background: rgba(255,255,255,0.12) !important;
    color: white !important;
    border: 1px solid rgba(255,255,255,0.15) !important;
    border-radius: 12px !important;
}

/* Hover */
[data-testid="stFileUploader"] button:hover {
    background: rgba(255,255,255,0.20) !important;
    color: white !important;
}

/* Button text */
[data-testid="stFileUploader"] button * {
    color: white !important;
}

/* Uploaded file display */
[data-testid="stFileUploader"] section {
    background: rgba(255,255,255,0.12);
    border-radius: 12px;
}

/* File uploader text */
[data-testid="stFileUploader"] {
    color: white !important;
}

/* Drag and drop text */
[data-testid="stFileUploader"] label,
[data-testid="stFileUploader"] small,
[data-testid="stFileUploader"] span,
[data-testid="stFileUploader"] p {
    color: rgba(255,255,255,0.85) !important;
}     

/* Sidebar */
[data-testid="stSidebar"] {
    background: #1e293b;
}

/* Sidebar font */
[data-testid="stSidebar"] * {
    font-family: 'Space Grotesk', sans-serif !important;
}
            
</style>
""", unsafe_allow_html=True)

st.markdown(
    """
    <h1 style="
        font-family: 'Space Grotesk', sans-serif;
        font-size: 3rem;
        font-weight: 700;
        color: white;
        margin-bottom: 0;
    ">
        🧠 QuizForge
    </h1>
    """,
    unsafe_allow_html=True
)

st.markdown(
    "Transform PDFs into AI-generated quizzes in seconds."
)

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
    subject = st.text_input("Subject")

    num_questions = st.number_input(
        "Number of Questions",
        min_value=1,
        max_value=20,
        value=5
    )



if st.button("Generate Quiz"):

    if uploaded_file is None:
        st.error("Please upload a PDF first.")

    else:

        text = extract_text_from_pdf(uploaded_file)
        with st.spinner("Generating quiz..."):
         

           quiz = generate_quiz(
           text,
           num_questions,
           subject,
           difficulty
           )

           quiz = quiz.replace("```json", "")
           quiz = quiz.replace("```", "")
           quiz = json.loads(quiz)
           
        st.subheader("📚 Generated Quiz")
        for q_num, q_data in quiz.items():

            with st.container(border=True):

                st.markdown(f"### Question {q_num}")

                st.write(q_data["mcq"])

                for option_key, option_value in q_data["options"].items():
                    st.markdown(
                        f"**{option_key.upper()}.** {option_value}"
                    )

                correct = q_data["correct"]
                answer_text = q_data["options"][correct]

                with st.expander("✅ Show Answer"):
                    st.success(
                        f"Correct Answer: {correct.upper()} — {answer_text}"   
                    )    