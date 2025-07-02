from prompt_engine import generate_action_plan
from step_executor import execute_plan

def run_task(task):
    plan = generate_action_plan(task)
    if "error" in plan:
        return f"Error: {plan['error']}"
    
    execute_plan(plan['final_command'])
    return "Execution complete."
