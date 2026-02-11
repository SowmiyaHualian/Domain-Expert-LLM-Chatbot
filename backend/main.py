import os
import uuid
import requests

from fastapi import FastAPI, HTTPException, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv

from backend.prompt import SYSTEM_PROMPT

load_dotenv(dotenv_path="backend/.env")

LLM_API_KEY = os.getenv("LLM_API_KEY")
LLM_API_URL = os.getenv("LLM_API_URL")

app = FastAPI(title="Domain Expert LLM Chatbot")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

sessions = {}

class ChatRequest(BaseModel):
    question: str


class ChatResponse(BaseModel):
    answer: str


@app.get("/")
def health_check():
    return {"status": "Domain Expert LLM Chatbot is running"}

@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest, req: Request, res: Response):

    if not LLM_API_KEY or not LLM_API_URL:
        raise HTTPException(
            status_code=500,
            detail="LLM API not configured."
        )

    session_id = req.cookies.get("session_id")

    if not session_id:
        session_id = str(uuid.uuid4())
        sessions[session_id] = []
        res.set_cookie(key="session_id", value=session_id)

    if session_id not in sessions:
        sessions[session_id] = []

    conversation_history = sessions[session_id]

    # Add user message
    conversation_history.append({
        "role": "user",
        "content": request.question
    })

    # Keep last 10 exchanges only (limit memory)
    trimmed_history = conversation_history[-10:]

    payload = {
        "model": "llama-3.1-8b-instant",
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            *trimmed_history
        ],
        "temperature": 0.3,
    }

    headers = {
        "Authorization": f"Bearer {LLM_API_KEY}",
        "Content-Type": "application/json",
    }

    try:
        response = requests.post(
            LLM_API_URL,
            headers=headers,
            json=payload,
            timeout=30,
        )
    except requests.RequestException as e:
        raise HTTPException(
            status_code=500,
            detail=f"LLM connection failed: {str(e)}"
        )

    if response.status_code != 200:
        raise HTTPException(
            status_code=response.status_code,
            detail=response.text
        )

    data = response.json()
    answer = data["choices"][0]["message"]["content"]

    # Add assistant reply to history
    conversation_history.append({
        "role": "assistant",
        "content": answer
    })

    return ChatResponse(answer=answer)
