from sqlalchemy import Column, Integer, String, DateTime, Float
from sqlalchemy.sql import func
from app.database import Base

class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    department = Column(String, index=True)
    manager_id = Column(Integer, nullable=True)
    hire_date = Column(DateTime, server_default=func.now())
    burnout_risk = Column(Float, default=0.0)
