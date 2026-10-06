from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db import get_db
from app.models import Vacancy
from app.schemas import VacancyOut

router = APIRouter()


@router.get("/", response_model=list[VacancyOut])
def list_vacancies(q: str = "", db: Session = Depends(get_db)):
    query = db.query(Vacancy)
    if q:
        query = query.filter(Vacancy.title.ilike(f"%{q}%"))
    return query.limit(50).all()

