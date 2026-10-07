from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db import get_db
from app.models import User
from app.schemas import ProfileOut

router = APIRouter()


@router.get("/{user_id}", response_model=ProfileOut)
def get_profile(user_id: int, db: Session = Depends(get_db)):
    user = db.get(User, user_id)
    if user is None:
        raise HTTPException(404, "Пользователь не найден")
    return user

