import requests
import json

# ---------------------------
# CALL OLLAMA (MISTRAL)
# ---------------------------
def call(prompt):
    url = "http://localhost:11434/api/generate"

    response = requests.post(url, json={
        "model": "mistral",
        "prompt": prompt,
        "stream": False,
        "options": {
            "num_predict": 150,
            "temperature": 0.7
        }
    })

    return response.json()["response"].strip()


# ---------------------------
# TOOLS
# ---------------------------

def generate_plan(user_input):
    prompt = f"""
    Create a short, structured step-by-step plan for:
    {user_input}

    Keep it simple and practical.
    """
    return call(prompt)


def refine_plan(plan, feedback):
    prompt = f"""
    Improve this plan:

    Plan:
    {plan}

    Feedback:
    {feedback}

    Make it better and simpler.
    """
    return call(prompt)


def create_schedule(goal):
    prompt = f"""
    Create a simple daily schedule for:
    {goal}

    Keep it realistic.
    """
    return call(prompt)


# ---------------------------
# AGENT DECISION (JSON OUTPUT)
# ---------------------------
def agent_decide(user_input):
    prompt = f"""
    You are an AI agent.

    Decide the best action for this input:
    {user_input}

    Available tools:
    - generate_plan
    - refine_plan
    - create_schedule

    Respond ONLY in JSON format like:
    {{"tool": "tool_name"}}
    """

    response = call(prompt)

    try:
        decision = json.loads(response)
        return decision.get("tool", "generate_plan")
    except:
        return "generate_plan"


# ---------------------------
# MAIN AGENT
# ---------------------------
def run_agent(user_input, previous_plan=None):
    tool = agent_decide(user_input)

    if tool == "refine_plan" and previous_plan:
        result = refine_plan(previous_plan, user_input)

    elif tool == "create_schedule":
        result = create_schedule(user_input)

    else:
        result = generate_plan(user_input)

    save_history(user_input, result, tool)
    return result, tool


# ---------------------------
# MEMORY
# ---------------------------
def save_history(user_input, output, tool):
    with open("history.txt", "a") as f:
        f.write(f"USER: {user_input}\nTOOL: {tool}\nOUTPUT: {output}\n\n")