"""
NUST Zimbabwe — Degree Class Predictor
Faculty of Applied Science
Streamlit GUI Application
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots

# ─────────────────────────────────────────────
# PAGE CONFIG
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="NUST Degree Class Predictor",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ─────────────────────────────────────────────
# NUST BRAND COLOURS
# ─────────────────────────────────────────────
NUST_NAVY    = "#001F54"   # Official NUST Deep Navy Blue
NUST_BLUE    = "#0057A8"   # NUST Medium Blue
NUST_GOLD    = "#FFD700"   # Official NUST Vibrant Crest Gold
NUST_LIGHT   = "#F4F7FA"   # Premium clean light background
NUST_WHITE   = "#FFFFFF"
NUST_DARK    = "#1A1A2E"
NUST_RED     = "#C0392B"   # For fail/warnings
NUST_GREEN   = "#1E8449"   # For first class

# ─────────────────────────────────────────────
# CUSTOM CSS — NUST BRANDING
# ─────────────────────────────────────────────
st.markdown(f"""
<style>
    /* ── Global ── */
    @import url('https://fonts.googleapis.com/css2?family=Georgia&family=Open+Sans:wght@400;600;700&display=swap');

    html, body, [class*="css"] {{
        font-family: 'Open Sans', sans-serif;
        background-color: {NUST_LIGHT};
    }}

    /* ── Sidebar ── */
    [data-testid="stSidebar"] {{
        background: linear-gradient(180deg, {NUST_NAVY} 0%, {NUST_BLUE} 100%);
        color: white;
    }}
    [data-testid="stSidebar"] * {{
        color: white !important;
    }}
    [data-testid="stSidebar"] .stSelectbox label,
    [data-testid="stSidebar"] .stRadio label,
    [data-testid="stSidebar"] p {{
        color: white !important;
        font-weight: 600;
    }}
    [data-testid="stSidebar"] hr {{
        border-color: {NUST_GOLD};
    }}

    /* ── Header Banner ── */
    .nust-header {{
        background: linear-gradient(135deg, {NUST_NAVY} 0%, {NUST_BLUE} 100%);
        padding: 24px 32px;
        border-bottom: 4px solid {NUST_GOLD};
        display: flex;
        align-items: center;
        gap: 20px;
        border-radius: 8px 8px 0 0;
        margin-bottom: 0;
    }}
    .nust-header-text h1 {{
        color: white;
        font-size: 26px;
        font-weight: 700;
        margin: 0;
        font-family: Georgia, serif;
    }}
    .nust-header-text p {{
        color: {NUST_GOLD};
        font-size: 13px;
        margin: 4px 0 0 0;
        letter-spacing: 1.5px;
        text-transform: uppercase;
    }}

    /* ── Cards ── */
    .nust-card {{
        background: white;
        border-radius: 6px;
        border-left: 5px solid {NUST_GOLD};
        padding: 20px 24px;
        margin: 12px 0;
        box-shadow: 0 2px 8px rgba(0,51,102,0.10);
    }}
    .nust-card h3 {{
        color: {NUST_NAVY};
        font-family: Georgia, serif;
        margin-top: 0;
        font-size: 17px;
    }}

    /* ── Section titles ── */
    .section-title {{
        color: {NUST_NAVY};
        font-family: Georgia, serif;
        font-size: 20px;
        font-weight: bold;
        border-bottom: 3px solid {NUST_GOLD};
        padding-bottom: 8px;
        margin: 24px 0 16px 0;
    }}

    /* ── Prediction badges ── */
    .class-badge {{
        display: inline-block;
        padding: 8px 20px;
        border-radius: 30px;
        font-weight: 700;
        font-size: 18px;
        text-align: center;
    }}
    .class-first   {{ background: {NUST_GREEN};  color: white; }}
    .class-upper   {{ background: {NUST_BLUE};   color: white; }}
    .class-lower   {{ background: #2E86AB;        color: white; }}
    .class-pass    {{ background: #E67E22;        color: white; }}
    .class-fail    {{ background: {NUST_RED};     color: white; }}

    /* ── Metric cards ── */
    .metric-box {{
        background: {NUST_NAVY};
        color: white;
        border-radius: 8px;
        padding: 16px;
        text-align: center;
        margin: 8px 0;
    }}
    .metric-box .metric-val {{
        font-size: 28px;
        font-weight: 700;
        color: {NUST_GOLD};
    }}
    .metric-box .metric-label {{
        font-size: 12px;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-top: 4px;
    }}

    /* ── Scenario rows ── */
    .scenario-pess {{ border-left: 5px solid {NUST_RED}  !important; }}
    .scenario-real {{ border-left: 5px solid {NUST_BLUE} !important; }}
    .scenario-opti {{ border-left: 5px solid {NUST_GREEN}!important; }}

    /* ── Input labels ── */
    label {{ color: {NUST_NAVY} !important; font-weight: 600; }}

    /* ── Primary buttons ── */
    .stButton > button {{
        background: linear-gradient(90deg, {NUST_NAVY}, {NUST_BLUE});
        color: white;
        border: none;
        border-radius: 6px;
        padding: 10px 28px;
        font-weight: 700;
        font-size: 15px;
        letter-spacing: 0.5px;
        transition: all 0.2s;
    }}
    .stButton > button:hover {{
        background: linear-gradient(90deg, {NUST_BLUE}, {NUST_GOLD});
        color: white;
        transform: translateY(-1px);
    }}

    /* ── Tabs ── */
    .stTabs [data-baseweb="tab-list"] {{
        background: {NUST_NAVY};
        border-radius: 6px 6px 0 0;
        gap: 2px;
    }}
    .stTabs [data-baseweb="tab"] {{
        color: rgba(255,255,255,0.7) !important;
        font-weight: 600;
    }}
    .stTabs [aria-selected="true"] {{
        background: {NUST_GOLD} !important;
        color: {NUST_NAVY} !important;
        border-radius: 4px;
    }}

    /* ── Footer ── */
    .nust-footer {{
        background: {NUST_NAVY};
        color: rgba(255,255,255,0.7);
        text-align: center;
        padding: 14px;
        font-size: 12px;
        border-radius: 0 0 8px 8px;
        margin-top: 32px;
    }}
    .nust-footer span {{ color: {NUST_GOLD}; font-weight: 700; }}
</style>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────
# MODULE DATA
# ─────────────────────────────────────────────

PROGRAMMES = {
    "BSc Honours Computer Science": "CS",
    "BSc Honours Applied Chemistry": "CHEM",
    "BSc Honours Environmental Science and Health": "ESH"
}

MODULES = {
    "CS": {
        "Part I": {
            "Semester 1": [
                ("SCS 1101", "Introduction to Computer Science & Programming", "PROG"),
                ("SCS 1102", "Mathematical Foundation of Computer Science", "MATH"),
                ("SCS 1103", "Computer Architecture", "THEORY"),
                ("SMA 1101", "Calculus I", "MATH"),
                ("SMA 1102", "Discrete Mathematics", "MATH"),
                ("PLC 1101", "Peace, Leadership & Conflict Transformation I", "THEORY"),
            ],
            "Semester 2": [
                ("SCS 1201", "Introduction to Operating Systems", "THEORY"),
                ("SCS 1202", "Digital Logic Design", "MIXED"),
                ("SCS 1203", "Visual Programming & GUI Development", "PROG"),
                ("SMA 1201", "Linear Mathematics", "MATH"),
                ("SORS 1201", "Probability Theory", "MATH"),
                ("PLC 1201", "Peace, Leadership & Conflict Transformation II", "THEORY"),
            ],
        },
        "Part II": {
            "Semester 1": [
                ("SCS 2101", "Systems Analysis and Design", "THEORY"),
                ("SCS 2102", "Database Systems & Design", "MIXED"),
                ("SCS 2103", "Data Structures and Algorithms", "MATH"),
                ("SCS 2104", "Data Communication & Computer Networks", "THEORY"),
                ("SCS 2105", "Object Oriented Programming I", "PROG"),
                ("SORS 2101", "Applied Statistics", "MATH"),
            ],
            "Semester 2": [
                ("SCS 2201", "Software Engineering", "THEORY"),
                ("SCS 2202", "Internet & Web Technologies", "PROG"),
                ("SCS 2203", "Computer Security", "THEORY"),
                ("SCS 2204", "Simulation and Modelling", "MATH"),
                ("SCS 2205", "Information Systems", "THEORY"),
                ("SCS 2206", "Mini Research Project", "MIXED"),
            ],
        },
        "Part III": {
            "Industrial Attachment": [
                ("SCS 3000", "Industrial Attachment (28 weeks)", "PRACTICAL"),
            ]
        },
        "Part IV": {
            "Semester 1": [
                ("SCS 4101", "Object Oriented Programming II", "PROG"),
                ("SCS 4102", "Advanced Databases", "MIXED"),
                ("SCS 4103", "Software Project Management", "THEORY"),
                ("SCS 4104", "Computer Graphics", "PROG"),
                ("SCS 4105", "Digital Signal Processing", "MATH"),
                ("SCS 4106", "Decision Support Systems", "THEORY"),
            ],
            "Semester 2": [
                ("SCS 4201", "Artificial Intelligence", "MATH"),
                ("SCS 4202", "Advanced Networks", "THEORY"),
                ("SCS 4203", "Management Information Systems", "THEORY"),
                ("SCS 4204", "Intellectual Property Rights", "THEORY"),
                ("SCS 4205", "Advanced Software Engineering", "THEORY"),
                ("SCS 4010", "Research Project (double-weighted)", "PROJECT"),
            ],
        },
    },
    "CHEM": {
        "Part I": {
            "Semester 1": [
                ("SCH 1101", "General Chemistry I", "MIXED"),
                ("SCH 1102", "Inorganic Chemistry I", "THEORY"),
                ("SMA 1101", "Calculus I", "MATH"),
                ("SPH 1101", "General Physics I", "MIXED"),
                ("SCS 1101", "Introduction to Computer Science & Programming", "PROG"),
                ("PLC 1101", "Peace, Leadership & Conflict Transformation I", "THEORY"),
            ],
            "Semester 2": [
                ("SCH 1201", "Organic Chemistry I", "THEORY"),
                ("SCH 1202", "Physical Chemistry I", "MATH"),
                ("SCH 1203", "Analytical Chemistry I", "MIXED"),
                ("SMA 1201", "Calculus II", "MATH"),
                ("SPH 1201", "General Physics II", "MIXED"),
                ("PLC 1201", "Peace, Leadership & Conflict Transformation II", "THEORY"),
            ],
        },
        "Part II": {
            "Semester 1": [
                ("SCH 2101", "Inorganic Chemistry II", "THEORY"),
                ("SCH 2102", "Organic Chemistry II", "THEORY"),
                ("SCH 2103", "Physical Chemistry II", "MATH"),
                ("SCH 2104", "Analytical Chemistry II", "MIXED"),
                ("SMA 2101", "Applied Mathematics for Chemistry", "MATH"),
                ("SORS 2101", "Applied Statistics", "MATH"),
            ],
            "Semester 2": [
                ("SCH 2201", "Inorganic Chemistry III", "THEORY"),
                ("SCH 2202", "Organic Chemistry III", "THEORY"),
                ("SCH 2203", "Physical Chemistry III (Thermodynamics)", "MATH"),
                ("SCH 2204", "Spectroscopy & Spectrometry", "MIXED"),
                ("SCH 2205", "Environmental Chemistry", "THEORY"),
                ("SCH 2206", "Industrial Chemistry", "THEORY"),
            ],
        },
        "Part III": {
            "Industrial Attachment": [
                ("SCH 3000", "Industrial Attachment (28 weeks)", "PRACTICAL"),
            ]
        },
        "Part IV": {
            "Semester 1": [
                ("SCH 4101", "Advanced Inorganic Chemistry", "THEORY"),
                ("SCH 4102", "Advanced Organic Chemistry", "THEORY"),
                ("SCH 4103", "Advanced Physical Chemistry", "MATH"),
                ("SCH 4104", "Advanced Analytical Chemistry", "MIXED"),
                ("SCH 4105", "Polymer Chemistry", "THEORY"),
                ("SCH 4106", "Medicinal Chemistry", "THEORY"),
            ],
            "Semester 2": [
                ("SCH 4201", "Industrial Waste Management & Green Chemistry", "THEORY"),
                ("SCH 4202", "Chemical Process Safety", "THEORY"),
                ("SCH 4203", "Biochemistry", "THEORY"),
                ("SCH 4204", "Food Chemistry", "THEORY"),
                ("SCH 4010", "Research Project (double-weighted)", "PROJECT"),
            ],
        },
    },
    "ESH": {
        "Part I": {
            "Semester 1": [
                ("ESH 1101", "Introduction to Environmental Science", "THEORY"),
                ("ESH 1102", "Patterns of Zimbabwe's Population", "THEORY"),
                ("ESH 1204", "Radiation and Pollution", "THEORY"),
                ("SCH 1217", "General Chemistry (Service)", "MIXED"),
                ("SMA 1112", "Preparatory Mathematics (Service)", "MATH"),
                ("PLC 1101", "Peace, Leadership & Conflict Transformation I", "THEORY"),
            ],
            "Semester 2": [
                ("ESH 1206", "Energy Resources Planning and Conservation", "THEORY"),
                ("ESH 1207", "Introduction to Ecology", "THEORY"),
                ("ESH 1211", "Environmental and Health Education", "THEORY"),
                ("SBB 1207", "General Microbiology (Service)", "THEORY"),
                ("SCS 1101", "Information Technology & Computer Applications", "PROG"),
                ("PLC 1201", "Peace, Leadership & Conflict Transformation II", "THEORY"),
            ],
        },
        "Part II": {
            "Semester 1": [
                ("ESH 2101", "Introduction to Fresh Water Environment", "THEORY"),
                ("ESH 2103", "Principles of Sociology and Psychology", "THEORY"),
                ("ESH 2108", "Environmental Economics", "MIXED"),
                ("ESH 2111", "Disease Prevention and Control", "THEORY"),
                ("ESH 2208", "Occupational Health and Safety", "THEORY"),
                ("ESH 2113", "Water Supply and Sanitation", "MIXED"),
            ],
            "Semester 2": [
                ("ESH 2203", "Management of Solid and Hazardous Waste", "THEORY"),
                ("ESH 2205", "Environmental Management Systems", "THEORY"),
                ("ESH 2211", "Research Methodology", "MIXED"),
                ("ESH 2213", "Food Hygiene", "THEORY"),
                ("ESH 2214", "Principles of Ecotoxicology", "THEORY"),
                ("SORS 2210", "Applied Statistics for Biological Sciences (Service)", "MATH"),
            ],
        },
        "Part III": {
            "Industrial Attachment": [
                ("ESH 3000", "Industrial Attachment (28 weeks)", "PRACTICAL"),
            ]
        },
        "Part IV": {
            "Semester 1": [
                ("ESH 4101", "Air Quality Management", "THEORY"),
                ("ESH 4102", "Environmental Law and Government Policy", "THEORY"),
                ("ESH 4103", "Environmental Impact Assessment", "MIXED"),
                ("ESH 4105", "GIS and Remote Sensing in Natural Resources", "MIXED"),
                ("ESH 4106", "Climate Change and Adaptation", "THEORY"),
                ("ESH 4107", "Community Health Promotion", "THEORY"),
            ],
            "Semester 2": [
                ("ESH 4120", "Integrated Waste Management", "THEORY"),
                ("ESH 4121", "Public Health Administration", "THEORY"),
                ("ESH 4122", "Environmental Auditing", "MIXED"),
                ("ESH 4123", "Occupational Toxicology", "THEORY"),
                ("ESH 4010", "Research Project (double-weighted)", "PROJECT"),
            ],
        },
    },
}

TRANSCRIPT_OPTIONS = [
    "End of Part I Semester 1",
    "End of Part I Semester 2",
    "End of Part II Semester 1",
    "End of Part II Semester 2",
    "Completed Part III (Industrial Attachment)",
    "End of Part IV Semester 1",
    "End of Part IV Semester 2 (All complete)",
]


# ─────────────────────────────────────────────
# HELPER FUNCTIONS
# ─────────────────────────────────────────────

def get_class_label(mark):
    if mark >= 75: return "First Class 🏆"
    elif mark >= 65: return "Upper Second (2.1) 🥈"
    elif mark >= 60: return "Lower Second (2.2) 🥉"
    elif mark >= 50: return "Pass"
    else: return "Fail ❌"

def get_class_color(mark):
    if mark >= 75: return NUST_GREEN
    elif mark >= 65: return NUST_BLUE
    elif mark >= 60: return "#2E86AB"
    elif mark >= 50: return "#E67E22"
    else: return NUST_RED

def get_class_badge_css(mark):
    if mark >= 75: return "class-first"
    elif mark >= 65: return "class-upper"
    elif mark >= 60: return "class-lower"
    elif mark >= 50: return "class-pass"
    else: return "class-fail"

def modules_up_to(prog_code, transcript_end):
    """Returns list of (part, semester, code, name, type) up to transcript end."""
    order = {
        "End of Part I Semester 1": ("Part I", "Semester 1"),
        "End of Part I Semester 2": ("Part I", "Semester 2"),
        "End of Part II Semester 1": ("Part II", "Semester 1"),
        "End of Part II Semester 2": ("Part II", "Semester 2"),
        "Completed Part III (Industrial Attachment)": ("Part III", "Industrial Attachment"),
        "End of Part IV Semester 1": ("Part IV", "Semester 1"),
        "End of Part IV Semester 2 (All complete)": ("Part IV", "Semester 2"),
    }
    stop_part, stop_sem = order[transcript_end]
    part_order = ["Part I", "Part II", "Part III", "Part IV"]
    result = []
    for part in part_order:
        if part not in MODULES[prog_code]: continue
        for sem, mods in MODULES[prog_code][part].items():
            result.append((part, sem, mods))
            if part == stop_part and sem == stop_sem:
                return result
    return result

def remaining_modules(prog_code, transcript_end):
    """Returns modules NOT yet completed."""
    done_parts_sems = {(p, s) for p, s, _ in modules_up_to(prog_code, transcript_end)}
    result = []
    for part in ["Part I", "Part II", "Part III", "Part IV"]:
        if part not in MODULES[prog_code]: continue
        for sem, mods in MODULES[prog_code][part].items():
            if (part, sem) not in done_parts_sems:
                result.append((part, sem, mods))
    return result

def analyse_profile(marks_dict):
    """Returns avg_theory, avg_math_prog, trajectory, overall_avg."""
    theory_marks, math_marks = [], []
    sem_avgs = {}
    for key, mark in marks_dict.items():
        part, sem, code, mtype = key
        if mtype in ("THEORY",): theory_marks.append(mark)
        elif mtype in ("MATH", "PROG", "MIXED"): math_marks.append(mark)
        sem_key = f"{part} | {sem}"
        sem_avgs.setdefault(sem_key, []).append(mark)

    avg_theory = np.mean(theory_marks) if theory_marks else 0
    avg_math = np.mean(math_marks) if math_marks else 0
    overall = np.mean(list(marks_dict.values())) if marks_dict else 0

    # Trajectory
    sem_order = list(sem_avgs.keys())
    sem_means = [np.mean(sem_avgs[k]) for k in sem_order]
    if len(sem_means) >= 2:
        diffs = [sem_means[i+1] - sem_means[i] for i in range(len(sem_means)-1)]
        avg_diff = np.mean(diffs)
        std_val = np.std(sem_means)
        if std_val > 10: trajectory = "VOLATILE"
        elif avg_diff > 3: trajectory = "IMPROVING"
        elif avg_diff < -3: trajectory = "DECLINING"
        elif overall >= 65: trajectory = "STABLE_HIGH"
        else: trajectory = "STABLE_MID"
    else:
        trajectory = "STABLE_MID"

    # Strength
    diff = avg_theory - avg_math
    if diff > 5: strength = "THEORY_STRONG"
    elif diff < -5: strength = "TECH_STRONG"
    else: strength = "BALANCED"

    return {
        "avg_theory": avg_theory,
        "avg_math": avg_math,
        "overall": overall,
        "trajectory": trajectory,
        "strength": strength,
        "sem_avgs": {k: np.mean(v) for k, v in sem_avgs.items()},
    }

def project_mark(base_avg, mtype, scenario, profile):
    """Project a single module mark based on scenario."""
    strength = profile["strength"]
    traj = profile["trajectory"]

    if scenario == "pessimistic":
        base = base_avg - 8
        if traj == "DECLINING": base -= 3
        if strength == "THEORY_STRONG" and mtype in ("MATH", "PROG"): base -= 5
        if strength == "TECH_STRONG" and mtype == "THEORY": base -= 3
        return max(50, base)

    elif scenario == "realistic":
        if strength == "THEORY_STRONG":
            adj = 2 if mtype == "THEORY" else -3
        elif strength == "TECH_STRONG":
            adj = 2 if mtype in ("MATH", "PROG") else -3
        else:
            adj = 0
        traj_adj = 3 if traj == "IMPROVING" else (-3 if traj == "DECLINING" else 0)
        return min(85, max(50, base_avg + adj + traj_adj))

    else:  # optimistic
        base = base_avg + 8
        if traj == "IMPROVING": base += 4
        return min(85, max(50, base))

def ia_mark(scenario, profile):
    if scenario == "pessimistic": return 65
    elif scenario == "realistic": return 78
    else: return 85

def project_mark_scenario(scenario, module_mark_scenario):
    return module_mark_scenario

def compute_weighted_aggregate(part2_avg, ia, part4_avg):
    return (part2_avg * 0.30) + (ia * 0.20) + (part4_avg * 0.50)

def compute_confidence(marks_dict, transcript_end):
    base = 50
    if "Part II" in transcript_end and "Semester 2" in transcript_end: base += 15
    if "Part IV" in transcript_end and "Semester 1" in transcript_end: base += 20
    if "All complete" in transcript_end: base += 25
    if "Part I" in transcript_end: base -= 20

    profile = analyse_profile(marks_dict)
    traj = profile["trajectory"]
    if traj in ("STABLE_HIGH", "STABLE_MID"): base += 10
    elif traj == "VOLATILE": base -= 10
    if traj == "IMPROVING": base += 8
    elif traj == "DECLINING": base -= 8

    # fail penalty
    for key, mark in marks_dict.items():
        if mark < 50: base -= 5

    if "Part III" in transcript_end: base += 10
    return min(92, max(30, base))


def run_prediction(prog_code, transcript_end, marks_dict, ia_actual=None):
    from models import StudentProfile, TranscriptEntry
    from data import get_programme
    from engine import PredictionEngine

    prog = get_programme(prog_code)
    
    end_map = {
        "End of Part I Semester 1": ("I", 1),
        "End of Part I Semester 2": ("I", 2),
        "End of Part II Semester 1": ("II", 1),
        "End of Part II Semester 2": ("II", 2),
        "Completed Part III (Industrial Attachment)": ("III", None),
        "End of Part IV Semester 1": ("IV", 1),
        "End of Part IV Semester 2 (All complete)": ("IV", 2),
    }
    end_part, end_sem = end_map[transcript_end]
    
    profile = StudentProfile(prog, current_part=end_part, transcript_end_part=end_part, transcript_end_semester=end_sem)
    
    module_map = {mod.code: mod for mod in prog.modules}
    for (part_str, sem_str, code, mtype), mark in marks_dict.items():
        if code in module_map:
            profile.transcript.append(TranscriptEntry(module_map[code], float(mark)))
            
    if ia_actual is not None:
        for mod in prog.modules:
            if mod.type == 'PRACTICAL':
                if not any(e.module.code == mod.code for e in profile.transcript):
                    profile.transcript.append(TranscriptEntry(mod, float(ia_actual)))
                else:
                    for e in profile.transcript:
                        if e.module.code == mod.code:
                            e.mark = float(ia_actual)
                break

    engine = PredictionEngine(profile)
    results_full = engine.run_full_analysis(ia_actual=ia_actual)
    
    results = {
        "pessimistic": results_full['predictions']['Pessimistic'],
        "realistic": results_full['predictions']['Realistic'],
        "optimistic": results_full['predictions']['Optimistic'],
    }
    
    return results, results_full['profile'], results_full['confidence']


# ─────────────────────────────────────────────
# SIDEBAR
# ─────────────────────────────────────────────
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

with st.sidebar:
    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 4, 1])
    with col2:
        st.image(os.path.join(SCRIPT_DIR, "nust_crest.png"), use_container_width=True)
    st.markdown("""
    <div style='text-align:center; padding-bottom: 12px;'>
        <div style='font-size:18px; font-weight:700; font-family:Georgia;'>NUST</div>
        <div style='font-size:11px; letter-spacing:2px; opacity:0.8;'>ZIMBABWE</div>
    </div>
    <hr/>
    """, unsafe_allow_html=True)

    st.markdown("**Faculty of Applied Science**")
    st.markdown("*Degree Class Predictor*")
    st.markdown("---")
    st.markdown("**📋 Navigation**")

    page = st.radio(
        "Go to:",
        ["🏠 Home", "📊 Predict My Class", "📖 About the Model"],
        label_visibility="collapsed"
    )

    st.markdown("---")
    st.markdown("""
    <div style='font-size:11px; opacity:0.7; line-height:1.6;'>
    Based on NUST Academic Regulations<br>
    & FAS Yearbook 2023–2024<br><br>
    ⚠️ This is a predictor, not an official NUST result.
    </div>
    """, unsafe_allow_html=True)


# ─────────────────────────────────────────────
# HEADER BANNER
# ─────────────────────────────────────────────
col_logo1, col_logo2, col_logo3 = st.columns([1, 2, 1])
with col_logo2:
    st.image(os.path.join(SCRIPT_DIR, "nust_logo_banner.png"), use_container_width=True)

st.markdown(f"""
<div class="nust-header" style="border-radius: 8px; margin-top: 16px; justify-content: center; text-align: center;">
    <div class="nust-header-text">
        <h1 style="font-size: 28px;">Faculty of Applied Science</h1>
        <p style="font-size: 14px;">Degree Class Predictor & Academic Trajectory Forecaster</p>
    </div>
</div>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────
# PAGE: HOME
# ─────────────────────────────────────────────
if page == "🏠 Home":
    st.markdown("")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f"""
        <div class="nust-card">
            <h3>🖥️ Computer Science</h3>
            <p>BSc Honours in Computer Science — 36 taught modules across Parts I–IV plus 28 weeks Industrial Attachment.</p>
        </div>""", unsafe_allow_html=True)
    with col2:
        st.markdown(f"""
        <div class="nust-card">
            <h3>⚗️ Applied Chemistry</h3>
            <p>BSc Honours in Applied Chemistry — theory, laboratory and project work across four years of study.</p>
        </div>""", unsafe_allow_html=True)
    with col3:
        st.markdown(f"""
        <div class="nust-card">
            <h3>🌿 Environmental Science & Health</h3>
            <p>BSc Honours in Environmental Science and Health — interdisciplinary science covering environment, public health and policy.</p>
        </div>""", unsafe_allow_html=True)

    st.markdown('<div class="section-title">How It Works</div>', unsafe_allow_html=True)
    steps = [
        ("1️⃣", "Select your degree programme"),
        ("2️⃣", "Tell us where your transcript currently ends"),
        ("3️⃣", "Enter your marks for completed modules only"),
        ("4️⃣", "The model analyses your profile and generates 3 degree class scenarios"),
        ("5️⃣", "Get personalised insights and a confidence rating"),
    ]
    for icon, step in steps:
        st.markdown(f"""
        <div class="nust-card" style="padding:14px 20px; margin:6px 0;">
            <strong>{icon} {step}</strong>
        </div>""", unsafe_allow_html=True)

    st.markdown('<div class="section-title">NUST Degree Classification</div>', unsafe_allow_html=True)
    df = pd.DataFrame({
        "Mark Range": ["75% and above", "65% – 74%", "60% – 64%", "50% – 59%", "Below 50%"],
        "Classification": ["First Class", "Upper Second (2.1)", "Lower Second (2.2)", "Pass", "Fail"],
        "Division": ["1", "2.1", "2.2", "P", "F"],
    })
    st.dataframe(df, use_container_width=True, hide_index=True)

    st.markdown("""
    <div class="nust-card">
        <h3>⚖️ Part Weighting</h3>
        <p><strong>Part I</strong> — Gateway only. Does NOT count toward degree class.<br>
        <strong>Part II (Year 2)</strong> — 30% of weighted aggregate<br>
        <strong>Part III (Industrial Attachment)</strong> — 20% of weighted aggregate<br>
        <strong>Part IV (Year 4, including Research Project)</strong> — 50% of weighted aggregate</p>
    </div>""", unsafe_allow_html=True)


# ─────────────────────────────────────────────
# PAGE: PREDICT
# ─────────────────────────────────────────────
elif page == "📊 Predict My Class":
    st.markdown('<div class="section-title">Step 1 — Your Programme & Standing</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        prog_name = st.selectbox("Select Your Degree Programme", list(PROGRAMMES.keys()))
    with col2:
        transcript_end = st.selectbox(
            "Where does your current transcript end?",
            TRANSCRIPT_OPTIONS
        )

    prog_code = PROGRAMMES[prog_name]

    # IA override
    ia_actual = None
    if "Part III" in transcript_end or "Part IV" in transcript_end:
        col_ia1, col_ia2 = st.columns([1, 2])
        with col_ia1:
            ia_known = st.checkbox("I have my Industrial Attachment mark")
        if ia_known:
            with col_ia2:
                ia_actual = st.number_input("Industrial Attachment Mark (%)", 0, 100, 78, key="ia_val")

    # ─── Mark Entry ───
    st.markdown('<div class="section-title">Step 2 — Enter Your Module Marks</div>', unsafe_allow_html=True)
    st.info("💡 Enter your marks for all modules on your transcript. Part I is collected for trend analysis only and does NOT count toward your degree class.")

    completed = modules_up_to(prog_code, transcript_end)
    marks_dict = {}

    for part, sem, mods in completed:
        if part == "Part III":
            continue  # handled via IA override

        with st.expander(f"📂 {part} — {sem}", expanded=(part == "Part II")):
            cols = st.columns(2)
            for i, (code, name, mtype) in enumerate(mods):
                tag_color = {"PROG": "#2980B9", "MATH": "#8E44AD", "THEORY": "#27AE60", "MIXED": "#E67E22", "PROJECT": NUST_GOLD}
                tag = f'<span style="background:{tag_color.get(mtype, NUST_NAVY)};color:white;padding:2px 8px;border-radius:12px;font-size:11px;">{mtype}</span>'
                with cols[i % 2]:
                    st.markdown(f"**{code}** {tag}", unsafe_allow_html=True)
                    mark = st.number_input(
                        name,
                        min_value=0, max_value=100, value=60,
                        key=f"{part}_{sem}_{code}",
                        help=f"{code} — {mtype}"
                    )
                    marks_dict[(part, sem, code, mtype)] = mark

    # ─── Run Prediction ───
    st.markdown("")
    if st.button("🔮 Generate Degree Class Prediction", use_container_width=True):
        if not marks_dict:
            st.error("Please enter at least some module marks first.")
        else:
            results, profile, confidence = run_prediction(prog_code, transcript_end, marks_dict, ia_actual)

            st.markdown('<div class="section-title">📊 Your Academic Profile</div>', unsafe_allow_html=True)

            c1, c2, c3, c4 = st.columns(4)
            metrics = [
                (c1, f"{profile['overall']:.1f}%", "Overall Average"),
                (c2, f"{profile['avg_theory']:.1f}%", "Theory Average"),
                (c3, f"{profile['avg_math']:.1f}%", "Math / Technical"),
                (c4, profile["strength"].replace("_", " ").title(), "Strength Profile"),
            ]
            for col, val, label in metrics:
                with col:
                    st.markdown(f"""
                    <div class="metric-box">
                        <div class="metric-val">{val}</div>
                        <div class="metric-label">{label}</div>
                    </div>""", unsafe_allow_html=True)

            traj_map = {
                "IMPROVING": ("📈 Improving", NUST_GREEN),
                "DECLINING": ("📉 Declining", NUST_RED),
                "STABLE_HIGH": ("✅ Stable (High)", NUST_BLUE),
                "STABLE_MID": ("➡️ Stable (Mid)", "#E67E22"),
                "VOLATILE": ("⚡ Volatile", "#8E44AD"),
            }
            traj_label, traj_color = traj_map.get(profile["trajectory"], ("Unknown", NUST_NAVY))
            st.markdown(f"""
            <div style="background:{traj_color};color:white;border-radius:6px;padding:12px 20px;margin:12px 0;font-weight:700;">
                Semester Trajectory: {traj_label}
            </div>""", unsafe_allow_html=True)

            # Semester avg chart
            if len(profile["sem_avgs"]) > 1:
                fig_traj = go.Figure()
                sems = list(profile["sem_avgs"].keys())
                avgs = list(profile["sem_avgs"].values())
                fig_traj.add_trace(go.Scatter(
                    x=sems, y=avgs,
                    mode="lines+markers",
                    line=dict(color=NUST_GOLD, width=3),
                    marker=dict(size=10, color=NUST_NAVY),
                    name="Semester Average"
                ))
                fig_traj.add_hline(y=75, line_dash="dash", line_color=NUST_GREEN, annotation_text="First Class (75%)")
                fig_traj.add_hline(y=65, line_dash="dash", line_color=NUST_BLUE, annotation_text="2.1 (65%)")
                fig_traj.add_hline(y=60, line_dash="dash", line_color="#2E86AB", annotation_text="2.2 (60%)")
                fig_traj.update_layout(
                    title="Your Semester-by-Semester Performance",
                    plot_bgcolor=NUST_LIGHT,
                    paper_bgcolor="white",
                    yaxis=dict(range=[40, 100], title="Average Mark (%)"),
                    xaxis_title="Semester",
                    font=dict(family="Open Sans"),
                    margin=dict(t=50, b=40),
                )
                st.plotly_chart(fig_traj, use_container_width=True)

            # ─── Predictions Table ───
            st.markdown('<div class="section-title">🎯 Degree Class Predictions</div>', unsafe_allow_html=True)

            scenario_labels = {
                "pessimistic": ("🔴 Pessimistic", "scenario-pess"),
                "realistic": ("🟡 Realistic", "scenario-real"),
                "optimistic": ("🟢 Optimistic", "scenario-opti"),
            }

            for sc, (label, card_class) in scenario_labels.items():
                r = results[sc]
                cls_badge = get_class_badge_css(r["weighted"])
                st.markdown(f"""
                <div class="nust-card {card_class}" style="margin:10px 0;">
                    <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:12px;">
                        <div>
                            <strong style="font-size:17px;">{label}</strong><br>
                            <span style="color:#555;font-size:13px;">
                                Part II Avg: <b>{r['part2_avg']}%</b> &nbsp;|&nbsp;
                                IA: <b>{r['ia']}%</b> &nbsp;|&nbsp;
                                Part IV Avg: <b>{r['part4_avg']}%</b> &nbsp;|&nbsp;
                                <b>Weighted: {r['weighted']}%</b>
                            </span>
                        </div>
                        <div>
                            <span class="class-badge {cls_badge}">{r['class']}</span>
                        </div>
                    </div>
                </div>""", unsafe_allow_html=True)

            # Confidence
            conf_color = NUST_GREEN if confidence >= 70 else (NUST_GOLD if confidence >= 50 else NUST_RED)
            st.markdown(f"""
            <div style="background:{conf_color};color:white;border-radius:8px;padding:14px 22px;text-align:center;margin:16px 0;">
                <span style="font-size:22px;font-weight:700;">Realistic Scenario Confidence: {confidence}%</span><br>
                <span style="font-size:13px;opacity:0.9;">
                    {"High confidence — significant transcript data available." if confidence >= 70
                     else ("Moderate confidence — more modules will improve accuracy." if confidence >= 50
                     else "Low confidence — limited data. Prediction is indicative only.")}
                </span>
            </div>""", unsafe_allow_html=True)

            # Radar chart
            categories = ["Theory Modules", "Math/Technical", "Overall", "Part II Potential", "Part IV Potential"]
            fig_radar = go.Figure()
            for sc, color in [("pessimistic", NUST_RED), ("realistic", NUST_BLUE), ("optimistic", NUST_GREEN)]:
                r = results[sc]
                fig_radar.add_trace(go.Scatterpolar(
                    r=[profile["avg_theory"], profile["avg_math"], profile["overall"], r["part2_avg"], r["part4_avg"]],
                    theta=categories,
                    fill="toself",
                    name=sc.title(),
                    line_color=color,
                    fillcolor=color,
                    opacity=0.2,
                ))
            fig_radar.update_layout(
                polar=dict(radialaxis=dict(visible=True, range=[40, 90])),
                title="Academic Profile Radar",
                paper_bgcolor="white",
                font=dict(family="Open Sans"),
                margin=dict(t=60, b=40),
            )
            st.plotly_chart(fig_radar, use_container_width=True)

            # ─── Insights ───
            st.markdown('<div class="section-title">💡 Key Insights & Recommendations</div>', unsafe_allow_html=True)

            insights = []
            real = results["realistic"]

            if real["weighted"] >= 75:
                insights.append(f"🏆 You are on track for a **First Class** degree. Maintain your current performance through Part IV.")
            elif real["weighted"] >= 65:
                insights.append(f"🎯 You are predicted a **Upper Second (2.1)**. A strong Part IV could push you to a First Class — you need Part IV avg ≥ {round((75 - real['part2_avg']*0.3 - real['ia']*0.2) / 0.5, 1)}% to achieve that.")
            elif real["weighted"] >= 60:
                insights.append(f"📌 You are predicted a **Lower Second (2.2)**. Improving your Part IV average to ~{round((65 - real['part2_avg']*0.3 - real['ia']*0.2) / 0.5, 1)}% would move you to a 2.1.")

            if profile["trajectory"] == "IMPROVING":
                insights.append("📈 Your semester averages are **improving** — this is an excellent sign. The optimistic scenario may well be your reality.")
            elif profile["trajectory"] == "DECLINING":
                insights.append("⚠️ Your performance appears to be **declining** across semesters. Reflect on what changed and seek academic support if needed.")

            if profile["strength"] == "THEORY_STRONG":
                insights.append("📚 You perform significantly better in **theory-based modules**. Be prepared for mathematical and programming-heavy modules in Part IV.")
            elif profile["strength"] == "TECH_STRONG":
                insights.append("💻 You perform better in **technical/mathematical modules**. Your Research Project could be a major strength — invest time in it early.")

            insights.append(f"🔬 The **Research Project (double-weighted)** in Part IV is the single most impactful module. A strong project can swing your final aggregate by 3–5 marks.")
            insights.append(f"🏭 Industrial Attachment carries **20%** of your final mark. With ~90% of NUST students achieving distinctions, this is likely to be a positive contribution.")

            for ins in insights:
                st.markdown(f"""
                <div class="nust-card" style="padding:12px 18px; margin:6px 0;">
                    {ins}
                </div>""", unsafe_allow_html=True)

            # What would it take?
            st.markdown('<div class="section-title">🔄 What Would It Take to Change Class?</div>', unsafe_allow_html=True)
            real_ia = ia_actual if ia_actual else 78
            for target_mark, target_label in [(75, "First Class"), (65, "Upper Second (2.1)"), (60, "Lower Second (2.2)")]:
                needed_p4 = (target_mark - real["part2_avg"] * 0.30 - real_ia * 0.20) / 0.50
                if 50 <= needed_p4 <= 100:
                    gap = round(needed_p4 - profile["overall"], 1)
                    feasibility = "✅ Realistic" if gap <= 5 else ("⚠️ Challenging" if gap <= 12 else "❌ Very Difficult")
                    st.markdown(f"""
                    <div class="nust-card" style="padding:12px 18px; margin:6px 0;">
                        <strong>To achieve {target_label}:</strong> you need a Part IV average of 
                        <strong>{round(needed_p4, 1)}%</strong> 
                        (that's {'+' if gap >= 0 else ''}{gap}% vs your current avg) — {feasibility}
                    </div>""", unsafe_allow_html=True)

            st.markdown(f"""
            <div class="nust-footer">
                <span>NUST</span> Zimbabwe — Faculty of Applied Science &nbsp;|&nbsp;
                Degree Class Predictor &nbsp;|&nbsp;
                Based on NUST Academic Regulations & FAS Yearbook 2023–2024 &nbsp;|&nbsp;
                ⚠️ This tool is for guidance only and does not constitute an official NUST result.
            </div>""", unsafe_allow_html=True)


# ─────────────────────────────────────────────
# PAGE: ABOUT
# ─────────────────────────────────────────────
elif page == "📖 About the Model":
    st.markdown('<div class="section-title">About This Model</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="nust-card">
        <h3>What this model does</h3>
        <p>This predictor takes a student's existing module marks from their NUST transcript and generates three
        probabilistic forecasts of their final degree classification: Pessimistic, Realistic, and Optimistic.
        Each scenario applies different assumptions about how the student will perform in remaining modules,
        based on their performance pattern, subject strength profile, and semester trajectory.</p>
    </div>

    <div class="nust-card">
        <h3>Regulations used</h3>
        <p>The model is built on official NUST Academic Regulations and the Faculty of Applied Science Yearbook 2023–2024.
        It uses the official grading scheme (75%+ = First, 65–74% = 2.1, 60–64% = 2.2, 50–59% = Pass)
        and the official part weighting: <strong>Part II (30%) + Industrial Attachment (20%) + Part IV (50%)</strong>.
        Part I marks are used only for trend analysis and do not contribute to the weighted aggregate.</p>
    </div>

    <div class="nust-card">
        <h3>Programmes covered</h3>
        <ul>
            <li>BSc Honours Computer Science</li>
            <li>BSc Honours Applied Chemistry</li>
            <li>BSc Honours Environmental Science and Health</li>
        </ul>
    </div>

    <div class="nust-card">
        <h3>Key modelling assumptions</h3>
        <ul>
            <li>Approximately 90% of NUST students achieve a Distinction (75%+) on Industrial Attachment — the realistic scenario assumes 78%.</li>
            <li>The Research Project is double-weighted within Part IV and modelled separately from taught modules.</li>
            <li>Module types (THEORY, MATH, PROG, MIXED) are used to adjust projections based on each student's strength profile.</li>
            <li>Semester trends (improving, declining, stable, volatile) apply adjustments to projected marks.</li>
        </ul>
    </div>

    <div class="nust-card">
        <h3>Limitations</h3>
        <p>This is a computational model built for educational purposes. It does not have access to official NUST systems,
        continuous assessment breakdowns, or exam marks separately. It is a forecast tool — not an official result.
        Always consult your faculty for official academic standing.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="nust-footer">
        <span>NUST</span> Zimbabwe — Faculty of Applied Science &nbsp;|&nbsp;
        Degree Class Predictor &nbsp;|&nbsp;
        Computational Modelling Project
    </div>""", unsafe_allow_html=True)
