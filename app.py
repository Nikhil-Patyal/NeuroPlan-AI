import streamlit as st
from agent import generate_plan, refine_plan

st.set_page_config(page_title="NeuroPlan AI", layout="wide")

# ---------------------------
# 🎨 UI STYLE
# ---------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&display=swap');

html, body {
    font-family: 'Inter', sans-serif;
    background: linear-gradient(135deg, #0f172a, #020617);
    color: white;
}

.title {
    font-size: 42px;
    font-weight: 600;
}

.card {
    background: rgba(255,255,255,0.05);
    padding: 20px;
    border-radius: 14px;
    margin-top: 20px;
    font-size: 16px;
    line-height: 1.8;
}

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
# FORMAT FUNCTION
# ---------------------------
def format_text(text):
    # remove unwanted symbols if model still gives them
    text = text.replace("**", "").replace("*", "")

    lines = text.split("\n")
    html = ""

    for line in lines:
        line = line.strip()

        # Step headings
        if line.lower().startswith("step"):
            html += f"<h3 style='margin-top:20px; color:#38bdf8;'>{line}</h3>"

        # bullets
        elif line.startswith("-"):
            html += f"<li>{line[1:].strip()}</li>"

        # normal text
        elif line:
            html += f"<p style='margin:6px 0;'>{line}</p>"

    return f"<div>{html}</div>"

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
    {format_text(st.session_state.plan)}
    </div>
    """, unsafe_allow_html=True)

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

    st.markdown(f"""
    <div class="card" style="border-left:6px solid #10b981;">
    <h4>✅ Refined Plan</h4>
    {format_text(st.session_state.refined)}
    </div>
    
    """, unsafe_allow_html=True)