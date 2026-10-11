from sqlalchemy import Column, Date, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.db import Base


class Achievement(Base):
    __tablename__ = "achievements"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    title = Column(String(500))
    place = Column(Integer)
    level = Column(String(50))  # региональный, всероссийский, международный
    date = Column(Date)
    proof_url = Column(String(1000))

    owner = relationship("User", back_populates="achievements")
