from datetime import datetime

from pydantic import BaseModel


class VacancyOut(BaseModel):
    id: int
    title: str
    company: str
    city: str
    salary_from: int | None
    salary_to: int | None
    published_at: datetime

    class Config:
        orm_mode = True


class AchievementOut(BaseModel):
    title: str
    place: int
    level: str


class ProfileOut(BaseModel):
    id: int
    full_name: str
    city: str | None
    fsp_rating: float
    achievements: list[AchievementOut]

    class Config:
        orm_mode = True
