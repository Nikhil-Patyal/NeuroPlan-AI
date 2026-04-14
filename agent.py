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
            max_tokens=700
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"


# ---------------------------
# GENERATE PLAN
# ---------------------------
def generate_plan(goal):
    return call(f"""
    Create a clean and natural plan:

    Rules:
    - Write like ChatGPT (clear and readable)
    - Use headings like "Step 1", "Step 2"
    - Add short explanation under each step
    - Use bullet points ONLY if needed
    - Avoid symbols like *, +, **

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
    - Keep it clean and natural
    - Use headings (Step 1, Step 2)
    - Add explanations under steps
    - Use bullets only when needed
    - Make it easy to read like ChatGPT

    Goal:
    {goal}

    Original Plan:
    {initial_plan}

    Feedback:
    {feedback}
    """)