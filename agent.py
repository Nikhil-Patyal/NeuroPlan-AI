from groq import Groq
import os

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# ---------------------------
# CALL FUNCTION
# ---------------------------
def call(prompt):
    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt.strip()}],
            temperature=0.7,
            max_tokens=2500
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"


# ---------------------------
# STEP 1: GENERATE PLAN
# ---------------------------
def generate_plan(goal):
    return call(f"""
    Create a clear and structured plan:
    - Step-by-step
    - Easy to follow
    - Use bullet points
    - Add small explanations

    Goal: {goal}
    """)


# ---------------------------
# STEP 2: REFINE PLAN
# ---------------------------
def refine_plan(goal, initial_plan, feedback):
    return call(f"""
    Improve this plan using feedback:

    Goal:
    {goal}

    Original Plan:
    {initial_plan}

    User Feedback:
    {feedback}

    Make it:
    - More clear
    - More practical
    - Better structured
    - More detailed
    """)