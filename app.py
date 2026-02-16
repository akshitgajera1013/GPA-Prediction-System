# ============================================================
# 🎓 AI Student Intelligence Dashboard
# Designed & Developed by Akshit Gajera
# ============================================================

import streamlit as st
import numpy as np
import pickle

# ------------------------------------------------------------
# PAGE CONFIG
# ------------------------------------------------------------
st.set_page_config(
    page_title="AI Student Intelligence",
    page_icon="🎓",
    layout="wide"
)

# ------------------------------------------------------------
# LOAD MODEL
# ------------------------------------------------------------
@st.cache_resource
def load_objects():
    with open("model.pkl", "rb") as f:
        model = pickle.load(f)
    with open("scaler.pkl", "rb") as f:
        scaler = pickle.load(f)
    return model, scaler

model, scaler = load_objects()

# ------------------------------------------------------------
# ADVANCED DASHBOARD CSS
# ------------------------------------------------------------
st.markdown("""
<style>

/* Background Gradient */
.stApp {
    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
    font-family: 'Segoe UI', sans-serif;
}

/* Glass Card */
.glass {
    background: rgba(255,255,255,0.05);
    backdrop-filter: blur(15px);
    border-radius: 20px;
    padding: 30px;
    border: 1px solid rgba(255,255,255,0.1);
    box-shadow: 0 8px 32px rgba(0,0,0,0.6);
    margin-bottom: 25px;
}

/* Title */
.title {
    font-size: 50px;
    font-weight: 800;
    color: #ffffff;
}

.subtitle {
    color: #a5f3fc;
    font-size: 18px;
    margin-bottom: 25px;
}

/* Neon KPI */
.kpi {
    font-size: 60px;
    font-weight: bold;
    text-align: center;
    color: #00f5ff;
    text-shadow: 0 0 15px #00f5ff;
}

.kpi-label {
    text-align: center;
    font-size: 20px;
    color: #e0f2fe;
}

/* Sidebar Styling */
section[data-testid="stSidebar"] {
    background: rgba(0,0,0,0.4);
}

/* Button Glow */
.stButton>button {
    width: 100%;
    height: 55px;
    font-size: 18px;
    font-weight: bold;
    border-radius: 12px;
    background: linear-gradient(90deg,#00f5ff,#3b82f6);
    color: black;
    border: none;
    box-shadow: 0 0 20px #00f5ff;
}

.stButton>button:hover {
    box-shadow: 0 0 35px #00f5ff;
}

.footer {
    text-align: center;
    color: #cbd5e1;
    margin-top: 30px;
}

</style>
""", unsafe_allow_html=True)

# ------------------------------------------------------------
# HEADER
# ------------------------------------------------------------
st.markdown('<div class="title">AI Student Intelligence</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Machine Learning-Based GPA Prediction System</div>', unsafe_allow_html=True)

# ------------------------------------------------------------
# DASHBOARD LAYOUT
# ------------------------------------------------------------
left, right = st.columns([1.2, 1])

# ------------------------------------------------------------
# LEFT PANEL (Analytics Preview)
# ------------------------------------------------------------
with left:
    st.markdown('<div class="glass">', unsafe_allow_html=True)
    st.subheader("📊 Academic Analytics Overview")

    colA, colB, colC = st.columns(3)

    colA.metric("Model Accuracy", "90%")
    colB.metric("Algorithm", "KNN")
    colC.metric("Features", "8")

    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown('<div class="glass">', unsafe_allow_html=True)
    st.subheader("🎯 Prediction Result")

    prediction_placeholder = st.empty()

    st.markdown("</div>", unsafe_allow_html=True)

# ------------------------------------------------------------
# RIGHT PANEL (Input Controls)
# ------------------------------------------------------------
with right:
    st.markdown('<div class="glass">', unsafe_allow_html=True)
    st.subheader("🧠 Student Profile Input")

    study_time = st.slider("Study Time (Hours/Week)", 0.0, 40.0, 12.0)
    absences = st.slider("Absences", 0, 50, 4)

    tutoring = st.selectbox("Tutoring Support", ["No", "Yes"])
    tutoring = 1 if tutoring == "Yes" else 0

    parental_support = st.selectbox("Parental Support Level", [0,1,2,3])
    extracurricular = st.selectbox("Extracurricular", ["No", "Yes"])
    extracurricular = 1 if extracurricular == "Yes" else 0

    sports = st.selectbox("Sports", ["No", "Yes"])
    sports = 1 if sports == "Yes" else 0

    music = st.selectbox("Music", ["No", "Yes"])
    music = 1 if music == "Yes" else 0

    grade_class = st.selectbox("Grade Class", [1,2,3,4])

    predict = st.button("🚀 Run AI Prediction")

    st.markdown("</div>", unsafe_allow_html=True)

# ------------------------------------------------------------
# PREDICTION LOGIC
# ------------------------------------------------------------
if predict:
    try:
        input_data = np.array([[
            study_time,
            absences,
            tutoring,
            parental_support,
            extracurricular,
            sports,
            music,
            grade_class
        ]])

        input_scaled = scaler.transform(input_data)
        prediction = model.predict(input_scaled)
        predicted_gpa = round(prediction[0], 2)

        if predicted_gpa >= 3.5:
            category = "Excellent Performance"
        elif predicted_gpa >= 2.5:
            category = "Good Performance"
        elif predicted_gpa >= 1.8:
            category = "Average Performance"
        else:
            category = "Academic Risk"

        prediction_placeholder.markdown(
            f'<div class="kpi">{predicted_gpa}</div>'
            f'<div class="kpi-label">{category}</div>',
            unsafe_allow_html=True
        )

    except Exception as e:
        st.error(f"Prediction Error: {e}")

# ------------------------------------------------------------
# FOOTER
# ------------------------------------------------------------
st.markdown(
    '<div class="footer">© 2026 Akshit Gajera | AI ML Dashboard</div>',
    unsafe_allow_html=True
)
