from pydantic import BaseModel

class ExpenseRequest(BaseModel):

    employee_id: str

    merchant: str

    amount: float