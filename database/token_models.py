from sqlalchemy import Column, String, Integer, DateTime
from models.database import Base
from datetime import datetime

class OAuthToken(Base):
    __tablename__ = "oauth_tokens"

    id = Column(Integer, primary_key=True, index=True)
    platform = Column(String, index=True)  # เช่น "lazada", "shopee"
    access_token = Column(String)
    refresh_token = Column(String, nullable=True)
    expires_in = Column(Integer)
    created_at = Column(DateTime, default=datetime.utcnow)
