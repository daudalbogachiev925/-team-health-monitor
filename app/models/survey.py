from sqlalchemy import Column, Integer, ForeignKey, DateTime, Float
from sqlalchemy.sql import func
from app.database import Base

class Survey(Base):
    __tablename__ = "surveys"

    id = Column(Integer, primary_key=True)
    employee_id = Column(Integer, ForeignKey("employees.id"))
    engagement = Column(Float)
    burnout = Column(Float)
    workload = Column(Float)
    conflicts = Column(Float)
    submitted_at = Column(DateTime, server_default=func.now())
