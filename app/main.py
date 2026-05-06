from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.security import OAuth2PasswordRequestForm
from app.models import Meeting, MeetingInput
from app.processor import process_transcript
from app.auth import verify_password, create_token, get_current_user, FAKE_USERS
from app.db import Session
import json

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="app/static"), name="static")
@app.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = FAKE_USERS.get(form_data.username)
    if not user or not verify_password(form_data.password, user["password"]):
        raise HTTPException(status_code=401, detail="Wrong username or password")
    token = create_token({"sub": form_data.username})
    return {"access_token": token, "token_type": "bearer"}
@app.get("/")
def read_root():
    return FileResponse("app/static/index.html")

@app.post("/process-meeting")
def process_meeting(data: MeetingInput, current_user: str = Depends(get_current_user)):
    if len(data.transcript) > 20000:
        return {"error": "Transcript too long"}
    if "ignore previous" in data.transcript.lower():
        return {"error": "Invalid input"}
    
    result = process_transcript(data.transcript)
    db = Session()
    meeting = Meeting(
        transcript=data.transcript,
        output=json.dumps(result)
    )
    db.add(meeting)
    db.commit()
    return result

@app.get("/history")
def get_history(current_user: str = Depends(get_current_user)):
    db = Session()
    meetings = db.query(Meeting).all()
    return [
        {
            "id": m.id,
            "transcript": m.transcript,
            "output": json.loads(m.output)
        }
        for m in meetings
    ]