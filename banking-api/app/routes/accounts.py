from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Account, Transaction
from app.schemas import AccountCreate

from app.schemas import (
    DepositRequest,
    WithdrawRequest,
    TransferRequest
)
from decimal import Decimal
from app.metrics import (
    accounts_created,
    deposits_total,
    withdrawals_total,
    transfers_total
)

router = APIRouter(
    prefix="/accounts",
    tags=["Accounts"]
)


@router.post("/")
def create_account(
    account: AccountCreate,
    db: Session = Depends(get_db)
):
    new_account = Account(
        account_number=account.account_number,
        customer_name=account.customer_name
    )

    db.add(new_account)
    db.commit()
    db.refresh(new_account)

    accounts_created.inc()

    return new_account


@router.get("/")
def get_accounts(
    db: Session = Depends(get_db)
):
    return db.query(Account).all()

from fastapi import HTTPException
from uuid import UUID


@router.get("/{account_id}")
def get_account(
    account_id: UUID,
    db: Session = Depends(get_db)
):
    account = (
        db.query(Account)
        .filter(Account.account_id == account_id)
        .first()
    )

    if not account:
        raise HTTPException(
            status_code=404,
            detail="Account not found"
        )

    return account

@router.post("/deposit")
def deposit(
    request: DepositRequest,
    db: Session = Depends(get_db)
):
    account = (
        db.query(Account)
        .filter(Account.account_id == request.account_id)
        .first()
    )

    if not account:
        raise HTTPException(
            status_code=404,
            detail="Account not found"
        )

    account.balance += Decimal(str(request.amount))
    transaction = Transaction(
        account_id=account.account_id,
        transaction_type="DEPOSIT",
        amount=Decimal(str(request.amount)),
        status="SUCCESS"

    )

    db.add(transaction)


    db.commit()
    db.refresh(account)
    deposits_total.inc()

    return {
        "message": "Deposit successful",
        "new_balance": account.balance
    }

@router.post("/withdraw")
def withdraw(
    request: WithdrawRequest,
    db: Session = Depends(get_db)
):
    account = (
        db.query(Account)
        .filter(Account.account_id == request.account_id)
        .first()
    )

    if not account:
        raise HTTPException(
            status_code=404,
            detail="Account not found"
        )

    if account.balance < Decimal(str(request.amount)):
        raise HTTPException(
            status_code=400,
            detail="Insufficient balance"
        )

    account.balance -= Decimal(str(request.amount))
    transaction = Transaction(
        account_id=account.account_id,
        transaction_type="WITHDRAW",
        amount=Decimal(str(request.amount)),
        status="SUCCESS"
    
    )

    db.add(transaction)

    db.commit()
    db.refresh(account)
    withdrawals_total.inc()

    return {
        "message": "Withdrawal successful",
        "new_balance": account.balance
    }

@router.post("/transfer")
def transfer(
    request: TransferRequest,
    db: Session = Depends(get_db)
):
    from_account = (
        db.query(Account)
        .filter(Account.account_id == request.from_account_id)
        .first()
    )

    to_account = (
        db.query(Account)
        .filter(Account.account_id == request.to_account_id)
        .first()
    )

    if not from_account:
        raise HTTPException(
            status_code=404,
            detail="Source account not found"
        )

    if not to_account:
        raise HTTPException(
            status_code=404,
            detail="Destination account not found"
        )

    amount = Decimal(str(request.amount))

    if from_account.balance < amount:
        raise HTTPException(
            status_code=400,
            detail="Insufficient balance"
        )

    from_account.balance -= amount
    to_account.balance += amount

    transaction = Transaction(
        account_id=from_account.account_id,
        transaction_type="TRANSFER",
        amount=amount,
        status="SUCCESS"
    )

    db.add(transaction)

    db.commit()
    transfers_total.inc()
    return {
        "message": "Transfer successful"
    }