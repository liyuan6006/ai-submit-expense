from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

from app.services.rag_service import (
    search_policy_context
)

from app.config import *

import os

from dotenv import load_dotenv
load_dotenv()

llm = ChatOpenAI(
    model="gpt-4.1-mini",
    api_key=os.getenv("OPENAI_API_KEY"),
    temperature=0
)

async def analyze_expense(
    expense
):

    question = f"""
    Expense Details:

    Merchant:
    {expense['merchant']}

    Amount:
    {expense['amount']}

    Category:
    {expense['category']}

    Analyze if this violates policy.
    """

    context = await search_policy_context(
        question
    )

    prompt = f"""
    You are an enterprise expense AI auditor.

    ONLY use the policy context.

    POLICY CONTEXT:
    {context}

    EXPENSE:
    {question}

    Determine:
    - compliant or not
    - reason
    - risk level
    """

    response = await llm.ainvoke(
        [
            HumanMessage(
                content=prompt
            )
        ]
    )

    return response.content