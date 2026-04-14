import streamlit as st
from agent import generate_plan, refine_plan

st.set_page_config(page_title="NeuroPlan AI", layout="wide")

# ---------------------------
# 🎨 MODERN UI
# ---------------------------
st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

/* Background */
body {
    background: linear-gradient(135deg, #0f172a, #020617);
    color: white;
}

/* Title */
.title {
    font-size: 42px;
    font-weight: 600;
}

/* Cards */
.card {
    background: rgba(255,255,255,0.05);
    padding: 16px;
    border-radius: 12px;
    margin-top: 20px;
    border-left: 6px solid #3b82f6;
}

/* Buttons */
.stButton>button {
    border-radius: 10px;
    padding: 8px 16px;
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

    st.markdown(f"""
    <div class="card" style="border-left:6px solid #f59e0b;">
    <h4>⚙️ Initial Plan</h4>
    <p>{st.session_state.plan.replace("\n","<br>")}</p>
    </div>
    """, unsafe_allow_html=True)

    # ---------------------------
    # FEEDBACK INPUT
    # ---------------------------
    feedback = st.text_input("Give feedback to improve plan:")

    # ---------------------------
    # REFINE BUTTON
    # ---------------------------
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

    st.markdown(f"""
    <div class="card" style="border-left:6px solid #10b981;">
    <h4>✅ Refined Plan</h4>
    <p>{st.session_state.refined.replace("\n","<br>")}</p>
    </div>
    """, unsafe_allow_html=True)