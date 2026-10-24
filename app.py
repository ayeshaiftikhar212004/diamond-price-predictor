import joblib
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Diamond Price Predictor", page_icon="💎")

@st.cache_resource
def load_model():
    return joblib.load("model.pkl")

model = load_model()

st.title("💎 Diamond Price Predictor")
st.caption("Machine Learning Fundamentals (AIC354), Assignment 3")

col1, col2 = st.columns(2)
with col1:
    carat = st.number_input("Carat", 0.2, 5.5, 0.9, step=0.01)
    cut = st.selectbox("Cut", ["Fair", "Good", "Very Good", "Premium", "Ideal"], index=4)
    color = st.selectbox("Color (D = best, J = worst)", list("DEFGHIJ"), index=3)
    clarity = st.selectbox("Clarity", ["I1", "SI2", "SI1", "VS2", "VS1", "VVS2", "VVS1", "IF"], index=3)
with col2:
    depth = st.number_input("Depth %", 43.0, 79.0, 61.8, step=0.1)
    table = st.number_input("Table %", 43.0, 95.0, 57.0, step=0.1)
    x = st.number_input("Length x (mm)", 0.1, 11.0, 6.2, step=0.01)
    y = st.number_input("Width y (mm)", 0.1, 12.0, 6.25, step=0.01)
    z = st.number_input("Depth z (mm)", 0.1, 8.0, 3.85, step=0.01)

if st.button("Predict price", type="primary"):
    row = pd.DataFrame([{
        "carat": carat, "cut": cut, "color": color, "clarity": clarity,
        "depth": depth, "table": table, "x": x, "y": y, "z": z,
    }])
    price = max(float(model.predict(row)[0]), 0)
    st.success(f"Estimated price: **${price:,.0f}**")