import streamlit as st
import requests

st.set_page_config(page_title="Income Prediction App", page_icon="💰")
st.title("💼 Income Class Prediction")
st.markdown("Enter your details to predict if your annual income is >50K or ≤50K.")

# --------------------------
# Encoded value dictionaries
# --------------------------
workclass_map = {
    "Federal-gov": 0, "Local-gov": 1, "Never-worked": 2, "Private": 3,
    "Self-emp-inc": 4, "Self-emp-not-inc": 5, "State-gov": 6, "Without-pay": 7
}

marital_map = {
    "Divorced": 0, "Married-AF-spouse": 1, "Married-civ-spouse": 2,
    "Married-spouse-absent": 3, "Never-married": 4, "Separated": 5, "Widowed": 6
}

occupation_map = {
    "Adm-clerical": 0, "Armed-Forces": 1, "Craft-repair": 2, "Exec-managerial": 3,
    "Farming-fishing": 4, "Handlers-cleaners": 5, "Machine-op-inspct": 6, "Other-service": 7,
    "Priv-house-serv": 8, "Prof-specialty": 9, "Protective-serv": 10, "Sales": 11,
    "Tech-support": 12, "Transport-moving": 13
}

relationship_map = {
    "Husband": 0, "Not-in-family": 1, "Other-relative": 2,
    "Own-child": 3, "Unmarried": 4, "Wife": 5
}

race_map = {
    "Amer-Indian-Eskimo": 0, "Asian-Pac-Islander": 1, "Black": 2,
    "Other": 3, "White": 4
}

sex_map = {"Female": 0, "Male": 1}

native_country_map = {
    "Cambodia": 0, "Canada": 1, "China": 2, "Columbia": 3, "Cuba": 4,
    "Dominican-Republic": 5, "Ecuador": 6, "El-Salvador": 7, "England": 8, "France": 9,
    "Germany": 10, "Greece": 11, "Guatemala": 12, "Haiti": 13, "Holand-Netherlands": 14,
    "Honduras": 15, "Hong": 16, "Hungary": 17, "India": 18, "Iran": 19,
    "Ireland": 20, "Italy": 21, "Jamaica": 22, "Japan": 23, "Laos": 24,
    "Mexico": 25, "Nicaragua": 26, "Outlying-US(Guam-USVI-etc)": 27, "Peru": 28, "Philippines": 29,
    "Poland": 30, "Portugal": 31, "Puerto-Rico": 32, "Scotland": 33, "South": 34,
    "Taiwan": 35, "Thailand": 36, "Trinadad-Tobago": 37, "United-States": 38, "Vietnam": 39,
    "Yugoslavia": 40
}

education_map = {
    "Preschool": 1, "1st-4th": 2, "5th-6th": 3, "7th-8th": 4, "9th": 5,
    "10th": 6, "11th": 7, "12th": 8, "HS-grad": 9, "Some-college": 10,
    "Assoc-voc": 11, "Assoc-acdm": 12, "Bachelors": 13, "Masters": 14,
    "Prof-school": 15, "Doctorate": 16
}

# --------------------------
# Input form
# --------------------------
with st.form("prediction_form"):
    age = st.number_input("Age", min_value=18, max_value=100, step=1)

    workclass = st.selectbox("Workclass", options=list(workclass_map.keys()))
    education_num = st.selectbox("Education", options=list(education_map.keys()))
    marital_status = st.selectbox("Marital Status", options=list(marital_map.keys()))
    occupation = st.selectbox("Occupation", options=list(occupation_map.keys()))
    relationship = st.selectbox("Relationship", options=list(relationship_map.keys()))
    race = st.selectbox("Race", options=list(race_map.keys()))
    sex = st.selectbox("Sex", options=list(sex_map.keys()))
    capital_gain = st.number_input("Capital Gain", min_value=0)
    capital_loss = st.number_input("Capital Loss", min_value=0)
    hours_per_week = st.number_input("Hours Per Week", min_value=1, max_value=100, step=1)
    native_country = st.selectbox("Native Country", options=list(native_country_map.keys()))

    submitted = st.form_submit_button("Predict")

if submitted:
    with st.spinner("Sending data to model..."):
        try:
            # Replace with your FastAPI URL
            fastapi_url = "http://localhost:8000/predict"

            input_data = {
                "age": age,
                "workclass": workclass_map[workclass],
                "education_num": education_map[education_num],
                "marital_status": marital_map[marital_status],
                "occupation": occupation_map[occupation],
                "relationship": relationship_map[relationship],
                "race": race_map[race],
                "sex": sex_map[sex],
                "capital_gain": capital_gain,
                "capital_loss": capital_loss,
                "hours_per_week": hours_per_week,
                "native_country": native_country_map[native_country],
            }

            response = requests.post(fastapi_url, json=input_data)

            if response.status_code == 200:
                prediction = response.json().get("prediction", "Unknown")
                st.success(f"✅ Predicted Income Class: **{prediction}**")
            else:
                st.error(f"❌ Error: {response.status_code}\n{response.text}")

        except Exception as e:
            st.exception(f"Unexpected Error: {e}")
