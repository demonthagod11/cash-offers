from fastapi import FastAPI
from app.bank_account import router as bank_account_router
from app.virtual_card import router as virtual_card_router
from app.payments import router as payments_router
from app.receiving import router as receiving_router

app = FastAPI()

app.include_router(bank_account_router, prefix="/bank_account", tags=["Bank Account"])
app.include_router(virtual_card_router, prefix="/virtual_card", tags=["Virtual Card"])
app.include_router(payments_router, prefix="/payments", tags=["Payments"])
app.include_router(receiving_router, prefix="/receiving", tags=["Receiving"])

@app.get("/")
def read_root():
    return {"message": "Welcome to Cash Offers API"}