"""Парсер вакансий hh.ru по профессиональным ролям ИТ."""

import httpx

from app.config import settings

IT_ROLES = [96, 104, 107, 112, 113, 114, 116, 121, 124, 125, 126]


def fetch_page(role: int, page: int) -> list[dict]:
    response = httpx.get(
        f"{settings.hh_api_url}/vacancies",
        params={"professional_role": role, "page": page, "per_page": 100},
        timeout=10,
    )
    response.raise_for_status()
    return response.json()["items"]

