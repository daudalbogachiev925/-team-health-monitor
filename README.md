# team-health-monitor

Платформа мониторинга здоровья команд: опросы вовлечённости, ML-прогноз риска ухода, алерты HR.

## Возможности
- Еженедельные пульс-опросы сотрудников (web + Telegram)
- ML-модель прогноза выгорания (RandomForest + SHAP)
- Дашборд для HR и руководителей
- Автоматические алерты в Slack/Telegram
- REST API для интеграции с HRIS

## Архитектура
FastAPI backend + Streamlit dashboard + PostgreSQL + Redis (очереди) + Docker.

## Быстрый старт

git clone https://github.com/your-org/team-health-monitor.git
cd team-health-monitor
cp .env.example .env
docker-compose up --build

API: http://localhost:8000/docs
Dashboard: http://localhost:8501

## Установка без Docker

pip install -r requirements.txt
alembic upgrade head
uvicorn app.main:app --reload
streamlit run dashboard/streamlit_app.py

## Обучение модели

python -m app.ml.train --data data/surveys.csv --out app/ml/model.pkl

## Тесты

pytest tests/ -v

## API

| Метод | Endpoint | Описание |
|-------|----------|----------|
| POST | /api/employees | создать сотрудника |
| POST | /api/surveys | отправить опрос |
| GET | /api/predictions/{employee_id} | прогноз риска |
| GET | /api/dashboard/summary | сводка по командам |

## Лицензия
MIT
