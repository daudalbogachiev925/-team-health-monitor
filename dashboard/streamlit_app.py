import streamlit as st
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine
import os

st.set_page_config(page_title="Team Health", layout="wide")
st.title("Team Health Monitor")

engine = create_engine(os.getenv("DATABASE_URL", "postgresql://user:pass@db:5432/health"))

@st.cache_data(ttl=60)
def load_employees():
    return pd.read_sql("SELECT * FROM employees", engine)

@st.cache_data(ttl=60)
def load_surveys():
    return pd.read_sql("SELECT * FROM surveys", engine)

emp = load_employees()
surveys = load_surveys()

col1, col2, col3, col4 = st.columns(4)
col1.metric("Сотрудников", len(emp))
col2.metric("Средний риск", f"{emp.burnout_risk.mean():.2f}")
col3.metric("Опросов", len(surveys))
col4.metric("Высокий риск", (emp.burnout_risk > 0.7).sum())

st.subheader("Риск выгорания по отделам")
agg = emp.groupby("department").burnout_risk.mean().reset_index()
st.plotly_chart(px.bar(agg, x="department", y="burnout_risk"))

st.subheader("Топ сотрудников в зоне риска")
st.dataframe(emp.nlargest(10, "burnout_risk")[["name","department","burnout_risk"]])
