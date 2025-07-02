import subprocess

def execute_plan(command):
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        print("Execution Output:\n")
        print(result.stdout)
        if result.stderr:
            print("Errors:\n")
            print(result.stderr)
    except Exception as e:
        print(f"Execution failed: {e}")
