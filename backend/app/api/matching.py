from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db import get_db
from app.services.matching import match_vacancies

router = APIRouter()


@router.get("/{user_id}")
def recommendations(user_id: int, db: Session = Depends(get_db)):
    return match_vacancies(db, user_id)
