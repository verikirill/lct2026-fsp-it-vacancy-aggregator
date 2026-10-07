"""Рейтинг участника по местам в соревнованиях ФСП."""

LEVEL_WEIGHT = {"региональный": 1.0, "всероссийский": 1.6, "международный": 2.2}
BASE = 1200.0
K = 32


def calc_elo(results: list[dict]) -> float:
    rating = BASE
    for r in sorted(results, key=lambda x: x["date"]):
        expected = 1 / (1 + 10 ** ((r["field_rating"] - rating) / 400))
        score = max(0.0, 1 - (r["place"] - 1) / r["participants"])
        rating += K * (score - expected)
    return rating
