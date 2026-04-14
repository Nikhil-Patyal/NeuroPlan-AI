import streamlit as st
import time
from agent import generate_plan, refine_plan

st.set_page_config(page_title="NeuroPlan AI", layout="wide")

# ---------------------------
# 🎨 UI STYLE (FINAL POLISH)
# ---------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&display=swap');

html, body {
    font-family: 'Inter', sans-serif;
    background: linear-gradient(135deg, #0f172a, #020617);
    color: white;
}

/* Title */
.title {
    font-size: 42px;
    font-weight: 600;
}

/* Card */
.card {
    background: rgba(255,255,255,0.05);
    padding: 22px;
    border-radius: 14px;
    margin-top: 25px;
    font-size: 16px;
    line-height: 1.9;
}

/* Divider */
.divider {
    height: 1px;
    background: rgba(255,255,255,0.08);
    margin: 16px 0;
}

/* Text spacing */
.text {
    margin: 8px 0;
    color: #e5e7eb;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------
# TITLE
# ---------------------------
st.markdown("<div class='title'>🧠 NeuroPlan AI</div>", unsafe_allow_html=True)
st.caption("AI Planner with Feedback Optimization")

# ---------------------------
# SESSION STATE
# ---------------------------
if "plan" not in st.session_state:
    st.session_state.plan = None

if "refined" not in st.session_state:
    st.session_state.refined = None

# ---------------------------
# FORMAT FUNCTION (CHATGPT STYLE)
# ---------------------------
def format_text(text):
    text = text.replace("**", "").replace("*", "")

    lines = text.split("\n")
    html = ""

    for line in lines:
        line = line.strip()

        # STEP HEADING
        if line.lower().startswith("step"):
            html += f"<div class='divider'></div>"
            html += f"<p style='margin-top:10px; color:#38bdf8; font-size:18px; font-weight:600;'>{line}</p>"

        # NORMAL TEXT
        elif line:
            html += f"<p class='text'>{line}</p>"

    return f"<div>{html}</div>"

# ---------------------------
# TYPING EFFECT
# ---------------------------
def typing_effect(text):
    placeholder = st.empty()
    output = ""

    for char in text:
        output += char
        placeholder.markdown(output, unsafe_allow_html=True)
        time.sleep(0.002)

# ---------------------------
# INPUT
# ---------------------------
goal = st.text_area("Enter your goal:")

# ---------------------------
# GENERATE PLAN
# ---------------------------
if st.button("🚀 Generate Plan"):

    if goal:
        with st.spinner("Generating plan..."):
            st.session_state.plan = generate_plan(goal)
            st.session_state.refined = None

# ---------------------------
# SHOW INITIAL PLAN
# ---------------------------
if st.session_state.plan:

    st.markdown("<div class='card' style='border-left:6px solid #f59e0b;'>", unsafe_allow_html=True)
    st.markdown("<h4>⚙️ Initial Plan</h4>", unsafe_allow_html=True)

    typing_effect(format_text(st.session_state.plan))

    st.markdown("</div>", unsafe_allow_html=True)

    feedback = st.text_input("Give feedback to improve plan:")

    if st.button("✨ Refine Plan"):

        if feedback:
            with st.spinner("Refining plan..."):
                st.session_state.refined = refine_plan(
                    goal,
                    st.session_state.plan,
                    feedback
                )

# ---------------------------
# SHOW REFINED PLAN
# ---------------------------
if st.session_state.refined:

    st.markdown("<div class='card' style='border-left:6px solid #10b981;'>", unsafe_allow_html=True)
    st.markdown("<h4>✅ Refined Plan</h4>", unsafe_allow_html=True)

    typing_effect(format_text(st.session_state.refined))

    st.markdown("</div>", unsafe_allow_html=True)