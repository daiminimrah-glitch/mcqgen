
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

load_dotenv()

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.5,
    api_key=os.getenv("OPENAI_API_KEY")
)

with open("response.json", "r") as f:
    response_json = f.read()

quiz_template = """
Text:
{text}

You are an expert MCQ maker.
Given the above text, create {number} multiple choice questions
for {subject} students in a {tone} tone.

RESPONSE_JSON:
{response_json}
"""

quiz_prompt = ChatPromptTemplate.from_template(quiz_template)
quiz_chain = quiz_prompt | llm


def generate_quiz(text, num_questions, subject, difficulty):

    quiz_result = quiz_chain.invoke({
        "text": text,
        "number": num_questions,
        "subject": subject,
        "tone": difficulty,
        "response_json": response_json
    })

    return quiz_result.content

