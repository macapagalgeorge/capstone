import streamlit as st
import pandas as pd

data = pd.read_csv("C:/Users/GlexCARD/Downloads/cpaatrainingmaterials/tips.csv")

st.write("Data Table")
st.table(data)