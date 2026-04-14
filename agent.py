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
def run_neuroplan(problem, feedback=None):

    steps = []

    # STEP 1: Initial Solution
    initial = call(f"""
    Solve this problem clearly:
    - Step-by-step
    - Explanation
    - Simple language

    Problem: {problem}
    """)
    steps.append(("⚙️ Initial Solution", initial))

    # STEP 2: Evaluation
    evaluation = call(f"""
    Evaluate this solution:
    - What is correct?
    - What is missing?
    - What can be improved?

    {initial}
    """)
    steps.append(("🔍 Evaluation", evaluation))

    # STEP 3: Improvement (WITH USER FEEDBACK)
    if feedback:
        improved = call(f"""
        Improve this solution using:

        User Feedback:
        {feedback}

        Original:
        {initial}

        Evaluation:
        {evaluation}

        Make it better, clearer, and more detailed.
        """)
    else:
        improved = call(f"""
        Improve this solution:

        {initial}

        Based on:
        {evaluation}
        """)

    steps.append(("✨ Improved Solution", improved))

    # STEP 4: Final Answer
    final = call(f"""
    Format final answer:
    - Headings
    - Bullet points
    - Clear explanation

    {improved}
    """)
    steps.append(("✅ Final Answer", final))

    return steps, final