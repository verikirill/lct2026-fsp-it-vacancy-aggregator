from celery import Celery

from app.config import settings
from app.db import SessionLocal
from app.models import Vacancy
from app.services.parser_hh import IT_ROLES, fetch_page, normalize

celery = Celery("talenthub", broker=settings.redis_url)
celery.conf.beat_schedule = {
    "parse-hh": {"task": "app.workers.tasks.parse_hh", "schedule": settings.parse_interval_minutes * 60},
}


@celery.task
def parse_hh() -> int:
    db = SessionLocal()
    saved = 0
    for role in IT_ROLES:
        for page in range(20):
            for item in fetch_page(role, page):
                db.merge(Vacancy(**normalize(item)))
                saved += 1
    db.commit()
    return saved
