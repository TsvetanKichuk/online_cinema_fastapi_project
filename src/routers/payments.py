from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from src.database.models.payments import Payment
from src.database.database import get_db

app = FastAPI()

@app.post("/payments/")
def create_payment(
    amount: float,
    currency: str = "USD",
    description: str = None,
    db: Session = Depends(get_db),
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
def get_payment(payment_id: int, db: Session = Depends(get_db)):
    payment = db.query(Payment).filter(Payment.id == payment_id).first()
    if not payment:
        raise HTTPException(status_code=404)
    return payment