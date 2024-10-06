from fastapi import FastAPI

from app.routers import notes, ping

app = FastAPI()

app.include_router(ping.router)
app.include_router(notes.router)
