from fastapi import APIRouter

from app.api import matching, profiles, vacancies

api_router = APIRouter()
api_router.include_router(vacancies.router, prefix="/vacancies", tags=["vacancies"])
api_router.include_router(profiles.router, prefix="/profiles", tags=["profiles"])
api_router.include_router(matching.router, prefix="/matching", tags=["matching"])
