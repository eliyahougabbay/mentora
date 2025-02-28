from src.celery_app import app
# from src.agents.mentora import MentoraAgent

@app.task
def run_mentora(query:str):
    # response: str = MentoraAgent.run_agent(query)
    print('hey')
    # return response


