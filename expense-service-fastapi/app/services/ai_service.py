import os

from dotenv import load_dotenv
load_dotenv()

from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

async def categorize_expense(
    merchant,
    amount
):

    prompt = f"""
    Categorize this expense.

    Merchant: {merchant}
    Amount: {amount}

    Categories:
    Travel
    Food
    Software
    Entertainment
    Office
    FraudRisk

    Return ONLY category.
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0
    )

    return response.choices[0].message.content