# NUST Zimbabwe — Degree Class Predictor
### Faculty of Applied Science | Streamlit Web Application

---

## How to Run (Step-by-Step)

### 1. Make sure Python is installed
You need Python 3.9 or later. Check with:
```
python --version
```

### 2. Install the required libraries
Open your terminal / command prompt in this folder and run:
```
pip install -r requirements.txt
```

### 3. Run the app
```
streamlit run app.py
```

The app will open automatically in your browser at `http://localhost:8501`

---

## What the App Does
- Covers 3 NUST FAS degree programmes: Computer Science, Applied Chemistry, Environmental Science & Health
- Student selects their programme and where their transcript currently ends
- Student enters marks for completed modules only
- Model analyses performance profile (theory vs mathematical/technical, semester trend)
- Generates 3 prediction scenarios: Pessimistic, Realistic, Optimistic
- Shows weighted aggregate calculation using official NUST regulations
- Outputs confidence level, radar chart, trajectory chart, and personalised insights

## Technologies Used
- Python 3.x
- Streamlit (GUI framework)
- Pandas (data handling)
- NumPy (calculations)
- Plotly (interactive charts)

## NUST Branding
Colours used are NUST Zimbabwe's official brand colours:
- Primary Navy: #003366
- Medium Blue: #0057A8
- Gold Accent: #C8971B

## Contributions
- Improved documentation by Nothando

---

*Built for Computational Modelling Course Group Project — NUST Faculty of Applied Science*
