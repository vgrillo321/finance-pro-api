# app/db/models/account.py
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base import Base


class Account(Base):
    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)               # Ej: "Chase Checking"
    type = Column(String(50), nullable=False)                # Ej: "checking", "credit_card"
    institution = Column(String(100), nullable=True)         # Ej: "Chase", "Capital One"
    last4 = Column(String(4), nullable=True)                 # Últimos 4 dígitos
    currency = Column(String(10), default="USD", nullable=False)
    is_active = Column(Boolean, default=True)

    owner_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    # Relaciones
    owner = relationship("User", back_populates="accounts")
    transactions = relationship("Transaction", back_populates="account", cascade="all, delete-orphan")
