from pydantic import BaseModel
from uuid import UUID


class AccountCreate(BaseModel):
    account_number: str
    customer_name: str


class AccountResponse(BaseModel):
    account_id: UUID
    account_number: str
    customer_name: str
    balance: float
    status: str

    class Config:
        from_attributes = True

    
class DepositRequest(BaseModel):
    account_id: UUID
    amount: float


class WithdrawRequest(BaseModel):
    account_id: UUID
    amount: float

class TransferRequest(BaseModel):
    from_account_id: UUID
    to_account_id: UUID
    amount: float