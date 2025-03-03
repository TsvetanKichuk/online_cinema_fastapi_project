from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from payments.models import Payment, PaymentStatus
from src.database.validators import get_postgresql_db  # Функция для подключения к базе данных

app = FastAPI()

@app.post("/payments/")
def create_payment(
    amount: float,
    currency: str = "USD",
    description: str = None,
    db: Session = Depends(get_postgresql_db),
):
    new_payment = Payment(
        amount=amount,
        currency=currency,
        description=description
    )
    db.add(new_payment)
    db.commit()
    db.refresh(new_payment)
    return new_payment


@app.get("/payments/{payment_id}")
def get_payment(payment_id: int, db: Session = Depends(get_postgresql_db)):
    payment = db.query(Payment).filter(Payment.id == payment_id).first()
    if not payment:
        raise HTTPException(status_code=404)
    return payment

