from datetime import datetime

from pydantic import BaseModel


class NoteBase(BaseModel):
    """base class for Notes schema"""

    title: str
    description: str


class NoteCreate(NoteBase):
    """class for Notes create schema"""

    pass


class Note(NoteBase):
    """class for Notes detail schema"""

    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
