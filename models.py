from sqlalchemy import Column, Integer, String, Float
from app.database import Base

class BankAccount(Base):
    __tablename__ = "bank_accounts"

    id = Column(Integer, primary_key=True, index=True)
    account_number = Column(String, unique=True, index=True)
    routing_number = Column(String)
    account_type = Column(String)

class VirtualCard(Base):
    __tablename__ = "virtual_cards"

    id = Column(Integer, primary_key=True, index=True)
    cardholder_id = Column(String, unique=True, index=True)
    balance = Column(Float, default=0.0)

class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True)
    from_account = Column(String)
    to_account = Column(String)
    amount = Column(Float)
    currency = Column(String)
    description = Column(String)