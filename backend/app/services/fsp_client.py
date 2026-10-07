"""Клиент к API ФСП: результаты соревнований участника."""

import httpx

from app.config import settings
from app.services.rating import calc_elo


class FspClient:
    def __init__(self) -> None:
        self.http = httpx.AsyncClient(base_url=settings.fsp_api_url, timeout=15)

    async def fetch_results(self, email: str) -> list[dict]:
        response = await self.http.get("/participants/results", params={"email": email})
        return response.json()["results"]

    def rating_from_results(self, results: list[dict]) -> float:
        return calc_elo(results)
