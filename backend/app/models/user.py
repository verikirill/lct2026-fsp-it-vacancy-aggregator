from sqlalchemy import Column, Float, Integer, String
from sqlalchemy.orm import relationship

from app.db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String(255), unique=True, nullable=False)
    full_name = Column(String(255))
    city = Column(String(120))
    skills = Column(String(2000), default="")
    fsp_rating = Column(Float, default=1200.0)

    achievements = relationship("Achievement", back_populates="owner")
