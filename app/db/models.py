from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime

from app.db.database import Base

class API(Base):
    """API model for database"""
    __tablename__ = "apis"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True, nullable=False)
    description = Column(Text)
    url = Column(String(512), unique=True, index=True, nullable=False)
    category = Column(String(100), index=True)
    source = Column(String(100))
    created_at = Column(DateTime, default=datetime.now)
    last_updated = Column(DateTime, default=datetime.now)
    
    def to_dict(self):
        """Convert model to dictionary"""
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "url": self.url,
            "category": self.category,
            "source": self.source,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "last_updated": self.last_updated.isoformat() if self.last_updated else None
        }