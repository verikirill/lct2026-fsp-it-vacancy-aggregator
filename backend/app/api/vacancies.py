from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db import get_db
from app.models import Vacancy
from app.schemas import VacancyOut

router = APIRouter()


@router.get("/", response_model=list[VacancyOut])
def list_vacancies(q: str = "", city: str | None = None, db: Session = Depends(get_db)):
    query = db.query(Vacancy)
    if q:
        query = query.filter(Vacancy.title.ilike(f"%{q}%"))
    if city:
        query = query.filter(Vacancy.city == city)
    return query.limit(50).all()


@router.get("/{vacancy_id}", response_model=VacancyOut)
def get_vacancy(vacancy_id: int, db: Session = Depends(get_db)):
    return db.get(Vacancy, vacancy_id)
