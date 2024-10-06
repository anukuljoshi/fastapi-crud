from typing import Annotated, List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.crud import notes as notes_crud
from app.dependencies import get_db
from app.schemas import notes as notes_schema

router = APIRouter()


@router.post(
    "/notes",
    response_model=notes_schema.Note,
    status_code=status.HTTP_201_CREATED,
)
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


@router.get(
    "/notes",
    response_model=List[notes_schema.Note],
)
async def notes_list(
    db: Annotated[Session, Depends(get_db)]
):
    """handler to get a list of notes

    Args:
    ----
        db: db connection

    Returns:
    -------
        list of all notes
    """
    db_notes = notes_crud.list_notes(db)
    return db_notes
