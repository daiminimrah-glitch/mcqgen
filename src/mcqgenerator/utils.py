"""
utils.py

- extract_text_from_pdf(): Extracts text from an uploaded PDF.
- generate_quiz(): Sends the extracted text and quiz settings to the LLM.
- QuizConfig: Validates quiz settings before the LLM call.
- GeneratedQuiz: Validates the structure of the LLM-generated quiz.
- Returns the validated quiz to Streamlit for display.

"""

import json
from .quiz_schema import QuizConfig, GeneratedQuiz
from pypdf import PdfReader

def extract_text_from_pdf(uploaded_file):
    pdf_reader = PdfReader(uploaded_file)

    text = ""

    for page in pdf_reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text

    return text

import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv(override=True)


llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.5,
    api_key=os.getenv("OPENAI_API_KEY")
)

with open("response.json", "r") as f:
    response_json = f.read()

quiz_template = """
You are an expert educational quiz generator.

Generate exactly {number} multiple-choice questions
based ONLY on the PDF content below.

Difficulty: {tone}

PDF Content:
{text}

Requirements:
- Each question must have four options: A, B, C, D.
- Exactly one option must be correct.
- Include an explanation for each correct answer.
- Do not introduce information outside the PDF.
- Set source_page to null.
- Return valid JSON only, without Markdown formatting.
- Follow this JSON structure:

{response_json}
"""

quiz_prompt = ChatPromptTemplate.from_template(quiz_template)
quiz_chain = quiz_prompt | llm


def generate_quiz(text, num_questions, difficulty, subject="General"):

    # Validate quiz settings before calling the LLM
    config = QuizConfig(
        num_questions=num_questions,
        subject=subject,
        difficulty=difficulty.lower()
    )

    # Ask the LLM to generate a quiz
    quiz_result = quiz_chain.invoke({
        "text": text,
        "number": config.num_questions,
        "subject": config.subject,
        "tone": config.difficulty,
        "response_json": response_json
    })

    # Remove Markdown code fences if the LLM includes them
    quiz_text = quiz_result.content.strip()

    if quiz_text.startswith("```json"):
        quiz_text = quiz_text[7:]
    elif quiz_text.startswith("```"):
        quiz_text = quiz_text[3:]

    if quiz_text.endswith("```"):
        quiz_text = quiz_text[:-3]

    # Convert the JSON string into a Python dictionary
    quiz_data = json.loads(quiz_text.strip())

    # Validate the complete generated quiz
    validated_quiz = GeneratedQuiz.model_validate(quiz_data)

    return validated_quiz

