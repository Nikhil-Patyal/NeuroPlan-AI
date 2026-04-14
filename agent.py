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
            messages=[
                {"role": "user", "content": prompt.strip()}
            ],
            temperature=0.7,
            max_tokens=500
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"


# ---------------------------
# MAIN AGENT (SAME FLOW, BETTER QUALITY)
# ---------------------------
def run_neuroplan(problem):

    steps = []

    # STEP 1: Initial Solution
    initial = call(f"""
    Solve this problem with:
    - Clear steps
    - Explanation
    - Simple language

    Problem: {problem}
    """)
    steps.append(("⚙️ Initial Solution", initial))

    # STEP 2: Evaluation (STRONGER FEEDBACK)
    evaluation = call(f"""
    Evaluate this solution deeply:
    - What is correct?
    - What is missing?
    - What can be improved?

    {initial}
    """)
    steps.append(("🔍 Evaluation", evaluation))

    # STEP 3: Improved Solution (SMARTER)
    improved = call(f"""
    Improve this solution using the feedback:
    - Fix mistakes
    - Add missing parts
    - Make it more detailed

    Original:
    {initial}

    Feedback:
    {evaluation}
    """)
    steps.append(("✨ Improved Solution", improved))

    # STEP 4: Final Answer (BEST VERSION)
    final = call(f"""
    Create final answer:
    - Well structured
    - Use headings
    - Use bullet points
    - Easy to read
    - Complete explanation

    {improved}
    """)
    steps.append(("✅ Final Answer", final))

    return steps, final