"""
quiz_schema.py

- QuizConfig: Checks quiz settings before sending them to the LLM.
- GeneratedQuestionSchema: Checks each question returned by the LLM.
- GeneratedQuiz: Checks the complete quiz returned by the LLM.

Pydantic checks data structure and format, NOT factual correctness.
Validation happens when these classes are used, not just defined.
"""
from pydantic import BaseModel, Field
from typing import Literal


class QuizConfig(BaseModel):
    num_questions: int = Field(default=5, ge=1, le=30)
    subject: str
    difficulty: Literal["easy", "medium", "hard"] = "medium"


class GeneratedQuestionSchema(BaseModel):
    question: str
    options: dict[Literal["A", "B", "C", "D"], str]
    correct_answer: Literal["A", "B", "C", "D"]
    explanation: str
    source_page: int | None = Field(default=None, ge=1)


class GeneratedQuiz(BaseModel):
    questions: list[GeneratedQuestionSchema]