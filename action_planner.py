import requests
import json
import re
from system_context import get_context_summary

def generate_action_plan(task):
    context = get_context_summary()

    prompt = f"""
You are a Linux AI assistant.

Current System Environment:
- OS: {context['os']}
- Package Manager: {context['package_manager']}
- Desktop Session: {context['session']}
- Installed Browsers: {', '.join(context['browsers']) or 'none'}
- Installed Editors: {', '.join(context['text_editors']) or 'none'}

Your task is to convert this user request into a structured plan that can be executed on this system.

Respond with a JSON object in the following format:
{{
  "goal": "<user's goal>",
  "steps": ["<step 1>", "<step 2>", "..."],
  "final_command": "<exact shell command to run>"
}}

User Request: {task}

Respond only with the JSON. Do not use markdown, explanations, or code blocks.
"""

    payload = {
        "model": "mistral",
        "prompt": prompt.strip(),
        "stream": False
    }

    try:
        response = requests.post("http://localhost:11434/api/generate", json=payload)
        result = response.json()
        raw = result.get("response", "").strip()

        if not raw:
            return {"error": "No response from LLM. Is Ollama running and mistral loaded?"}

        # Try extracting the first JSON-like object from raw output
        match = re.search(r'\{.*\}', raw, re.DOTALL)
        if not match:
            return {"error": "No valid JSON object found in response."}

        parsed = json.loads(match.group(0))

        # Validate basic structure
        if not all(k in parsed for k in ("goal", "steps", "final_command")):
            return {"error": "Incomplete JSON structure returned by LLM."}

        return parsed

    except json.JSONDecodeError as e:
        return {"error": f"JSON decode error: {e}"}
    except requests.exceptions.RequestException as e:
        return {"error": f"Network error: {e}"}
    except Exception as e:
        return {"error": str(e)}
