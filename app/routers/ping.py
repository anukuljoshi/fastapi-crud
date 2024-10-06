from fastapi import APIRouter

router = APIRouter()


@router.get("/ping")
async def pong():
    """handler for ping check api"""
    return {"ping": "pong!"}
