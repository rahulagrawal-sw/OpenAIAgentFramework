from fastapi import FastAPI
from dotenv import load_dotenv
import os

from .controller.RunController import router as run_router

app = FastAPI()
load_dotenv(override=True)

app.include_router(run_router)

@app.get("/")
def read_root():
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    return {"message": f"Hello, I am your FastAPI Application for AgenticAI - {OPENAI_API_KEY[:4]}"}
