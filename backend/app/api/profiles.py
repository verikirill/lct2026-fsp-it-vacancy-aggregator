from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db import get_db
from app.models import User
from app.schemas import ProfileOut
from app.services.fsp_client import FspClient

router = APIRouter()


@router.get("/{user_id}", response_model=ProfileOut)
def get_profile(user_id: int, db: Session = Depends(get_db)):
    user = db.get(User, user_id)
    if user is None:
        raise HTTPException(404, "Пользователь не найден")
    return user


@router.post("/{user_id}/sync-fsp")
async def sync_fsp(user_id: int, db: Session = Depends(get_db)):
    user = db.get(User, user_id)
    client = FspClient()
    results = await client.fetch_results(user.email)
    user.fsp_rating = client.rating_from_results(results)
    db.commit()
    return {"rating": user.fsp_rating, "results": len(results)}
