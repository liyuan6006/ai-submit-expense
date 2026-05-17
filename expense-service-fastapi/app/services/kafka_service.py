from aiokafka import AIOKafkaProducer
import json

producer = None

async def start_kafka():

    global producer

    producer = AIOKafkaProducer(
        bootstrap_servers='localhost:9092'
    )

    await producer.start()

async def stop_kafka():

    await producer.stop()

async def publish_expense_created(
    expense
):

    await producer.send_and_wait(
        "expense-created",
        json.dumps(expense).encode()
    )