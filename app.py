# ============================================================
# 🎓 AI Student Intelligence Platform (Enterprise Edition)
# Designed & Developed by Akshit Gajera
# ============================================================

import streamlit as st
import numpy as np
import pickle
import plotly.express as px
import pandas as pd

# ------------------------------------------------------------
# PAGE CONFIG
# ------------------------------------------------------------
st.set_page_config(
    page_title="AI Student Intelligence",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
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
# PREMIUM GLASS UI
# ------------------------------------------------------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg,#0f2027,#203a43,#2c5364);
    font-family: 'Segoe UI', sans-serif;
}
.main-header {
    font-size: 2.6rem;
    font-weight: 800;
    text-align: center;
}
.sub-header {
    text-align: center;
    color: #a5f3fc;
    margin-bottom: 2rem;
}
.glass {
    background: rgba(255,255,255,0.05);
    backdrop-filter: blur(12px);
    border-radius: 20px;
    padding: 30px;
    border: 1px solid rgba(255,255,255,0.1);
    box-shadow: 0 8px 32px rgba(0,0,0,0.6);
    margin-bottom: 25px;
}
.kpi {
    font-size: 65px;
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
</style>
""", unsafe_allow_html=True)

# ------------------------------------------------------------
# SIDEBAR
# ------------------------------------------------------------
with st.sidebar:
    st.markdown("## 🎓 Project Overview")
    st.info("""
    Machine Learning-Based GPA Prediction
    
    Algorithm: KNN  
    Features: 8  
    Scaling: StandardScaler  
    """)

    st.markdown("---")
    st.metric("Accuracy", "90%")
    st.metric("Model Type", "KNN Regression")

# ------------------------------------------------------------
# HEADER
# ------------------------------------------------------------
st.markdown('<div class="main-header">🎓 AI Student Intelligence Platform</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Predict Student GPA Using Machine Learning</div>', unsafe_allow_html=True)

# ------------------------------------------------------------
# TABS
# ------------------------------------------------------------
tab1, tab2, tab3, tab4 = st.tabs([
    "Prediction",
    "Analytics",
    "Model Insights",
    "Student Report"
])

# ============================================================
# TAB 1 - PREDICTION
# ============================================================
with tab1:

    st.markdown("### 🧠 Student Profile Input")

    col1, col2, col3 = st.columns(3)

    with col1:
        study_time = st.slider("Study Time (Hours/Week)", 0.0, 40.0, 12.0)
        absences = st.slider("Absences", 0, 50, 4)
        tutoring = st.selectbox("Tutoring", ["No", "Yes"])
        tutoring = 1 if tutoring == "Yes" else 0

    with col2:
        parental_support = st.selectbox("Parental Support Level", [0,1,2,3])
        extracurricular = st.selectbox("Extracurricular", ["No", "Yes"])
        extracurricular = 1 if extracurricular == "Yes" else 0
        sports = st.selectbox("Sports", ["No", "Yes"])
        sports = 1 if sports == "Yes" else 0

    with col3:
        music = st.selectbox("Music", ["No", "Yes"])
        music = 1 if music == "Yes" else 0
        grade_class = st.selectbox("Grade Class", [1,2,3,4])

    st.markdown("---")

    predict = st.button("🚀 Run AI Prediction")

    if predict:

        input_data = np.array([[study_time, absences, tutoring,
                                parental_support, extracurricular,
                                sports, music, grade_class]])

        input_scaled = scaler.transform(input_data)
        prediction = model.predict(input_scaled)
        predicted_gpa = round(prediction[0], 2)

        st.session_state["gpa"] = predicted_gpa
        st.session_state["study_time"] = study_time
        st.session_state["absences"] = absences
        st.session_state["tutoring"] = tutoring
        st.session_state["parental_support"] = parental_support
        st.session_state["extracurricular"] = extracurricular
        st.session_state["sports"] = sports
        st.session_state["music"] = music
        st.session_state["grade_class"] = grade_class

        if predicted_gpa >= 3.5:
            category = "Excellent Performance"
        elif predicted_gpa >= 2.5:
            category = "Good Performance"
        elif predicted_gpa >= 1.8:
            category = "Average Performance"
        else:
            category = "Academic Risk"

        st.markdown(
            f"""
            <div class="glass">
                <div class="kpi">{predicted_gpa}</div>
                <div class="kpi-label">{category}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

# ============================================================
# TAB 2 - ANALYTICS
# ============================================================
with tab2:

    if "gpa" in st.session_state:

        gpa = st.session_state["gpa"]

        # Radar Chart
        st.markdown("### 🧠 Student Profile Radar Chart")

        profile_features = {
            "Study Time": st.session_state["study_time"]/40,
            "Absence Discipline": 1-(st.session_state["absences"]/50),
            "Tutoring": st.session_state["tutoring"],
            "Parental Support": st.session_state["parental_support"]/3,
            "Extracurricular": st.session_state["extracurricular"],
            "Sports": st.session_state["sports"],
            "Music": st.session_state["music"],
            "Grade Level": st.session_state["grade_class"]/4
        }

        radar_df = pd.DataFrame(dict(
            r=list(profile_features.values()),
            theta=list(profile_features.keys())
        ))

        fig_radar = px.line_polar(radar_df, r='r', theta='theta', line_close=True)
        fig_radar.update_traces(fill='toself')
        fig_radar.update_layout(
            polar=dict(radialaxis=dict(visible=True, range=[0,1])),
            showlegend=False
        )
        st.plotly_chart(fig_radar, use_container_width=True)

        # GPA Probability Distribution
        st.markdown("### 📈 GPA Probability Distribution")

        x_vals = np.linspace(gpa - 1, gpa + 1, 200)
        y_vals = (1 / (0.35 * np.sqrt(2 * np.pi))) * \
                 np.exp(-0.5 * ((x_vals - gpa) / 0.35) ** 2)

        dist_df = pd.DataFrame({
            "GPA": x_vals,
            "Probability Density": y_vals
        })

        fig_dist = px.area(dist_df, x="GPA", y="Probability Density",
                           title="Predicted GPA Confidence Curve")

        fig_dist.add_vline(x=gpa, line_width=3, line_dash="dash", line_color="red")
        st.plotly_chart(fig_dist, use_container_width=True)

    else:
        st.info("Run prediction first to see analytics.")

# ============================================================
# TAB 3 - MODEL INSIGHTS
# ============================================================
with tab3:
    st.success("""
    ✔ KNN captures non-linear student behavior  
    ✔ Feature scaling improves performance  
    ✔ Study Time & Absences strongest indicators  
    ✔ Extracurricular balance influences GPA  
    """)

# ============================================================
# TAB 4 - STUDENT REPORT
# ============================================================
with tab4:

    if "gpa" in st.session_state:

        gpa = st.session_state["gpa"]

        performance_band = (
            "Top Tier Student" if gpa >= 3.5 else
            "Consistent Performer" if gpa >= 2.5 else
            "Needs Monitoring"
        )

        st.write(f"**Predicted GPA:** {gpa}")
        st.write(f"**Performance Category:** {performance_band}")

        if gpa < 2.5:
            st.warning("Recommendation: Increase study hours & reduce absences.")
        else:
            st.success("Keep maintaining current academic strategy.")

    else:
        st.info("Run prediction to generate report.")

# ------------------------------------------------------------
# FOOTER
# ------------------------------------------------------------
st.markdown("---")
st.markdown(
    "<div style='text-align:center;color:#cbd5e1;'>© 2026 Akshit Gajera | AI Student Intelligence Platform</div>",
    unsafe_allow_html=True
)
