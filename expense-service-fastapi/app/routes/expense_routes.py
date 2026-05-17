from fastapi import APIRouter
from app.schemas.expense_schema import ExpenseRequest
from app.services.ai_service import categorize_expense
from app.services.kafka_service import publish_expense_created

router = APIRouter()

@router.post("/submit-expense")
async def submit_expense(
    request: ExpenseRequest
):

    category = await categorize_expense(
        request.merchant,
        request.amount
    )

    expense = {
        "employee_id": request.employee_id,
        "merchant": request.merchant,
        "amount": request.amount,
        "category": category
    }

    await publish_expense_created(
        expense
    )

    return {
        "message": "Expense submitted",
        "expense": expense
    }