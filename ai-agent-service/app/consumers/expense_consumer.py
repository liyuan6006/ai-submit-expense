import json

from aiokafka import AIOKafkaConsumer

from app.config import (
    KAFKA_BOOTSTRAP_SERVERS
)

from app.agents.expense_agent import (
    analyze_expense
)

TOPIC = "expense-created"

async def consume():

    consumer = AIOKafkaConsumer(
        TOPIC,
        bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
        value_deserializer=lambda m:
            json.loads(
                m.decode("utf-8")
            )
    )

    await consumer.start()

    try:

        async for msg in consumer:

            expense = msg.value

            print(
                "Expense received:",
                expense
            )

            result = await analyze_expense(
                expense
            )

            print(
                "AI RESULT:"
            )

            print(result)

    finally:

        await consumer.stop()