from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.crud import notes as notes_crud
from app.dependencies import get_db
from app.schemas import notes as notes_schema

router = APIRouter()


@router.post("/notes", response_model=notes_schema.Note)
async def notes_create(
    note: notes_schema.NoteCreate, db: Annotated[Session, Depends(get_db)]
):
    """handler to create a note

    Args:
    ----
        note: request data to create note
        db: db connection

    Returns:
    -------
        details of the created note
    """
    db_note = notes_crud.create_note(db, note)
    return db_note
