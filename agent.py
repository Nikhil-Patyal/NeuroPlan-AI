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
# GENERATE PLAN
# ---------------------------
def generate_plan(goal):
    return call(f"""
    Create a clean structured plan:

    Rules:
    - Use headings like Step 1, Step 2
    - Use simple bullet points
    - NO symbols like *, +, **
    - Each point on new line
    - Keep it clear and readable

    Goal:
    {goal}
    """)


# ---------------------------
# REFINE PLAN
# ---------------------------
def refine_plan(goal, initial_plan, feedback):
    return call(f"""
    Improve this plan using feedback:

    Rules:
    - Clean formatting
    - Proper headings (Step 1, Step 2)
    - Simple bullet points
    - No symbols like *, +, **

    Goal:
    {goal}

    Original Plan:
    {initial_plan}

    Feedback:
    {feedback}
    """)