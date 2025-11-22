# app/db/models/__init__.py
# Esto solo hace que el folder sea un paquete de Python

from app.db.base import Base  # opcional, pero útil para Alembic etc.

from .user import User
from .account import Account
from .category import Category
from .transaction import Transaction

__all__ = ["User", "Account", "Category", "Transaction", "Base"]