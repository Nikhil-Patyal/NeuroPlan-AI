import streamlit as st
from agent import run_neuroplan

st.set_page_config(page_title="NeuroPlan AI", layout="wide")

st.title("🧠 NeuroPlan AI")
st.caption("Context-Aware Recommendation System")

# ---------------------------
# INPUT
# ---------------------------
user_input = st.text_area("Enter your goal:")

if st.button("Generate Plan"):

    with st.spinner("Generating detailed plan..."):
        context, plan = run_neuroplan(user_input)

    st.subheader("📌 Context Analysis")
    st.write(context)

    st.subheader("📋 Generated Plan (~800 words)")
    st.write(plan)

# ---------------------------
# FEEDBACK
# ---------------------------
feedback = st.text_input("Give feedback to improve plan:")

if st.button("Refine Plan"):

    with st.spinner("Refining..."):
        _, improved = run_neuroplan(user_input, feedback)

    st.subheader("✅ Improved Plan")
    st.write(improved)