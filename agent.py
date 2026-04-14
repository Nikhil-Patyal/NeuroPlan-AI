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
- Do NOT use *, **, # or any symbols
- Do NOT use markdown or bold text
- Use plain text only
- Format exactly like:

Step 1: Title
Explanation in simple lines

Step 2: Title
Explanation...

- Use bullet points ONLY if really needed using "-"
- Keep it clean and readable like ChatGPT

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
- No *, **, # or markdown
- Plain clean text only
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