import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import pandas as pd
import plotly.express as px

sns.set()
data = pd.read_csv("C:/Users/GlexCARD/Downloads/cpaatrainingmaterials/CAPSTONEDATA.csv")

data["PROJDATE"] = pd.to_datetime(data["PROJDATE"])
data["YEAR-MONTH"] = data["PROJDATE"].dt.to_period("M").astype(str)
monthly_sales = data.groupby("YEAR-MONTH")["GROSSSALES"].sum().reset_index()
st.line_chart(monthly_sales.set_index("YEAR-MONTH"))

st.divider()
st.bar_chart(data, x = "COUNTRY", y = "GROSSSALES")

st.divider()
total_sales = data.groupby("COUNTRY")["GROSSSALES"].sum().reset_index()
fig = px.pie(total_sales, values="GROSSSALES", names="COUNTRY", title = "SALES DISTRIBUTION PER COUNTRY")
st.plotly_chart(fig)
