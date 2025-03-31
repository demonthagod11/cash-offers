from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from app.database import get_db
from app.models import VirtualCard
from app.logger import logger

router = APIRouter()

class FundVirtualCard(BaseModel):
    cardholder_id: str
    amount: float

@router.post("/fund")
def fund_virtual_card(fund: FundVirtualCard, db: Session = Depends(get_db)):
    db_virtual_card = db.query(VirtualCard).filter(VirtualCard.cardholder_id == fund.cardholder_id).first()
    if not db_virtual_card:
        logger.error("Virtual card not found")
        raise HTTPException(status_code=404, detail="Virtual card not found")
    db_virtual_card.balance += fund.amount
    db.commit()
    db.refresh(db_virtual_card)
    logger.info(f"Virtual card funded: {db_virtual_card.cardholder_id}, Amount: {fund.amount}")
    return {"message": "Virtual card funded successfully", "virtual_card": db_virtual_card}