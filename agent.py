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
Create a clean and natural plan.

STRICT RULES:
- Do NOT use *, **, # or markdown
- Use plain text only
- Format like:

Step 1: Title
Explanation

Step 2: Title
Explanation

- Keep it readable like ChatGPT

Goal:
{goal}
""")


# ---------------------------
# REFINE PLAN
# ---------------------------
def refine_plan(goal, initial_plan, feedback):
    return call(f"""
Improve this plan using feedback.

STRICT RULES:
- No *, **, # symbols
- Plain text only
- Use format:

Step 1: Title
Explanation

Step 2: Title
Explanation

Goal:
{goal}

Original Plan:
{initial_plan}

Feedback:
{feedback}
""")