import streamlit as st
from agent import *

st.set_page_config(page_title="ReflexMind AI", layout="wide")

# ---------------------------
# 🎨 PREMIUM UI STYLE
# ---------------------------
st.markdown("""
<style>

/* Background Gradient */
body {
    background: linear-gradient(135deg, #e0f2fe, #f8fafc);
}

/* Title */
.title {
    text-align: center;
    font-size: 42px;
    font-weight: bold;
    color: #0f172a;
}

.subtitle {
    text-align: center;
    color: #475569;
    margin-bottom: 30px;
}

/* Glass Cards */
.card {
    background: rgba(255,255,255,0.7);
    backdrop-filter: blur(10px);
    padding: 18px;
    border-radius: 16px;
    margin: 12px 0;
    box-shadow: 0 8px 20px rgba(0,0,0,0.08);
    transition: transform 0.2s ease;
}

.card:hover {
    transform: scale(1.02);
}

/* Colored Borders */
.strategy { border-left: 6px solid #3b82f6; }
.initial { border-left: 6px solid #f59e0b; }
.eval { border-left: 6px solid #ef4444; }
.final { border-left: 6px solid #10b981; }

/* Sidebar */
section[data-testid="stSidebar"] {
    background: #0f172a;
    color: white;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------
# 🧠 HEADER
# ---------------------------
st.markdown("<div class='title'>🧠 ReflexMind AI</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Think • Evaluate • Improve</div>", unsafe_allow_html=True)

# ---------------------------
# 📊 SIDEBAR
# ---------------------------
st.sidebar.title("📊 ReflexMind Dashboard")

st.sidebar.markdown("### ⚙️ System")
st.sidebar.write("Model: Mistral")
st.sidebar.write("Mode: Adaptive Agent")

st.sidebar.markdown("### 🧠 Features")
st.sidebar.write("✔ Strategy Selection")
st.sidebar.write("✔ Self Evaluation")
st.sidebar.write("✔ Improvement Loop")

st.sidebar.markdown("### 🚀 Status")
st.sidebar.success("Active")

# ---------------------------
# 💬 INPUT BOX
# ---------------------------
problem = st.text_area("💬 Enter your problem:", placeholder="e.g. How to prepare for exams in 5 days?")

# ---------------------------
# 🚀 RUN BUTTON
# ---------------------------
if st.button("🚀 Run ReflexMind"):

    with st.spinner("🧠 Thinking..."):
        steps, final = run_agent(problem)

    strategy = steps[0][1]
    initial = steps[1][1]
    evaluation = steps[2][1]

    # ---------------------------
    # 📦 OUTPUT CARDS
    # ---------------------------

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 🧠 Strategy")
        st.markdown(f"<div class='card strategy'>{strategy}</div>", unsafe_allow_html=True)

        st.markdown("### ⚙️ Initial Solution")
        st.markdown(f"<div class='card initial'>{initial}</div>", unsafe_allow_html=True)

    with col2:
        st.markdown("### 🔍 Evaluation")
        st.markdown(f"<div class='card eval'>{evaluation}</div>", unsafe_allow_html=True)

        st.markdown("### ✅ Final Answer")
        st.markdown(f"<div class='card final'>{final}</div>", unsafe_allow_html=True)