# 🤖 Meeting AI

A FastAPI-powered backend application that processes meeting transcripts using OpenAI GPT and extracts structured insights including summaries, decisions, action items, and risks.

## 🚀 Features

- **AI Meeting Processing** — Extracts summaries, decisions, action items, and risks from transcripts
- **JWT Authentication** — Secure login system protecting all endpoints
- **Database Storage** — All meetings saved to SQLite via SQLAlchemy
- **Simple Dashboard UI** — Clean frontend to submit transcripts and view history
- **Auto API Docs** — Swagger UI generated automatically by FastAPI

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| FastAPI | Web framework & API |
| OpenAI GPT | AI transcript processing |
| SQLAlchemy | Database ORM |
| SQLite | Database |
| python-jose | JWT token handling |
| passlib | Password hashing |
| Uvicorn | ASGI server |

## ⚙️ Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/Meeting-ai.git
cd Meeting-ai
```

### 2. Create virtual environment
```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Create `.env` file
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

### 5. Run the server
```bash
uvicorn app.main:app --reload
```

### 6. Open the app
- **Dashboard:** http://127.0.0.1:8000
- **API Docs:** http://127.0.0.1:8000/docs

## 🔐 Default Login Credentials

Username: admin
Password: password123

## 📡 API Endpoints

| Method | Endpoint | Auth Required | Description |
|---|---|---|---|
| POST | `/login` | ❌ | Get JWT token |
| POST | `/process-meeting` | ✅ | Process a transcript |
| GET | `/history` | ✅ | Get all past meetings |

## 📥 Example Request

```json
POST /process-meeting
{
  "transcript": "John will finish the API by May 10th. Team decided to delay launch to June. Risk: backend may not be ready in time."
}
```

## 📤 Example Response

```json
{
  "summary": "Team discussed API completion and launch timeline.",
  "decisions": ["Delay launch to June"],
  "action_items": [
    {
      "owner": "John",
      "task": "Finish the API",
      "deadline": "May 10th"
    }
  ],
  "risks": ["Backend may not be ready in time"]
}
```

## 📁 Project Structure
meeting.ai/
├── app/
│   ├── init.py
│   ├── auth.py        # JWT authentication
│   ├── config.py      # Environment variables
│   ├── db.py          # Database setup
│   ├── llm.py         # OpenAI integration
│   ├── main.py        # API routes
│   ├── models.py      # Data models
│   ├── processor.py   # Transcript processing
│   ├── utils.py       # Helper functions
│   └── static/
│       └── index.html # Frontend dashboard
├── .env               # API keys (not committed)
├── .gitignore
├── README.md
└── requirements.txt