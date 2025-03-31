from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from app.database import get_db
from app.models import BankAccount
from app.logger import logger

router = APIRouter()

class BankAccountCreate(BaseModel):
    account_number: str
    routing_number: str
    account_type: str

@router.post("/add")
def add_bank_account(bank_account: BankAccountCreate, db: Session = Depends(get_db)):
    db_bank_account = BankAccount(**bank_account.dict())
    try:
        db.add(db_bank_account)
        db.commit()
        db.refresh(db_bank_account)
        logger.info(f"Bank account added: {db_bank_account.account_number}")
        return {"message": "Bank account added successfully", "bank_account": db_bank_account}
    except Exception as e:
        logger.error(f"Failed to add bank account: {e}")
        raise HTTPException(status_code=500, detail="Failed to add bank account")