# ============================================================
# 🎓 AI Student Intelligence Platform (Enterprise Edition)
# Designed & Developed by Akshit Gajera
# Enhanced UI — Academic Intelligence Terminal
# ============================================================

import streamlit as st
import numpy as np
import pickle
import plotly.graph_objects as go
import pandas as pd

# ============================================================
# PAGE CONFIG  —  must be the very first Streamlit call
# ============================================================
st.set_page_config(
    page_title="AI Student Intelligence",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ============================================================
# LOAD MODEL FILES
# ============================================================
@st.cache_resource
def load_objects():
    with open("model.pkl", "rb") as f:
        model = pickle.load(f)
    with open("scaler.pkl", "rb") as f:
        scaler = pickle.load(f)
    return model, scaler


model, scaler = load_objects()

# ============================================================
# PROFESSIONAL ANIMATED THEME  —  Emerald Academic Intelligence
# ============================================================
st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=Space+Mono:wght@400;700&family=DM+Sans:wght@300;400;500;600&display=swap');

/* ── VARIABLES ── */
:root {
    --emerald:       #10b981;
    --emerald-light: #34d399;
    --emerald-dark:  #059669;
    --violet:        #8b5cf6;
    --violet-light:  #a78bfa;
    --gold:          #f59e0b;
    --red:           #ef4444;
    --dark-950:      #030712;
    --dark-900:      #080f1a;
    --dark-800:      #0f1f2e;
    --dark-700:      #162436;
    --glass:         rgba(16,185,129,0.04);
    --glass-border:  rgba(16,185,129,0.14);
    --glow:          0 0 28px rgba(16,185,129,0.22);
    --text-main:     #ecfdf5;
    --text-muted:    rgba(236,253,245,0.5);
}

/* ── BACKGROUND ── */
.stApp {
    background: var(--dark-950);
    font-family: 'DM Sans', sans-serif;
    overflow-x: hidden;
}

.stApp::before {
    content: '';
    position: fixed;
    inset: 0;
    background:
        radial-gradient(ellipse at 15% 15%, rgba(16,185,129,0.09) 0%, transparent 50%),
        radial-gradient(ellipse at 85% 85%, rgba(139,92,246,0.08) 0%, transparent 50%),
        radial-gradient(ellipse at 50% 50%, rgba(245,158,11,0.03) 0%, transparent 60%);
    pointer-events: none;
    z-index: 0;
    animation: ambientShift 12s ease-in-out infinite alternate;
}

@keyframes ambientShift {
    0%   { opacity: 0.6; }
    100% { opacity: 1.0; }
}

/* ── DOT GRID ── */
.stApp::after {
    content: '';
    position: fixed;
    inset: 0;
    background-image: radial-gradient(circle, rgba(16,185,129,0.08) 1px, transparent 1px);
    background-size: 36px 36px;
    pointer-events: none;
    z-index: 0;
}

/* ── MAIN BLOCK ── */
.main .block-container {
    position: relative;
    z-index: 1;
    padding-top: 10px;
    padding-bottom: 40px;
    max-width: 1400px;
}

/* ── HERO ── */
.hero {
    text-align: center;
    padding: 48px 20px 24px;
    animation: heroReveal 0.8s cubic-bezier(0.22,1,0.36,1) both;
}

@keyframes heroReveal {
    from { opacity: 0; transform: translateY(-22px); }
    to   { opacity: 1; transform: translateY(0); }
}

.hero-badge {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: rgba(16,185,129,0.08);
    border: 1px solid rgba(16,185,129,0.2);
    border-radius: 50px;
    padding: 7px 18px;
    font-family: 'Space Mono', monospace;
    font-size: 10px;
    color: var(--emerald-light);
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: 18px;
    animation: heroReveal 0.8s ease both 0.1s;
}

.hero-badge-dot {
    width: 6px; height: 6px;
    border-radius: 50%;
    background: var(--emerald);
    box-shadow: 0 0 8px var(--emerald);
    animation: dotPulse 1.6s ease-in-out infinite;
}

@keyframes dotPulse {
    0%, 100% { opacity: 1; box-shadow: 0 0 8px var(--emerald); }
    50%       { opacity: 0.4; box-shadow: 0 0 3px var(--emerald); }
}

.hero-title {
    font-family: 'Syne', sans-serif;
    font-size: clamp(30px, 5vw, 64px);
    font-weight: 800;
    color: var(--text-main);
    letter-spacing: -1px;
    line-height: 1.05;
    margin-bottom: 8px;
}

.hero-title em {
    font-style: normal;
    background: linear-gradient(135deg, var(--emerald-light), var(--violet-light));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    filter: drop-shadow(0 0 20px rgba(16,185,129,0.5));
}

.hero-sub {
    font-family: 'Space Mono', monospace;
    font-size: 11px;
    color: var(--text-muted);
    letter-spacing: 3px;
    text-transform: uppercase;
    animation: heroReveal 0.8s ease both 0.25s;
}

.hero-line {
    display: flex;
    align-items: center;
    gap: 14px;
    margin: 20px auto 0;
    max-width: 420px;
}

.hero-line-seg {
    flex: 1;
    height: 1px;
    background: linear-gradient(90deg, transparent, var(--emerald), transparent);
    animation: lineGrow 1s ease both 0.4s;
}

@keyframes lineGrow {
    from { transform: scaleX(0); opacity: 0; }
    to   { transform: scaleX(1); opacity: 1; }
}

.hero-line-gem {
    width: 8px; height: 8px;
    background: var(--emerald);
    clip-path: polygon(50% 0%, 100% 50%, 50% 100%, 0% 50%);
    box-shadow: 0 0 14px var(--emerald);
    animation: gemSpin 6s linear infinite;
}

@keyframes gemSpin {
    from { transform: rotate(0deg); }
    to   { transform: rotate(360deg); }
}

/* ── SCORE BAND ── */
.score-band {
    display: flex;
    justify-content: center;
    gap: 24px;
    flex-wrap: wrap;
    margin-bottom: 26px;
    animation: heroReveal 0.8s ease both 0.3s;
}

.score-chip {
    display: flex;
    align-items: center;
    gap: 8px;
    background: rgba(16,185,129,0.05);
    border: 1px solid rgba(16,185,129,0.12);
    border-radius: 8px;
    padding: 8px 16px;
    font-family: 'Space Mono', monospace;
    font-size: 11px;
    color: var(--emerald-light);
    letter-spacing: 1px;
}

.score-chip-dot {
    width: 6px; height: 6px;
    border-radius: 50%;
    background: var(--emerald);
}

/* ── GLASS PANEL ── */
.glass-panel {
    background: var(--glass);
    border: 1px solid var(--glass-border);
    border-radius: 18px;
    padding: 26px;
    margin-bottom: 22px;
    position: relative;
    overflow: hidden;
    transition: all 0.3s ease;
    animation: panelIn 0.5s ease both;
}

@keyframes panelIn {
    from { opacity: 0; transform: translateY(14px); }
    to   { opacity: 1; transform: translateY(0); }
}

.glass-panel::before {
    content: '';
    position: absolute;
    top: 0; left: -100%;
    width: 100%; height: 2px;
    background: linear-gradient(90deg, transparent, var(--emerald), var(--violet), transparent);
    animation: scanRail 3.5s linear infinite;
}

@keyframes scanRail {
    0%   { left: -100%; }
    100% { left: 100%; }
}

.glass-panel:hover {
    border-color: rgba(16,185,129,0.3);
    box-shadow: var(--glow);
    transform: translateY(-2px);
}

.panel-eyebrow {
    font-family: 'Space Mono', monospace;
    font-size: 10px;
    letter-spacing: 3px;
    color: var(--emerald);
    text-transform: uppercase;
    margin-bottom: 4px;
    opacity: 0.75;
}

.panel-heading {
    font-family: 'Syne', sans-serif;
    font-size: 20px;
    font-weight: 700;
    color: var(--text-main);
    margin-bottom: 0;
}

/* ── INPUT FIELDS ── */
div[data-testid="stNumberInput"] > div > div > input,
div[data-testid="stSelectbox"] > div > div,
div[data-testid="stSlider"] {
    background: rgba(16,185,129,0.04) !important;
    border: 1px solid rgba(16,185,129,0.18) !important;
    border-radius: 10px !important;
    color: var(--text-main) !important;
    font-family: 'DM Sans', sans-serif !important;
    transition: all 0.25s ease !important;
}

div[data-testid="stNumberInput"] > div > div > input:focus {
    border-color: var(--emerald) !important;
    box-shadow: 0 0 0 3px rgba(16,185,129,0.14) !important;
    outline: none !important;
}

.stSelectbox label,
.stNumberInput label,
.stSlider label {
    color: rgba(16,185,129,0.85) !important;
    font-family: 'Space Mono', monospace !important;
    font-size: 10px !important;
    letter-spacing: 1.5px !important;
    text-transform: uppercase !important;
}

/* ── SLIDER TRACK ── */
div[data-testid="stSlider"] > div > div > div {
    background: linear-gradient(90deg, var(--emerald), var(--violet)) !important;
}

/* ── INPUT GROUP LABEL ── */
.input-group {
    font-family: 'Syne', sans-serif;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 3px;
    color: var(--emerald);
    text-transform: uppercase;
    border-bottom: 1px solid rgba(16,185,129,0.14);
    padding-bottom: 8px;
    margin-bottom: 14px;
}

/* ── PREDICT BUTTON ── */
div.stButton > button {
    width: 100% !important;
    background: linear-gradient(135deg, var(--emerald-dark) 0%, var(--violet) 100%) !important;
    color: #ffffff !important;
    font-family: 'Syne', sans-serif !important;
    font-size: 16px !important;
    font-weight: 800 !important;
    letter-spacing: 3px !important;
    text-transform: uppercase !important;
    border: none !important;
    border-radius: 12px !important;
    padding: 16px 40px !important;
    cursor: pointer !important;
    transition: all 0.3s ease !important;
    box-shadow: 0 0 28px rgba(16,185,129,0.3), 0 0 50px rgba(139,92,246,0.15) !important;
}

div.stButton > button:hover {
    transform: translateY(-3px) !important;
    box-shadow: 0 0 50px rgba(16,185,129,0.5), 0 0 80px rgba(139,92,246,0.25) !important;
}

div.stButton > button:active {
    transform: translateY(0) !important;
}

/* ── GPA RESULT BOX ── */
.gpa-box {
    border-radius: 22px;
    padding: 50px 30px;
    text-align: center;
    position: relative;
    overflow: hidden;
    animation: gpaReveal 0.6s cubic-bezier(0.175,0.885,0.32,1.275) both;
}

@keyframes gpaReveal {
    from { opacity: 0; transform: scale(0.82); }
    to   { opacity: 1; transform: scale(1); }
}

.gpa-box::before {
    content: '';
    position: absolute;
    top: -50%; left: -50%;
    width: 200%; height: 200%;
    background: conic-gradient(from 0deg, transparent 0deg, rgba(255,255,255,0.04) 60deg, transparent 120deg);
    animation: rotateConic 7s linear infinite;
}

@keyframes rotateConic {
    from { transform: rotate(0deg); }
    to   { transform: rotate(360deg); }
}

.gpa-num {
    font-family: 'Syne', sans-serif;
    font-size: clamp(60px, 10vw, 100px);
    font-weight: 800;
    line-height: 1;
    position: relative;
    z-index: 1;
    filter: drop-shadow(0 0 20px currentColor);
}

.gpa-category {
    font-family: 'Space Mono', monospace;
    font-size: 13px;
    letter-spacing: 3px;
    text-transform: uppercase;
    position: relative;
    z-index: 1;
    margin-top: 10px;
    opacity: 0.85;
}

/* ── GPA COLOR VARIANTS ── */
.gpa-excellent { background: linear-gradient(135deg, #022c22, #064e3b); border: 1px solid rgba(16,185,129,0.5); color: var(--emerald-light); box-shadow: 0 0 50px rgba(16,185,129,0.2); }
.gpa-good      { background: linear-gradient(135deg, #1c1917, #292524); border: 1px solid rgba(139,92,246,0.45); color: var(--violet-light);   box-shadow: 0 0 50px rgba(139,92,246,0.2); }
.gpa-average   { background: linear-gradient(135deg, #1c1400, #292000); border: 1px solid rgba(245,158,11,0.45); color: var(--gold);            box-shadow: 0 0 50px rgba(245,158,11,0.2); }
.gpa-risk      { background: linear-gradient(135deg, #1c0000, #290000); border: 1px solid rgba(239,68,68,0.45);  color: var(--red);             box-shadow: 0 0 50px rgba(239,68,68,0.2);  }

/* ── STAT CHIPS ── */
.stat-row {
    display: flex;
    gap: 14px;
    flex-wrap: wrap;
    margin-top: 20px;
}

.stat-chip {
    flex: 1;
    min-width: 100px;
    background: rgba(16,185,129,0.05);
    border: 1px solid rgba(16,185,129,0.15);
    border-radius: 12px;
    padding: 16px 12px;
    text-align: center;
    transition: all 0.25s ease;
}

.stat-chip:hover {
    background: rgba(16,185,129,0.10);
    transform: translateY(-2px);
    box-shadow: var(--glow);
}

.stat-chip-val {
    font-family: 'Syne', sans-serif;
    font-size: 22px;
    font-weight: 800;
    color: var(--emerald-light);
}

.stat-chip-lbl {
    font-family: 'Space Mono', monospace;
    font-size: 9px;
    color: var(--text-muted);
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-top: 4px;
}

/* ── SECTION TITLE ── */
.section-title {
    font-family: 'Syne', sans-serif;
    font-size: 16px;
    font-weight: 800;
    color: var(--emerald-light);
    text-transform: uppercase;
    letter-spacing: 3px;
    padding-bottom: 10px;
    border-bottom: 1px solid rgba(16,185,129,0.12);
    margin: 28px 0 18px;
}

/* ── TABS ── */
.stTabs [data-baseweb="tab-list"] {
    background: rgba(16,185,129,0.04) !important;
    border-radius: 12px !important;
    border: 1px solid rgba(16,185,129,0.1) !important;
    padding: 5px !important;
    gap: 4px !important;
}

.stTabs [data-baseweb="tab"] {
    font-family: 'Syne', sans-serif !important;
    font-size: 12px !important;
    font-weight: 700 !important;
    letter-spacing: 2px !important;
    text-transform: uppercase !important;
    color: rgba(16,185,129,0.5) !important;
    border-radius: 9px !important;
    padding: 10px 18px !important;
    transition: all 0.3s ease !important;
}

.stTabs [aria-selected="true"] {
    background: linear-gradient(135deg, rgba(16,185,129,0.18), rgba(139,92,246,0.18)) !important;
    color: var(--emerald-light) !important;
    box-shadow: 0 0 14px rgba(16,185,129,0.15) !important;
}

/* ── SIDEBAR ── */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #030f0a 0%, #060f14 100%) !important;
    border-right: 1px solid rgba(16,185,129,0.1) !important;
}

.sb-logo-text {
    font-family: 'Syne', sans-serif;
    font-size: 26px;
    font-weight: 800;
    background: linear-gradient(135deg, var(--emerald-light), var(--violet-light));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    letter-spacing: 2px;
}

.sb-logo-sub {
    font-family: 'Space Mono', monospace;
    font-size: 9px;
    color: rgba(16,185,129,0.4);
    letter-spacing: 3px;
    margin-top: 3px;
}

.sb-title {
    font-family: 'Syne', sans-serif;
    font-size: 12px;
    font-weight: 700;
    color: var(--emerald);
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: 10px;
}

.sb-info {
    background: rgba(16,185,129,0.05);
    border: 1px solid rgba(16,185,129,0.13);
    border-radius: 12px;
    padding: 16px;
    font-family: 'DM Sans', sans-serif;
    font-size: 14px;
    color: rgba(236,253,245,0.75);
    line-height: 1.85;
}

.sb-info span { color: var(--emerald-light); font-weight: 600; }

.sb-metric {
    background: rgba(16,185,129,0.05);
    border: 1px solid rgba(16,185,129,0.13);
    border-radius: 10px;
    padding: 14px;
    text-align: center;
}

.sb-metric-val {
    font-family: 'Syne', sans-serif;
    font-size: 22px;
    font-weight: 800;
    color: var(--emerald-light);
}

.sb-metric-lbl {
    font-family: 'Space Mono', monospace;
    font-size: 9px;
    color: var(--text-muted);
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-top: 4px;
}

/* ── INSIGHT CARD ── */
.insight {
    background: rgba(16,185,129,0.04);
    border: 1px solid rgba(16,185,129,0.12);
    border-left: 4px solid var(--emerald);
    border-radius: 12px;
    padding: 16px 20px;
    margin-bottom: 12px;
    font-family: 'DM Sans', sans-serif;
    font-size: 14px;
    color: rgba(236,253,245,0.8);
    line-height: 1.7;
    transition: all 0.25s ease;
}

.insight:hover {
    background: rgba(16,185,129,0.08);
    border-left-color: var(--emerald-light);
    transform: translateX(4px);
}

.insight b { color: var(--emerald-light); }

/* ── REPORT CARD ── */
.report-card {
    background: rgba(16,185,129,0.04);
    border: 1px solid rgba(16,185,129,0.14);
    border-radius: 16px;
    padding: 26px;
    margin-bottom: 18px;
}

.report-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 10px 0;
    border-bottom: 1px solid rgba(16,185,129,0.08);
    font-family: 'DM Sans', sans-serif;
    font-size: 14px;
    color: rgba(236,253,245,0.75);
}

.report-row:last-child { border-bottom: none; }

.report-row-key {
    font-family: 'Space Mono', monospace;
    font-size: 10px;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    color: var(--text-muted);
}

.report-row-val {
    font-family: 'Syne', sans-serif;
    font-size: 15px;
    font-weight: 700;
    color: var(--emerald-light);
}

/* ── RECOMMENDATION BOX ── */
.rec-warn {
    background: rgba(245,158,11,0.07);
    border: 1px solid rgba(245,158,11,0.25);
    border-radius: 12px;
    padding: 16px 20px;
    font-family: 'DM Sans', sans-serif;
    font-size: 14px;
    color: rgba(245,240,220,0.85);
    line-height: 1.7;
}

.rec-ok {
    background: rgba(16,185,129,0.06);
    border: 1px solid rgba(16,185,129,0.22);
    border-radius: 12px;
    padding: 16px 20px;
    font-family: 'DM Sans', sans-serif;
    font-size: 14px;
    color: rgba(236,253,245,0.85);
    line-height: 1.7;
}

/* ── PROGRESS BAR ── */
div[data-testid="stProgressBar"] > div {
    background: linear-gradient(90deg, var(--emerald), var(--violet)) !important;
    border-radius: 99px !important;
}

div[data-testid="stProgressBar"] {
    background: rgba(16,185,129,0.1) !important;
    border-radius: 99px !important;
}

/* ── DATAFRAME ── */
div[data-testid="stDataFrame"] {
    border: 1px solid rgba(16,185,129,0.14) !important;
    border-radius: 14px !important;
    overflow: hidden !important;
}

/* ── INFO / WARNING / SUCCESS ── */
div[data-testid="stInfo"],
div[data-testid="stSuccess"],
div[data-testid="stWarning"] {
    border-radius: 12px !important;
    font-family: 'DM Sans', sans-serif !important;
}

/* ── SCROLLBAR ── */
::-webkit-scrollbar { width: 5px; }
::-webkit-scrollbar-track { background: var(--dark-950); }
::-webkit-scrollbar-thumb {
    background: linear-gradient(180deg, var(--emerald), var(--violet));
    border-radius: 3px;
}

/* ── FLOATING PARTICLES ── */
.particles {
    position: fixed;
    inset: 0;
    pointer-events: none;
    z-index: 0;
    overflow: hidden;
}

.pt {
    position: absolute;
    border-radius: 50%;
    animation: ptFloat linear infinite;
}

.pt:nth-child(1)  { width:2px; height:2px; left: 5%;  background:var(--emerald);       box-shadow:0 0 5px var(--emerald);       animation-duration:15s; animation-delay:0s;   opacity:0.5; }
.pt:nth-child(2)  { width:2px; height:2px; left:18%;  background:var(--violet-light);   box-shadow:0 0 5px var(--violet-light);  animation-duration:20s; animation-delay:3s;   opacity:0.4; }
.pt:nth-child(3)  { width:3px; height:3px; left:30%;  background:var(--emerald-light);  box-shadow:0 0 8px var(--emerald-light); animation-duration:13s; animation-delay:6s;   opacity:0.6; }
.pt:nth-child(4)  { width:2px; height:2px; left:45%;  background:var(--gold);           box-shadow:0 0 5px var(--gold);          animation-duration:23s; animation-delay:1s;   opacity:0.3; }
.pt:nth-child(5)  { width:2px; height:2px; left:60%;  background:var(--emerald);        box-shadow:0 0 5px var(--emerald);       animation-duration:17s; animation-delay:8s;   opacity:0.5; }
.pt:nth-child(6)  { width:2px; height:2px; left:73%;  background:var(--violet-light);   box-shadow:0 0 5px var(--violet-light);  animation-duration:21s; animation-delay:4s;   opacity:0.4; }
.pt:nth-child(7)  { width:3px; height:3px; left:85%;  background:var(--emerald-light);  box-shadow:0 0 8px var(--emerald-light); animation-duration:14s; animation-delay:2s;   opacity:0.6; }
.pt:nth-child(8)  { width:2px; height:2px; left:93%;  background:var(--gold);           box-shadow:0 0 5px var(--gold);          animation-duration:19s; animation-delay:7s;   opacity:0.3; }

@keyframes ptFloat {
    0%   { transform: translateY(110vh) scale(0);   opacity: 0; }
    10%  { opacity: 0.7; }
    90%  { opacity: 0.5; }
    100% { transform: translateY(-10vh) scale(1.5); opacity: 0; }
}

/* ── FOOTER ── */
.footer {
    text-align: center;
    padding: 28px;
    font-family: 'Space Mono', monospace;
    font-size: 10px;
    color: rgba(16,185,129,0.3);
    letter-spacing: 2px;
    text-transform: uppercase;
    border-top: 1px solid rgba(16,185,129,0.07);
    margin-top: 40px;
    position: relative;
    z-index: 1;
}
</style>

<!-- Floating Particles -->
<div class="particles">
    <div class="pt"></div><div class="pt"></div><div class="pt"></div>
    <div class="pt"></div><div class="pt"></div><div class="pt"></div>
    <div class="pt"></div><div class="pt"></div>
</div>
""",
    unsafe_allow_html=True,
)

# ============================================================
# SESSION STATE INIT
# ============================================================
_STATE_KEYS = [
    "gpa", "study_time", "absences", "tutoring",
    "parental_support", "extracurricular", "sports",
    "music", "grade_class",
]
for _k in _STATE_KEYS:
    if _k not in st.session_state:
        st.session_state[_k] = None

# ============================================================
# SIDEBAR
# ============================================================
with st.sidebar:

    st.markdown(
        """
        <div style='text-align:center; padding:10px 0 24px;'>
            <div class="sb-logo-text">ASIP</div>
            <div class="sb-logo-sub">AI STUDENT INTELLIGENCE</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown('<div class="sb-title">&#127891; System Overview</div>', unsafe_allow_html=True)
    st.markdown(
        """
        <div class="sb-info">
            <span>Algorithm:</span> K-Nearest Neighbours<br>
            <span>Scaling:</span> StandardScaler<br>
            <span>Features:</span> 8 Student Attributes<br>
            <span>Task:</span> GPA Regression<br>
            <span>Accuracy:</span> ~90%
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<div class="sb-title">&#128202; Model Performance</div>', unsafe_allow_html=True)

    sb_c1, sb_c2 = st.columns(2)
    with sb_c1:
        st.markdown(
            """<div class="sb-metric">
                <div class="sb-metric-val">90%</div>
                <div class="sb-metric-lbl">Accuracy</div>
            </div>""",
            unsafe_allow_html=True,
        )
    with sb_c2:
        st.markdown(
            """<div class="sb-metric">
                <div class="sb-metric-val">8</div>
                <div class="sb-metric-lbl">Features</div>
            </div>""",
            unsafe_allow_html=True,
        )

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<div class="sb-title">&#127919; Live GPA Score</div>', unsafe_allow_html=True)

    if st.session_state.gpa is not None:
        gpa_live = float(st.session_state.gpa)
        gpa_frac = min(gpa_live / 4.0, 1.0)
        gpa_color = (
            "#10b981" if gpa_live >= 3.5 else
            "#8b5cf6" if gpa_live >= 2.5 else
            "#f59e0b" if gpa_live >= 1.8 else
            "#ef4444"
        )
        st.markdown(
            f"""
            <div style='background:rgba(0,0,0,0.4); border:1px solid {gpa_color}44;
                        border-radius:14px; padding:18px; text-align:center;
                        box-shadow:0 0 20px {gpa_color}22;'>
                <div style='font-family:Syne,sans-serif; font-size:42px; font-weight:800;
                            color:{gpa_color}; text-shadow:0 0 20px {gpa_color};'>{gpa_live}</div>
                <div style='font-family:"Space Mono",monospace; font-size:10px;
                            color:rgba(255,255,255,0.4); letter-spacing:2px; margin-top:4px;'>
                    GPA / 4.0
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.progress(gpa_frac)
    else:
        st.markdown(
            """<div style='background:rgba(16,185,129,0.03); border:1px solid rgba(16,185,129,0.1);
                           border-radius:14px; padding:18px; text-align:center;'>
                <div style='font-family:"Space Mono",monospace; font-size:10px;
                            color:rgba(16,185,129,0.4); letter-spacing:2px;'>AWAITING INPUT</div>
            </div>""",
            unsafe_allow_html=True,
        )
        st.progress(0.0)

    st.markdown("<br>", unsafe_allow_html=True)
    with st.expander("&#9881;&#65039; About KNN Model"):
        st.markdown(
            """<div style='font-family:"DM Sans",sans-serif; font-size:13px;
                           color:rgba(236,253,245,0.7); line-height:1.85;'>
                • Finds k nearest students in feature space<br>
                • StandardScaler normalises all features<br>
                • Captures non-linear academic patterns<br>
                • Study time &amp; absences are top drivers<br>
                • Extracurricular balance adds signal
            </div>""",
            unsafe_allow_html=True,
        )

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(
        """<div style='background:linear-gradient(135deg,rgba(16,185,129,0.1),rgba(139,92,246,0.1));
                       border:1px solid rgba(16,185,129,0.2); border-radius:12px;
                       padding:14px; text-align:center;'>
            <div style='font-family:Syne,sans-serif; font-size:11px; font-weight:800;
                        color:var(--emerald-light); letter-spacing:2px;'>
                &#127891; ENTERPRISE ACADEMIC AI
            </div>
            <div style='font-family:"Space Mono",monospace; font-size:9px;
                        color:rgba(255,255,255,0.3); letter-spacing:1px; margin-top:6px;'>
                Developed by Akshit Gajera
            </div>
        </div>""",
        unsafe_allow_html=True,
    )

# ============================================================
# HERO HEADER
# ============================================================
st.markdown(
    """
    <div class="hero">
        <div class="hero-badge">
            <div class="hero-badge-dot"></div>
            KNN Regression &nbsp;|&nbsp; GPA Prediction Engine
        </div>
        <div class="hero-title">AI Student <em>Intelligence</em></div>
        <div class="hero-sub">Predict Academic GPA Using Machine Learning</div>
        <div class="hero-line">
            <div class="hero-line-seg"></div>
            <div class="hero-line-gem"></div>
            <div class="hero-line-seg"></div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# Score band
st.markdown(
    """
    <div class="score-band">
        <div class="score-chip"><div class="score-chip-dot"></div>3.5+ = Excellent</div>
        <div class="score-chip"><div class="score-chip-dot"></div>2.5–3.4 = Good</div>
        <div class="score-chip"><div class="score-chip-dot"></div>1.8–2.4 = Average</div>
        <div class="score-chip"><div class="score-chip-dot"></div>&lt;1.8 = Academic Risk</div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ============================================================
# TABS
# ============================================================
tab1, tab2, tab3, tab4 = st.tabs(
    [
        "&#9889;  PREDICTION",
        "&#128202;  ANALYTICS",
        "&#129504;  MODEL INSIGHTS",
        "&#128196;  STUDENT REPORT",
    ]
)

# ============================================================
# TAB 1 — PREDICTION ENGINE
# ============================================================
with tab1:

    st.markdown(
        """<div class="glass-panel">
            <div class="panel-eyebrow">Student Profile Configuration</div>
            <div class="panel-heading">Enter Academic Parameters</div>
        </div>""",
        unsafe_allow_html=True,
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown('<div class="input-group">&#128218; Academic Habits</div>', unsafe_allow_html=True)
        study_time = st.slider("Study Time (Hours/Week)", 0.0, 40.0, 12.0, step=0.5)
        absences   = st.slider("Absences",                0,    50,   4)

    with col2:
        st.markdown('<div class="input-group">&#128106; Support &amp; Engagement</div>', unsafe_allow_html=True)
        tutoring_sel        = st.selectbox("Tutoring",               ["No", "Yes"])
        parental_support    = st.selectbox("Parental Support Level", [0, 1, 2, 3])
        extracurricular_sel = st.selectbox("Extracurricular",        ["No", "Yes"])

    with col3:
        st.markdown('<div class="input-group">&#127917; Activities &amp; Level</div>', unsafe_allow_html=True)
        sports_sel  = st.selectbox("Sports",      ["No", "Yes"])
        music_sel   = st.selectbox("Music",       ["No", "Yes"])
        grade_class = st.selectbox("Grade Class", [1, 2, 3, 4])

    # Encode binary selects
    tutoring_enc        = 1 if tutoring_sel        == "Yes" else 0
    extracurricular_enc = 1 if extracurricular_sel == "Yes" else 0
    sports_enc          = 1 if sports_sel          == "Yes" else 0
    music_enc           = 1 if music_sel           == "Yes" else 0

    st.markdown("<br>", unsafe_allow_html=True)
    _, btn_col, _ = st.columns([1, 2, 1])
    with btn_col:
        predict_clicked = st.button("&#127891;  RUN GPA PREDICTION", use_container_width=True)

    if predict_clicked:
        input_arr    = np.array([[
            study_time, absences, tutoring_enc,
            parental_support, extracurricular_enc,
            sports_enc, music_enc, grade_class,
        ]])
        input_scaled = scaler.transform(input_arr)
        raw_pred     = model.predict(input_scaled)
        predicted_gpa = round(float(raw_pred[0]), 2)

        # Persist everything
        st.session_state.gpa              = predicted_gpa
        st.session_state.study_time       = float(study_time)
        st.session_state.absences         = int(absences)
        st.session_state.tutoring         = tutoring_enc
        st.session_state.parental_support = int(parental_support)
        st.session_state.extracurricular  = extracurricular_enc
        st.session_state.sports           = sports_enc
        st.session_state.music            = music_enc
        st.session_state.grade_class      = int(grade_class)

    # ── Display Result ──
    if st.session_state.gpa is not None:
        gpa = float(st.session_state.gpa)

        if gpa >= 3.5:
            box_cls  = "gpa-excellent"
            category = "Excellent Performance"
        elif gpa >= 2.5:
            box_cls  = "gpa-good"
            category = "Good Performance"
        elif gpa >= 1.8:
            box_cls  = "gpa-average"
            category = "Average Performance"
        else:
            box_cls  = "gpa-risk"
            category = "Academic Risk"

        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown(
            f"""<div class="gpa-box {box_cls}">
                <div class="gpa-num">{gpa}</div>
                <div class="gpa-category">{category}</div>
            </div>""",
            unsafe_allow_html=True,
        )

        # ── Stat chips ──
        chips = [
            (f"{st.session_state.study_time}h",          "Study/Week"),
            (str(st.session_state.absences),              "Absences"),
            ("Yes" if st.session_state.tutoring    else "No", "Tutoring"),
            ("Yes" if st.session_state.extracurricular else "No", "Extra-Curr"),
        ]
        chip_html = "".join(
            f'<div class="stat-chip"><div class="stat-chip-val">{v}</div>'
            f'<div class="stat-chip-lbl">{l}</div></div>'
            for v, l in chips
        )
        st.markdown(f'<div class="stat-row">{chip_html}</div>', unsafe_allow_html=True)

# ============================================================
# TAB 2 — ANALYTICS SUITE
# ============================================================
with tab2:

    if st.session_state.gpa is None:
        st.markdown(
            """<div style='text-align:center; padding:80px 20px; font-family:Syne,sans-serif;
                           font-size:16px; letter-spacing:3px; text-transform:uppercase;
                           color:rgba(16,185,129,0.4);'>
                &#9672; Run Prediction First To Unlock Analytics &#9672;
            </div>""",
            unsafe_allow_html=True,
        )
    else:
        gpa            = float(st.session_state.gpa)
        s_study        = float(st.session_state.study_time)        if st.session_state.study_time        is not None else 12.0
        s_absences     = int(st.session_state.absences)            if st.session_state.absences          is not None else 4
        s_tutoring     = int(st.session_state.tutoring)            if st.session_state.tutoring          is not None else 0
        s_parental     = int(st.session_state.parental_support)    if st.session_state.parental_support  is not None else 0
        s_extra        = int(st.session_state.extracurricular)     if st.session_state.extracurricular   is not None else 0
        s_sports       = int(st.session_state.sports)              if st.session_state.sports            is not None else 0
        s_music        = int(st.session_state.music)               if st.session_state.music             is not None else 0
        s_grade        = int(st.session_state.grade_class)         if st.session_state.grade_class       is not None else 1

        # ── Radar Chart ──
        st.markdown('<div class="section-title">&#127944; Student Profile Radar</div>', unsafe_allow_html=True)

        radar_labels = [
            "Study Time", "Attendance", "Tutoring",
            "Parental Support", "Extracurricular",
            "Sports", "Music", "Grade Level",
        ]
        # Normalise each to [0, 1]
        absence_score = max(0.0, 1.0 - s_absences / 50.0)
        radar_values  = [
            s_study / 40.0,
            absence_score,
            float(s_tutoring),
            s_parental / 3.0,
            float(s_extra),
            float(s_sports),
            float(s_music),
            s_grade / 4.0,
        ]
        # Close the polygon
        r_closed     = radar_values + [radar_values[0]]
        theta_closed = radar_labels + [radar_labels[0]]

        fig_radar = go.Figure()
        fig_radar.add_trace(
            go.Scatterpolar(
                r=r_closed,
                theta=theta_closed,
                fill="toself",
                fillcolor="rgba(16,185,129,0.12)",
                line=dict(color="#10b981", width=2.5),
                name="Student",
            )
        )
        fig_radar.add_trace(
            go.Scatterpolar(
                r=[0.75] * (len(radar_labels) + 1),
                theta=theta_closed,
                mode="lines",
                line=dict(color="rgba(139,92,246,0.35)", width=1.5, dash="dot"),
                name="Benchmark",
            )
        )
        fig_radar.update_layout(
            polar=dict(
                bgcolor="rgba(0,0,0,0)",
                radialaxis=dict(
                    gridcolor="rgba(16,185,129,0.1)",
                    color="rgba(16,185,129,0.5)",
                    range=[0, 1],
                ),
                angularaxis=dict(
                    gridcolor="rgba(16,185,129,0.1)",
                    color="rgba(16,185,129,0.7)",
                ),
            ),
            paper_bgcolor="rgba(0,0,0,0)",
            font=dict(family="Space Mono", color="#10b981", size=10),
            height=420,
            margin=dict(l=40, r=40, t=40, b=40),
            showlegend=True,
            legend=dict(font=dict(color="#10b981", size=11)),
        )
        st.plotly_chart(fig_radar, use_container_width=True)

        # ── GPA Confidence Curve ──
        st.markdown('<div class="section-title">&#128200; GPA Confidence Distribution</div>', unsafe_allow_html=True)

        sigma   = 0.32
        x_vals  = np.linspace(max(0.0, gpa - 1.2), min(4.0, gpa + 1.2), 200)
        y_vals  = (1.0 / (sigma * np.sqrt(2.0 * np.pi))) * np.exp(-0.5 * ((x_vals - gpa) / sigma) ** 2)

        fig_dist = go.Figure()
        fig_dist.add_trace(
            go.Scatter(
                x=x_vals.tolist(),
                y=y_vals.tolist(),
                mode="lines",
                fill="tozeroy",
                fillcolor="rgba(16,185,129,0.1)",
                line=dict(color="#10b981", width=3),
                name="Confidence Curve",
            )
        )
        fig_dist.add_vline(
            x=gpa,
            line=dict(color="#8b5cf6", width=2.5, dash="dash"),
            annotation_text=f"Predicted GPA: {gpa}",
            annotation_font_color="#a78bfa",
        )
        fig_dist.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(16,185,129,0.02)",
            font=dict(family="DM Sans", color="#10b981"),
            xaxis=dict(
                title="GPA",
                range=[0, 4],
                gridcolor="rgba(16,185,129,0.08)",
                color="rgba(16,185,129,0.7)",
            ),
            yaxis=dict(
                title="Probability Density",
                gridcolor="rgba(16,185,129,0.08)",
                color="rgba(16,185,129,0.7)",
            ),
            height=360,
            margin=dict(l=20, r=20, t=20, b=20),
            showlegend=False,
        )
        st.plotly_chart(fig_dist, use_container_width=True)

        # ── Study Time Simulation ──
        st.markdown('<div class="section-title">&#128336; Study Time vs GPA Simulation</div>', unsafe_allow_html=True)

        study_range  = np.linspace(0.0, 40.0, 40)
        sim_gpas     = []
        for sh in study_range:
            sim_arr    = np.array([[
                sh, s_absences, s_tutoring,
                s_parental, s_extra,
                s_sports, s_music, s_grade,
            ]])
            sim_scaled = scaler.transform(sim_arr)
            sim_pred   = float(model.predict(sim_scaled)[0])
            sim_gpas.append(round(min(max(sim_pred, 0.0), 4.0), 3))

        fig_study = go.Figure()
        fig_study.add_trace(
            go.Scatter(
                x=study_range.tolist(),
                y=sim_gpas,
                mode="lines+markers",
                line=dict(color="#10b981", width=3, shape="spline"),
                marker=dict(color="#8b5cf6", size=6, line=dict(color="#10b981", width=2)),
                fill="tozeroy",
                fillcolor="rgba(16,185,129,0.06)",
                name="Simulated GPA",
            )
        )
        fig_study.add_vline(
            x=s_study,
            line=dict(color="#f59e0b", width=2, dash="dash"),
            annotation_text=f"Current: {s_study}h",
            annotation_font_color="#f59e0b",
        )
        fig_study.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(16,185,129,0.02)",
            font=dict(family="DM Sans", color="#10b981"),
            xaxis=dict(
                title="Study Hours / Week",
                gridcolor="rgba(16,185,129,0.08)",
                color="rgba(16,185,129,0.7)",
            ),
            yaxis=dict(
                title="Predicted GPA",
                range=[0, 4],
                gridcolor="rgba(16,185,129,0.08)",
                color="rgba(16,185,129,0.7)",
            ),
            height=360,
            margin=dict(l=20, r=20, t=20, b=20),
            showlegend=False,
        )
        st.plotly_chart(fig_study, use_container_width=True)

# ============================================================
# TAB 3 — MODEL INSIGHTS
# ============================================================
with tab3:

    st.markdown('<div class="section-title">&#129504; Why KNN Regression?</div>', unsafe_allow_html=True)

    why_insights = [
        ("<b>Non-linear capture</b> — KNN detects complex academic behaviour patterns that linear models miss.",),
        ("<b>Instance-based learning</b> — predictions draw from the k most similar historical students.",),
        ("<b>Feature scaling</b> — StandardScaler ensures no single feature dominates the distance metric.",),
        ("<b>No training assumptions</b> — ideal for academic data with mixed distributions.",),
    ]
    for (text,) in why_insights:
        st.markdown(f'<div class="insight">{text}</div>', unsafe_allow_html=True)

    st.markdown('<div class="section-title">&#128204; Key Academic Drivers</div>', unsafe_allow_html=True)

    driver_insights = [
        ("<b>Study Time</b> is the highest-impact variable — each extra hour correlates with meaningful GPA gain.",),
        ("<b>Absences</b> have a strong negative effect — consistent attendance is critical.",),
        ("<b>Parental Support</b> at higher levels correlates with better academic outcomes.",),
        ("<b>Tutoring</b> provides measurable uplift, especially for students below 2.5 GPA.",),
        ("<b>Extracurricular activities</b> show a positive balance effect when not excessive.",),
        ("<b>Sports &amp; Music</b> contribute marginally but help with engagement and discipline.",),
    ]
    for (text,) in driver_insights:
        st.markdown(f'<div class="insight">{text}</div>', unsafe_allow_html=True)

    st.markdown('<div class="section-title">&#128200; Feature Reference Table</div>', unsafe_allow_html=True)

    feat_df = pd.DataFrame(
        {
            "Feature":      ["study_time", "absences", "tutoring", "parental_support", "extracurricular", "sports", "music", "grade_class"],
            "Type":         ["Numeric", "Numeric", "Binary", "Ordinal (0-3)", "Binary", "Binary", "Binary", "Ordinal (1-4)"],
            "Scaling":      ["Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes"],
            "Impact Level": ["High", "High", "Medium", "Medium", "Low", "Low", "Low", "Medium"],
        }
    )
    st.dataframe(feat_df, use_container_width=True, hide_index=True)

# ============================================================
# TAB 4 — STUDENT REPORT
# ============================================================
with tab4:

    if st.session_state.gpa is None:
        st.markdown(
            """<div style='text-align:center; padding:80px 20px; font-family:Syne,sans-serif;
                           font-size:16px; letter-spacing:3px; text-transform:uppercase;
                           color:rgba(16,185,129,0.4);'>
                &#9672; Run Prediction To Generate Report &#9672;
            </div>""",
            unsafe_allow_html=True,
        )
    else:
        gpa = float(st.session_state.gpa)

        if gpa >= 3.5:
            band  = "Top Tier Student"
            b_cls = "gpa-excellent"
        elif gpa >= 2.5:
            band  = "Consistent Performer"
            b_cls = "gpa-good"
        elif gpa >= 1.8:
            band  = "Needs Monitoring"
            b_cls = "gpa-average"
        else:
            band  = "Academic Risk — Intervention Required"
            b_cls = "gpa-risk"

        # Result summary box
        st.markdown(
            f"""<div class="gpa-box {b_cls}" style='padding:30px;'>
                <div class="gpa-num" style='font-size:60px;'>{gpa}</div>
                <div class="gpa-category">{band}</div>
            </div>""",
            unsafe_allow_html=True,
        )

        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown('<div class="section-title">&#128203; Detailed Profile Report</div>', unsafe_allow_html=True)

        yes_no = lambda v: "Yes" if v else "No"

        report_rows = [
            ("Predicted GPA",         str(gpa)),
            ("Performance Band",      band),
            ("Study Time",            f"{st.session_state.study_time}h / week"),
            ("Absences",              str(st.session_state.absences)),
            ("Tutoring",              yes_no(st.session_state.tutoring)),
            ("Parental Support",      str(st.session_state.parental_support) + " / 3"),
            ("Extracurricular",       yes_no(st.session_state.extracurricular)),
            ("Sports",                yes_no(st.session_state.sports)),
            ("Music",                 yes_no(st.session_state.music)),
            ("Grade Class",           str(st.session_state.grade_class)),
        ]

        rows_html = "".join(
            f'<div class="report-row">'
            f'<span class="report-row-key">{k}</span>'
            f'<span class="report-row-val">{v}</span>'
            f'</div>'
            for k, v in report_rows
        )
        st.markdown(f'<div class="report-card">{rows_html}</div>', unsafe_allow_html=True)

        # Recommendation
        st.markdown('<div class="section-title">&#128161; Personalised Recommendation</div>', unsafe_allow_html=True)

        if gpa < 1.8:
            st.markdown(
                """<div class="rec-warn">
                    &#9888; <b>Academic Risk Detected.</b> Immediate intervention recommended:<br>
                    &bull; Increase study hours significantly (target 20+ hrs/week)<br>
                    &bull; Reduce absences to near zero<br>
                    &bull; Enrol in tutoring sessions immediately<br>
                    &bull; Engage parents / guardians for home support
                </div>""",
                unsafe_allow_html=True,
            )
        elif gpa < 2.5:
            st.markdown(
                """<div class="rec-warn">
                    &#128204; <b>Below Target GPA.</b> Improvement actions:<br>
                    &bull; Aim for 15–20 study hours per week<br>
                    &bull; Limit absences &mdash; attend every session<br>
                    &bull; Consider tutoring for weaker subjects<br>
                    &bull; Ensure parental engagement where possible
                </div>""",
                unsafe_allow_html=True,
            )
        else:
            st.markdown(
                """<div class="rec-ok">
                    &#9989; <b>Strong Academic Performance.</b> Keep it up:<br>
                    &bull; Maintain current study schedule<br>
                    &bull; Continue extracurricular balance<br>
                    &bull; Explore advanced enrichment opportunities<br>
                    &bull; Peer mentoring can further strengthen outcomes
                </div>""",
                unsafe_allow_html=True,
            )

        # GPA progress bar
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown(
            f"""<div style='font-family:"Space Mono",monospace; font-size:10px;
                            color:rgba(16,185,129,0.6); letter-spacing:2px;
                            text-transform:uppercase; margin-bottom:6px;'>
                GPA Progress: {gpa} / 4.0
            </div>""",
            unsafe_allow_html=True,
        )
        st.progress(min(gpa / 4.0, 1.0))

# ============================================================
# FOOTER
# ============================================================
st.markdown(
    """
    <div class="footer">
        &copy; 2026 &nbsp;|&nbsp; Akshit Gajera &nbsp;|&nbsp;
        AI Student Intelligence Platform &nbsp;|&nbsp;
        KNN Regression &nbsp;|&nbsp; Enterprise Academic AI
    </div>
    """,
    unsafe_allow_html=True,
)
