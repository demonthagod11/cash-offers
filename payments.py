from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from app.database import get_db
from app.models import Payment, BankAccount, VirtualCard
from app.logger import logger

router = APIRouter()

class PaymentCreate(BaseModel):
    from_account: str
    to_account: str
    amount: float
    currency: str
    description: str

@router.post("/send")
def send_payment(payment: PaymentCreate, db: Session = Depends(get_db)):
    db_from_account = db.query(BankAccount).filter(BankAccount.account_number == payment.from_account).first()
    db_to_account = db.query(BankAccount).filter(BankAccount.account_number == payment.to_account).first()
    db_virtual_card = db.query(VirtualCard).filter(VirtualCard.cardholder_id == payment.to_account).first()
    
    if not db_from_account:
        logger.error("From account not found")
        raise HTTPException(status_code=404, detail="From account not found")
    if not (db_to_account or db_virtual_card):
        logger.error("To account not found")
        raise HTTPException(status_code=404, detail="To account not found")

    db_payment = Payment(**payment.dict())
    db.add(db_payment)
    db.commit()
    db.refresh(db_payment)
    logger.info(f"Payment sent from {payment.from_account} to {payment.to_account}, Amount: {payment.amount}")
    return {"message": "Payment sent successfully", "payment": db_payment}