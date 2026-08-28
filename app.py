import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Page configuration
st.set_page_config(
    page_title="Intelligent Mammogram Screening Recommendation System",
    page_icon="🩺",
    layout="wide"
)

# Title
st.title("🩺 Intelligent Mammogram Screening Recommendation System")
st.write(
    "AI-based system for analyzing patient screening information and "
    "providing a mammogram screening recommendation."
)

st.divider()

# Sidebar
st.sidebar.header("Patient Information")

age = st.sidebar.number_input(
    "Age",
    min_value=20,
    max_value=100,
    value=45
)

family_history = st.sidebar.selectbox(
    "Family History of Breast Cancer",
    ["No", "Yes"]
)

previous_abnormality = st.sidebar.selectbox(
    "Previous Breast Abnormality",
    ["No", "Yes"]
)

breast_symptoms = st.sidebar.selectbox(
    "Breast Symptoms",
    ["No", "Yes"]
)

# Main section
st.subheader("Patient Details")

col1, col2 = st.columns(2)

with col1:
    st.write("**Age:**", age)
    st.write("**Family History:**", family_history)

with col2:
    st.write("**Previous Abnormality:**", previous_abnormality)
    st.write("**Breast Symptoms:**", breast_symptoms)

st.divider()

# Recommendation button
if st.button("🔍 Generate Screening Recommendation"):

    # Calculate risk score
    risk_score = 0

    if age >= 50:
        risk_score += 2
    elif age >= 40:
        risk_score += 1

    if family_history == "Yes":
        risk_score += 2

    if previous_abnormality == "Yes":
        risk_score += 2

    if breast_symptoms == "Yes":
        risk_score += 3

    # Display result
    st.subheader("📊 AI Screening Recommendation")

    if risk_score >= 5:
        st.error("🔴 HIGH PRIORITY")
        st.write(
            "Recommendation: Mammogram screening and clinical evaluation "
            "should be considered promptly."
        )

    elif risk_score >= 3:
        st.warning("🟠 MODERATE PRIORITY")
        st.write(
            "Recommendation: Mammogram screening is recommended based on "
            "the provided risk factors."
        )

    else:
        st.success("🟢 ROUTINE PRIORITY")
        st.write(
            "Recommendation: Continue with routine screening according to "
            "applicable clinical screening guidelines."
        )

    # Show score
    st.metric("Risk Score", f"{risk_score}/9")

    # Risk Score Gauge Chart
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=risk_score,
        title={"text": "Risk Level"},
        gauge={
            "axis": {"range": [0, 9]},
            "bar": {"color": "red"},
            "steps": [
                {"range": [0, 3], "color": "green"},
                {"range": [3, 6], "color": "yellow"},
                {"range": [6, 9], "color": "orange"}
            ],
            "threshold": {
                "line": {"color": "red", "width": 4},
                "thickness": 0.75,
                "value": risk_score
            }
        }
    ))

    st.plotly_chart(fig, use_container_width=True)

    # Create result table
    result_data = {
        "Parameter": [
            "Age",
            "Family History",
            "Previous Abnormality",
            "Breast Symptoms",
            "Risk Score"
        ],
        "Value": [
            age,
            family_history,
            previous_abnormality,
            breast_symptoms,
            risk_score
        ]
    }

    df = pd.DataFrame(result_data)

    st.subheader("Patient Assessment Summary")
    st.table(df)

st.divider()

st.caption(
    "Disclaimer: This application is a prototype for academic/research purposes "
    "and is not a substitute for professional medical diagnosis."
)