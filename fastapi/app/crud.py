from sqlalchemy.orm import Session
from app.models import User, UserProduct
from datetime import datetime

def create_user(db: Session, name: str, password: str, email: str):
    user = User(name=name, password=password, email=email, created_at=datetime.now())
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def create_user_product(db: Session, name: str, user_id: int):
    user_product = UserProduct(name=name, user_id=user_id, created_at=datetime.now())
    db.add(user_product)
    db.commit()
    db.refresh(user_product)
    return user_product

def get_user_products(db: Session, user_id: int):
    return db.query(UserProduct).filter(UserProduct.user_id == user_id).all()
