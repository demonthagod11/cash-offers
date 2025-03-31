# Cash Offers LLC API

## Overview

Cash Offers LLC API is a production-ready API for processing cash payments, adding bank accounts, funding virtual cards, and handling payments and receiving.

## Features
- Accept cash payments.
- Add bank accounts with account and routing numbers.
- Fund virtual cards.
- Process payments and handle receiving payments.

## Prerequisites
- Python 3.8+
- SQLite database (or any preferred database)

## Setup Instructions

### Clone the Repository
```sh
git clone https://github.com/demonthagod11/cash-offers-llc.git
cd cash-offers-llc
```

### Install Dependencies
```sh
pip install -r requirements.txt
```

### Set Up Environment Variables
- Create a `.env` file and add the following environment variables:
```env
DATABASE_URL=sqlite:///./cashoffers.db
SECRET_KEY=your_secret_key_here
```

### Initialize Database
```sh
python -c "from app.database import Base, engine; Base.metadata.create_all(bind=engine)"
```

### Run the Application
```sh
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

## Directory Structure
```plaintext
cash-offers-llc/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── bank_account.py
│   ├── virtual_card.py
│   ├── payments.py
│   ├── receiving.py
│   ├── authentication.py
│   ├── models.py
│   ├── database.py
│   ├── logger.py
├── tests/
│   ├── __init__.py
│   ├── test_main.py
│   ├── test_bank_account.py
│   ├── test_virtual_card.py
│   ├── test_payments.py
│   ├── test_receiving.py
├── .env
├── .gitignore
├── README.md
├── requirements.txt
└── run.py
```

## API Endpoints

### Bank Account

#### Add Bank Account
- **Endpoint:** `/bank_account/add`
- **Method:** POST
- **Payload:**
```json
{
  "account_number": "123456789",
  "routing_number": "987654321",
  "account_type": "checking"
}
```
- **Response:**
```json
{
  "message": "Bank account added successfully",
  "bank_account": {
    "id": 1,
    "account_number": "123456789",
    "routing_number": "987654321",
    "account_type": "checking"
  }
}
```

### Virtual Card

#### Fund Virtual Card
- **Endpoint:** `/virtual_card/fund`
- **Method:** POST
- **Payload:**
```json
{
  "cardholder_id": "ch_123456789",
  "amount": 100.00
}
```
- **Response:**
```json
{
  "message": "Virtual card funded successfully",
  "virtual_card": {
    "id": 1,
    "cardholder_id": "ch_123456789",
    "balance": 100.00
  }
}
```

### Payments

#### Send Payment
- **Endpoint:** `/payments/send`
- **Method:** POST
- **Payload:**
```json
{
  "from_account": "123456789",
  "to_account": "987654321",
  "amount": 100.00,
  "currency": "usd",
  "description": "Payment for services"
}
```
- **Response:**
```json
{
  "message": "Payment sent successfully",
  "payment": {
    "id": 1,
    "from_account": "123456789",
    "to_account": "987654321",
    "amount": 100.00,
    "currency": "usd",
    "description": "Payment for services"
  }
}
```

### Receiving

#### Receive Payment
- **Endpoint:** `/receiving/receive`
- **Method:** POST
- **Payload:**
```json
{
  "from_account": "123456789",
  "to_account": "987654321",
  "amount": 100.00,
  "currency": "usd",
  "description": "Payment received"
}
```
- **Response:**
```json
{
  "message": "Payment received successfully",
  "payment": {
    "id": 1,
    "from_account": "123456789",
    "to_account": "987654321",
    "amount": 100.00,
    "currency": "