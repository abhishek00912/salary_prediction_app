import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import seaborn as sns

# =====================================
# LOAD MODEL + DATA
# =====================================
model = joblib.load("salary_model.pkl")  # trained in notebook

excel_file = "Employees.xlsx"

# ---- COLUMN NAMES (Change if required) ----
experience_col = "Years"
jobrole_col = "Department"
salary_col = "Annual Salary"
# -------------------------------------------

df = pd.read_excel(excel_file)
df = df[[experience_col, jobrole_col, salary_col]].dropna()

roles = sorted(df[jobrole_col].unique())


st.title("💼 Salary Prediction Web App")
st.write("This app predicts **salary using Experience + Job Role**, trained using your dataset.")





st.header("🔮 Predict Salary")

exp = st.number_input("Enter experience (in years)", min_value=0.0, max_value=40.0, step=0.5)

role = st.selectbox("Select job role", roles)

if st.button("Predict Salary"):
    inp = pd.DataFrame({
        experience_col: [exp],
        jobrole_col: [role]
    })
    pred = model.predict(inp)[0]
    st.success(f"Estimated Salary: ₹{pred:,.2f}")
