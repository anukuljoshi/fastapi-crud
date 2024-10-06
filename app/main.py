from fastapi import FastAPI

app = FastAPI()


@app.get("/ping")
async def pong():
    """handler for ping check api"""
    return {"ping": "pong!"}
