from fastapi import FastAPI
from app.routes.expense_routes import router
from app.services.kafka_service import (
    start_kafka,
    stop_kafka
)

app = FastAPI()

@app.on_event("startup")
async def startup_event():

    await start_kafka()

@app.on_event("shutdown")
async def shutdown_event():

    await stop_kafka()

app.include_router(router)