"""
Tools available to the QuizForge Study Agent.
"""


class QuizTool:
    """Generate quizzes from study material."""

    name = "quiz"

    description = (
        "Generate multiple-choice quiz questions from educational content."
    )


class SummaryTool:
    """Generate summaries from study material."""

    name = "summary"

    description = (
        "Generate concise summaries of educational content."
    )


class FlashcardTool:
    """Generate flashcards from study material."""

    name = "flashcards"

    description = (
        "Generate question-and-answer flashcards."
    )


class ExplainTool:
    """Explain concepts clearly."""

    name = "explain"

    description = (
        "Explain concepts in simple language."
    )