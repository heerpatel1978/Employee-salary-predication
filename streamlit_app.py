import streamlit as st
import importlib.util
import os

# Define path to predict.py
predict_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src', 'predict.py'))

# Load the module manually
spec = importlib.util.spec_from_file_location("predict", predict_path)
predict_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(predict_module)

# Access the predict_salary function
predict_salary = predict_module.predict_salary


# Page config
st.set_page_config(page_title="Employee Salary Predictor", page_icon="💼", layout="wide")

import streamlit as st

# Background and global text color
st.markdown("""
<style>
/* Background and general text color */
[data-testid="stAppViewContainer"] {
    background-image: url("https://images.unsplash.com/photo-1521791136064-7986c2920216");  
    background-size: cover;
    color: #000 !important;
}
[data-testid="stAppViewContainer"] * {
    color: #000 !important;
}
[data-testid="stAppViewContainer"]::before {
    content: "";
    position: fixed;
    top: 0; left: 0;
    width: 100vw; height: 100vh;
    background: rgba(255,255,255,0.5); /* Makes background lighter */
    z-index: 0;
    pointer-events: none;
}

/* Employee Name text input */
[data-testid="stTextInput"] input {
    background: #fff !important;
    color: #000 !important;
    border-radius: 5px;
}

/* Selectbox main visible area */
div[data-baseweb="select"] > div {
    background-color: #fff !important;
    color: #000 !important;
    border-radius: 6px !important;
    border: 1px solid #aaa !important;
}

/* Dropdown menu when open */
ul[role="listbox"] {
    background-color: #fff !important;
    color: #000 !important;
    border-radius: 6px !important;
}

/* Dropdown list items */
ul[role="listbox"] li {
    color: #000 !important;
    background-color: #fff !important;
}

/* Search input (if used in dropdown) */
[data-testid="stSelectbox"] input {
    background-color: #fff !important;
    color: #000 !important;
}

/* Button: white background, black text */
button[kind="secondary"], button[title="Predict Salary 💰"], button[tabindex="0"] {
    background-color: #fff !important;
    color: #000 !important;
    border-radius: 5px;
    border: 1px solid #000 !important;
    font-weight: 600;
}
</style>
""", unsafe_allow_html=True)

# Title and header
st.title("💼 Employee Salary Predictor")
st.markdown("Predict salaries with machine learning! Fill in the details below 👇")

# Input fields
name = st.text_input("Employee Name")
age = st.slider("Age", 18, 65, 30)
education = st.selectbox("Education Level", ["High School", "Bachelor’s", "Master’s", "PhD"])
occupation = st.selectbox("Occupation", ["Tech", "Sales", "Executive", "Admin"])
hours_per_week = st.slider("Hours Worked per Week", 20, 80, 40)

# Button and prediction
if st.button("Predict Salary 💰"):
    # Convert inputs to model format
    input_data = {
        "age": age,
        "education": {"High School": 0, "Bachelor’s": 1, "Master’s": 2, "PhD": 3}[education],
        "occupation": {"Tech": 0, "Sales": 1, "Executive": 2, "Admin": 3}[occupation],
        "hours_per_week": hours_per_week
    }
    salary_class = predict_salary(input_data)
    st.success(f"Predicted Salary Category for {name or 'this employee'}: **{salary_class}**")
