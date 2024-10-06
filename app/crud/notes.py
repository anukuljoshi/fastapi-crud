from sqlalchemy.orm import Session

from app.models import notes
from app.schemas.notes import NoteCreate


def create_note(db: Session, note: NoteCreate):
    """helper function to create a note using NoteCreate schema

    Args:
    ----
        db: db connection
        note: pydantic schema for NoteCreate

    Returns:
    -------
        Notes instance of created note
    """
    db_note = notes.Notes(title=note.title, description=note.description)
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note


def list_notes(db: Session):
    """helper function to create a note using NoteCreate schema

    Args:
    ----
        db: db connection

    Returns:
    -------
        List of Notes
    """
    db_notes = db.query(notes.Notes).all()
    return db_notes
