import json

from langchain_openai import ChatOpenAI

from .plan import Plan

class Planner:
    """
    Creates a study plan based on the user's request.
    """

    def __init__(self):

        self.llm = ChatOpenAI(
            model="gpt-4.1-mini",
            temperature=0
        )

    
    def create_plan(self, user_request):

        """
        Create a study plan from the user's request.
        """
     