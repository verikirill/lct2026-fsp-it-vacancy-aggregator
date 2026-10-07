from app.services.rating import calc_elo


def test_first_place_raises_rating():
    results = [
        {"date": "2025-03-01", "place": 1, "participants": 40, "field_rating": 1300, "level": "всероссийский"}
    ]
    assert calc_elo(results) > 1200


def test_empty_history_keeps_base():
    assert calc_elo([]) == 1200
