from app.db import Base
from sqlalchemy import Column, Integer, Text
from pydantic import BaseModel  # add this

class Meeting(Base):
    __tablename__ = "meetings"
    id = Column(Integer, primary_key=True, index=True)
    transcript = Column(Text)
    output = Column(Text)

# Add this Pydantic model for the request body
class MeetingInput(BaseModel):
    transcript: str