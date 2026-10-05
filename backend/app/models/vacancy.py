from sqlalchemy import Column, DateTime, Integer, String, Text

from app.db import Base


class Vacancy(Base):
    __tablename__ = "vacancies"

    id = Column(Integer, primary_key=True)
    source = Column(String(50))  # hh, habr, superjob
    external_id = Column(String(100), index=True)
    title = Column(String(500))
    company = Column(String(500))
    city = Column(String(120))
    salary_from = Column(Integer)
    salary_to = Column(Integer)
    description = Column(Text)
    skills = Column(String(2000), default="")
    published_at = Column(DateTime)
