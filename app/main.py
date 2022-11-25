from fastapi import FastAPI, Depends, status

from app.foo import Settings, get_settings

app = FastAPI()


@app.get("/ping", status_code=status.HTTP_200_OK)
def pong(settings: Settings = Depends(get_settings)):
    return {
        "ping": "pong!",
        "environment": settings.environment,
        "testing": settings.testing
        }
