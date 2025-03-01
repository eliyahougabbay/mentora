# Test file for either runnig the agent directly or under a task

# -> Define what to test
# The CPU load, celery's limits, should we use celery or not. What's the role of celery? Why using a queue would help?

from src.celery_app import app
from src.agents.mentora import mentora_agent
from pydantic_ai.usage import Usage, UsageLimits


# restrict how many requests this app can make to the LLM
usage_limits = UsageLimits(request_limit=5)


async def mentora(query:str):
    usage = Usage()
    while True:
        result = await mentora_agent.run(query, usage=usage, usage_limits=usage_limits)
        quiz = result.data
        print(f'Quiz: {quiz}')


@app.task
def run_mentora(query:str):
    return mentora(query)


