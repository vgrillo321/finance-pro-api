# app/db/models/category.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base import Base


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False, unique=True)  # Ej: "Groceries", "Rent"
    type = Column(String(50), nullable=False)                # "income", "expense", "transfer"

    parent_id = Column(Integer, ForeignKey("categories.id"), nullable=True)

    # Relaciones
    parent = relationship("Category", remote_side=[id], backref="children")
    transactions = relationship("Transaction", back_populates="category")
