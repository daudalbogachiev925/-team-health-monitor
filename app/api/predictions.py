from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.employee import Employee
from app.models.survey import Survey
from app.services.ml_model import model

router = APIRouter()

@router.get("/{employee_id}")
def predict(employee_id: int, db: Session = Depends(get_db)):
    emp = db.query(Employee).filter(Employee.id == employee_id).first()
    if not emp:
        raise HTTPException(404, "Employee not found")

    surveys = db.query(Survey).filter(Survey.employee_id == employee_id) \
               .order_by(Survey.submitted_at.desc()).limit(4).all()
    if not surveys:
        return {"employee_id": employee_id, "risk": 0.0, "reason": "no data"}

    avg = {
        "engagement": sum(s.engagement for s in surveys) / len(surveys),
        "burnout": sum(s.burnout for s in surveys) / len(surveys),
        "workload": sum(s.workload for s in surveys) / len(surveys),
        "conflicts": sum(s.conflicts for s in surveys) / len(surveys),
    }
    risk = model.predict(avg)
    emp.burnout_risk = risk
    db.commit()

    return {"employee_id": employee_id, "risk": risk, "features": avg}
