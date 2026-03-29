from dotenv import load_dotenv
load_dotenv()

import asyncio
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai.types import Content, Part
from agent import root_agent

app = FastAPI(title="BullSpace AI")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

session_service = InMemorySessionService()
runner = Runner(
    agent=root_agent,
    app_name="bullspace_ai",
    session_service=session_service,
)

sessions = {}

class ChatRequest(BaseModel):
    student_id: str
    message: str

@app.get("/health")
def health():
    return {"status": "BullSpace AI is running", "university": "USF Tampa"}

@app.post("/chat")
async def chat(req: ChatRequest):
    try:
        if req.student_id not in sessions:
            session = await session_service.create_session(
                app_name="bullspace_ai",
                user_id=req.student_id,
            )
            sessions[req.student_id] = session.id

        message = Content(parts=[Part(text=req.message)])
        reply = ""

        async for event in runner.run_async(
            user_id=req.student_id,
            session_id=sessions[req.student_id],
            new_message=message,
        ):
            if event.is_final_response():
                reply = event.content.parts[0].text

        return {"response": reply, "student_id": req.student_id}

    
    except Exception as e:
        error_str = str(e)
        if "rate_limit" in error_str or "Rate limit" in error_str:
            return {"response": "I'm getting a lot of requests right now! Please wait 10 seconds and try again. 🐂", "student_id": req.student_id}
        return {"response": f"Sorry, I ran into an issue. Please try again in a moment!", "student_id": req.student_id}
    
    
@app.get("/")
def root():
    return FileResponse("index.html")