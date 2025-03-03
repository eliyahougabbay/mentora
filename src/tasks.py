import asyncio
import requests
from src.celery_app import app
from src.agents.mentora import mentora_agent
from pydantic_ai.usage import Usage, UsageLimits


# Limit the number of requests to the LLM
usage_limits = UsageLimits(request_limit=5)


async def mentora(query:str):
    usage = Usage()
    # Run the agent once and retrieve the result data
    result = await mentora_agent.run(query, usage=usage, usage_limits=usage_limits)
    return result.data


@app.task
def run_mentora(query: str, callback_url: str):
    # Run the asynchronous mentora function
    result_data = asyncio.run(mentora(query))
    
    # Notify the provided webhook with the result
    try:
        requests.post(callback_url, json={"result": result_data})
    except Exception as e:
        print("Error notifying webhook:", e)
    
    return result_data