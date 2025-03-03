import os
from openai import AsyncAzureOpenAI
from pydantic import Field
from pydantic_ai import Agent, RunContext
from pydantic_ai.models.openai import OpenAIModel
from typing_extensions import TypedDict


# Retrieve environment variables
api_key = os.environ.get("AZURE_API_KEY")
azure_endpoint = os.environ.get("AZURE_ENDPOINT")
api_version = os.environ.get("AZURE_API_VERSION")
azure_model = os.environ.get("AZURE_MODEL_ID")

# Shared OpenAI client and model (configured once)
openai_client = AsyncAzureOpenAI(
    api_key=api_key,
    azure_endpoint=azure_endpoint,
    api_version=api_version,
)

openai_model = OpenAIModel(
    azure_model, openai_client=openai_client
)


MENTORA_AGENT_OLD= """
    You are a brillant mind and a genius teacher. You know the best way to explain things, to make them simple and clear. You are a master of your craft. You are a mentor.
    You want the user to learn at a fundamental level, to understand the basics and the core concepts.
    
    When asked for a course, you first detail a summary of core concepts to understand, with chapters and units.
    
    You then provide a very brief summary of the first unit of the first chapter.

    After that, you suggest the user to take a quiz to test their knowledge.

    Use the `quiz_factory` to provide a quiz to test the user's knowledge.
"""
 
MENTORA_AGENT= """
    You are a brillant mind and a genius teacher. You know the best way to explain things, to make them simple and clear. You are a master of your craft. You are a mentor.
    You want the user to learn at a fundamental level, to understand the basics and the core concepts.
    
    When asked for a course, you first detail a summary of core concepts to understand.

    After that, you suggest the user to take a quiz on the summary, to test their knowledge.

    Use the `quiz_factory` to provide a quiz to test the user's knowledge.
"""

SUMMARY_AGENT= """
    You are a brillant mind and a genius teacher. You know the best way to explain things, to make them simple and clear. You are a master of your craft. You are a mentor.

    Create a brief summary on the user subject.
"""

QUIZZ_AGENT= """
    You are a quiz master. You know how to create engaging and challenging quizzes that help people learn and remember things. You are a master of your craft.
    You elaborate a quiz of the text you receive. You Suggest 4 possible answers, where only one is correct answer.
"""

# Mentora Agent
mentora_agent = Agent(
    openai_model,
    system_prompt = MENTORA_AGENT,
)


# Summary Agent
# class CourseSummary(BaseModel):
#     summary: str = Field(description='The summary of the course')

# summary_agent = Agent(
#     openai_model,
#     result_type=CourseSummary,
#     system_prompt = SUMMARY_AGENT,
# )


# Quiz Agent
class QuizResult(TypedDict):  
    question: str = Field(description='The question to ask the user')
    answer: list[str] = Field(description="A list of possible answers")
    correct_answer: str = Field(description='The correct answer')

quiz_agent = Agent(
    openai_model,
    result_type=QuizResult,
    system_prompt=QUIZZ_AGENT,
 )


# # Mentora tools
# @mentora_agent.tool
# async def summary_factory(ctx: RunContext[None], course:str):
#     print(ctx)
#     r = await mentora_agent.run(course)
#     return r.data


# Quiz tool
@mentora_agent.tool
async def quiz_factory(ctx: RunContext[None], course:str):
    print(ctx)
    r = await quiz_agent.run(course)
    return r.data