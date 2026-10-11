from fastapi import FastAPI
from app.api import employees, surveys, predictions
from app.database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Team Health Monitor", version="1.0.0")

app.include_router(employees.router, prefix="/api/employees", tags=["employees"])
app.include_router(surveys.router, prefix="/api/surveys", tags=["surveys"])
app.include_router(predictions.router, prefix="/api/predictions", tags=["predictions"])

@app.get("/health")
def health():
    return {"status": "ok"}
