
import streamlit as st
import numpy as np
import joblib

# Load model and scaler
model = joblib.load("xgboost_salary_model.pkl")
scaler = joblib.load("salary_scaler.pkl")

st.set_page_config(page_title="Employee Salary Predictor", layout="centered")
st.title("💼 ⚡⚡Employee Salary Predictor by Sadvik ⚡⚡")
st.write("Use this app to predict whether an employee earns >50K or <=50K based on input data.")

# Input fields
age = st.slider("Age", 18, 75, 30)
fnlwgt = st.number_input("Final Weight (fnlwgt)", min_value=10000, max_value=500000, value=200000)
educational_num = st.slider("Education Level (educational-num)", 1, 16, 10)
hours_per_week = st.slider("Hours per week", 1, 100, 40)
capital_gain = st.number_input("Capital Gain", 0, 100000, 0)
capital_loss = st.number_input("Capital Loss", 0, 100000, 0)

# Encoded categorical values
workclass_map = {
    "?": 0, "Federal-gov": 1, "Local-gov": 2, "Never-worked": 3,
    "Private": 4, "Self-emp-inc": 5, "Self-emp-not-inc": 6,
    "State-gov": 7, "Without-pay": 8
}
workclass_input = st.selectbox("Workclass", list(workclass_map.keys()))
workclass = workclass_map[workclass_input]
marital_map = {
    "Divorced": 0, "Married-AF-spouse": 1, "Married-civ-spouse": 2,
    "Married-spouse-absent": 3, "Never-married": 4, "Separated": 5,
    "Widowed": 6
}
marital_input = st.selectbox("Marital Status", list(marital_map.keys()))
marital_status = marital_map[marital_input]
occupation_map = {
    "?": 0, "Adm-clerical": 1, "Armed-Forces": 2, "Craft-repair": 3,
    "Exec-managerial": 4, "Farming-fishing": 5, "Handlers-cleaners": 6,
    "Machine-op-inspct": 7, "Other-service": 8, "Priv-house-serv": 9,
    "Prof-specialty": 10, "Protective-serv": 11, "Sales": 12,
    "Tech-support": 13, "Transport-moving": 14
}
occupation_input = st.selectbox("Occupation", list(occupation_map.keys()))
occupation = occupation_map[occupation_input]
relationship_map = {
    "Husband": 0, "Not-in-family": 1, "Other-relative": 2,
    "Own-child": 3, "Unmarried": 4, "Wife": 5
}
relationship_input = st.selectbox("Relationship", list(relationship_map.keys()))
relationship = relationship_map[relationship_input]
race_map = {
    "Amer-Indian-Eskimo": 0, "Asian-Pac-Islander": 1,
    "Black": 2, "Other": 3, "White": 4
}
race_input = st.selectbox("Race", list(race_map.keys()))
race = race_map[race_input]
gender_map = {
    "Female": 0, "Male": 1
}
gender_input = st.selectbox("Gender", list(gender_map.keys()))
gender = gender_map[gender_input]
native_country_map = {
    "?": 0, "Cambodia": 1, "Canada": 2, "China": 3, "Columbia": 4,
    "Cuba": 5, "Dominican-Republic": 6, "Ecuador": 7, "El-Salvador": 8,
    "England": 9, "France": 10, "Germany": 11, "Greece": 12,
    "Guatemala": 13, "Haiti": 14, "Holand-Netherlands": 15,
    "Honduras": 16, "Hong": 17, "Hungary": 18, "India": 19,
    "Iran": 20, "Ireland": 21, "Italy": 22, "Jamaica": 23,
    "Japan": 24, "Laos": 25, "Mexico": 26, "Nicaragua": 27,
    "Outlying-US(Guam-USVI-etc)": 28, "Peru": 29, "Philippines": 30,
    "Poland": 31, "Portugal": 32, "Puerto-Rico": 33, "Scotland": 34,
    "South": 35, "Taiwan": 36, "Thailand": 37, "Trinadad&Tobago": 38,
    "United-States": 39, "Vietnam": 40, "Yugoslavia": 41
}
native_input = st.selectbox("Native Country", list(native_country_map.keys()))
native_country = native_country_map[native_input]

# Combine all inputs into feature array
features = np.array([[age, workclass, fnlwgt, educational_num, marital_status,
                      occupation, relationship, race, gender, capital_gain,
                      capital_loss, hours_per_week, native_country]])

# Scale the input
features_scaled = scaler.transform(features)

# Prediction
if st.button("Predict"):
    prediction = model.predict(features_scaled)[0]
    if prediction == 1:
        st.success("✅ Predicted Income: >50K")
    else:
        st.warning("🔻 Predicted Income: <=50K")
