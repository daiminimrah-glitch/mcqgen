import streamlit as st

from src.mcqgenerator.utils import  (
    extract_text_from_pdf,
    generate_quiz
)

st.title("MCQ Generator")

uploaded_file = st.file_uploader(
    "Upload PDF",
    type=["pdf"]
)

subject = st.text_input("Subject")

num_questions = st.number_input(
    "Number of Questions",
    min_value=1,
    max_value=20,
    value=5
)

difficulty = st.selectbox(
    "Difficulty",
    ["Easy", "Medium", "Hard"]
)

if st.button("Generate Quiz"):

    if uploaded_file is None:
        st.error("Please upload a PDF first.")

    else:

        text = extract_text_from_pdf(uploaded_file)

        quiz = generate_quiz(
            text,
            num_questions,
            subject,
            difficulty
        )

        st.subheader("Generated Quiz")
        st.write(quiz)