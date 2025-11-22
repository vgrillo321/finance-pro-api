from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.db.models.transaction import Transaction  # ajusta path si es distinto

router = APIRouter()

@router.get("/transactions")
def get_transactions(db: Session = Depends(get_db)):
    transactions = db.query(Transaction).all()
    return transactions
