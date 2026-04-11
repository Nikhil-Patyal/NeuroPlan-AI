import streamlit as st
from agent import *

st.set_page_config(page_title="NeuroPlan AI Agent", layout="wide")

# ---------------------------
# CUSTOM CSS (PREMIUM UI)
# ---------------------------
st.markdown("""
<style>
.main {
    background-color: #0f172a;
    color: white;
}

.stChatMessage {
    border-radius: 15px;
    padding: 10px;
    margin-bottom: 10px;
}

.user-msg {
    background-color: #1e293b;
    padding: 12px;
    border-radius: 10px;
}

.bot-msg {
    background-color: #334155;
    padding: 12px;
    border-radius: 10px;
}

.card {
    background-color: #1e293b;
    padding: 20px;
    border-radius: 15px;
    margin: 10px 0;
    box-shadow: 0px 0px 10px rgba(0,0,0,0.3);
}

.metric {
    background-color: #020617;
    padding: 15px;
    border-radius: 10px;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# ---------------------------
# HEADER
# ---------------------------
st.title("🧠 NeuroPlan AI Agent")
st.caption("Autonomous Planning System • Think → Decide → Act")

# ---------------------------
# DASHBOARD METRICS
# ---------------------------
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="metric">⚡ Fast Local AI</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="metric">🛠 Tool-Based Agent</div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="metric">🧠 Smart Planning</div>', unsafe_allow_html=True)

# ---------------------------
# SIDEBAR
# ---------------------------
st.sidebar.title("⚙️ Agent Dashboard")
st.sidebar.markdown("### Available Tools")
st.sidebar.write("✔ Plan Generator")
st.sidebar.write("✔ Plan Refiner")
st.sidebar.write("✔ Schedule Creator")

# ---------------------------
# SESSION STATE
# ---------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

if "plan" not in st.session_state:
    st.session_state.plan = None

# ---------------------------
# INPUT
# ---------------------------
user_input = st.chat_input("Enter your goal or feedback...")

# ---------------------------
# AGENT PROCESSING
# ---------------------------
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.spinner("🤖 Agent thinking..."):
        result, tool = run_agent(user_input, st.session_state.plan)

    st.session_state.plan = result

    st.session_state.messages.append({
        "role": "assistant",
        "content": f"🛠 Tool Used: {tool}\n\n{result}"
    })

# ---------------------------
# CHAT DISPLAY (CARDS STYLE)
# ---------------------------
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f'<div class="card user-msg">👤 {msg["content"]}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="card bot-msg">🤖 {msg["content"]}</div>', unsafe_allow_html=True)

# ---------------------------
# PLAN DASHBOARD
# ---------------------------
if st.session_state.plan:
    st.markdown("### 📊 Latest Plan Overview")

    st.markdown(f"""
    <div class="card">
    <h4>📌 Generated Plan</h4>
    <p>{st.session_state.plan}</p>
    </div>
    """, unsafe_allow_html=True)

# ---------------------------
# DOWNLOAD BUTTON
# ---------------------------
if st.session_state.plan:
    st.download_button(
        label="📥 Download Plan",
        data=st.session_state.plan,
        file_name="neuroplan_output.txt"
    )