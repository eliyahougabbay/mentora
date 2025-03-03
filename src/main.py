from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.tasks import run_mentora

app = FastAPI()

class MentoraRequest(BaseModel):
    query: str
    callback_url: str

@app.post("/mentora")
async def mentora_endpoint(request: MentoraRequest):
    try:
        task = run_mentora.delay(request.query, request.callback_url)
    except Exception as e:
        raise HTTPException(status_code=500, detail="Task submission failed")
    return {"task_id": task.id}