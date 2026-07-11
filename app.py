import streamlit as st
from hospital_decision_support import predict_patient
st.title("🏥 Hospital Decision Support System")


age = st.number_input(
    "Age",
    min_value=1,
    max_value=120,
    value=40
)


gender = st.selectbox(
    "Gender",
    [
        "Male",
        "Female"
    ]
)


department = st.selectbox(
    "Department",
    [
        "Cardiology",
        "Neurology",
        "Oncology",
        "Orthopedics",
        "Emergency",
        "General Surgery",
        "Pediatrics"
    ]
)


diagnosis = st.selectbox(
    "Diagnosis",
    [
        "Cancer",
        "Malaria",
        "Fracture",
        "Infection",
        "Hypertension"
    ]
)


if st.button("Predict"):

    result = predict_patient(
        age,
        gender,
        department,
        diagnosis
    )


    st.success(
        f"Expected Hospital Stay: {result['Hospital Stay']}"
    )


    st.info(
        f"Expected Treatment: {result['Treatment']}"
    )


    st.warning(
        f"Expected Medical Bill: {result['Medical Bill']}"
    )
