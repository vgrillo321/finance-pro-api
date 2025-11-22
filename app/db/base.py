# app/db/base.py
from sqlalchemy.orm import declarative_base

Base = declarative_base()

# importa TODOS los modelos para que se registren
# from app.db.models.user import User
# from app.db.models.account import Account
# from app.db.models.category import Category
# from app.db.models.transaction import Transaction

# __all__ = ["User", "Account", "Category", "Transaction"]