import json
from app.llm import call_llm


def process_transcript(text: str):
    raw_output = call_llm(text)

    try:
        return json.loads(raw_output)
    except json.JSONDecodeError:
        return {
            "summary": "",
            "decisions": [],
            "action_items": [],
            "risks": []
        }
