"""Рекомендации вакансий: TF-IDF по навыкам плюс бонус за рейтинг ФСП."""

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from app.config import settings
from app.models import User, Vacancy
from app.services import rating

RATING_BONUS = 0.15


def match_vacancies(db, user_id: int) -> list[dict]:
    user = db.get(User, user_id)
    vacancies = db.query(Vacancy).all()
    corpus = [user.skills] + [v.skills + " " + v.title for v in vacancies]
    matrix = TfidfVectorizer().fit_transform(corpus)
    scores = cosine_similarity(matrix[0], matrix[1:])[0]
    bonus = rating.compute_elo_bonus(user.fsp_rating) * RATING_BONUS
    ranked = sorted(zip(vacancies, scores), key=lambda p: p[1] + bonus, reverse=True)
    return [
        {"vacancy_id": v.id, "title": v.title, "score": round(float(s) + bonus, 3)}
        for v, s in ranked[: settings.match_top_n]
    ]
