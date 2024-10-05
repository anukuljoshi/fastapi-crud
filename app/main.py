from fastapi import FastAPI

app = FastAPI()


@app.get("/ping")
def pong():
    """handler for ping check api"""
    return {"ping": "pong!"}
