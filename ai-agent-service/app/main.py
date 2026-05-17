import asyncio

from fastapi import FastAPI

from app.consumers.expense_consumer import (
    consume
)

app = FastAPI()

@app.on_event("startup")
async def startup_event():

    asyncio.create_task(
        consume()
    )

@app.get("/")
async def root():

    return {
        "message":
        "AI Agent Running"
    }