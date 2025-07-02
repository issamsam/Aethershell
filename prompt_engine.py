import json
import re
import os
from system_context import get_context_summary
from llama_cpp import Llama

# Load model once (fast after first load)
MODEL_PATH = "models/mistral-7b-instruct-v0.1.Q4_K_M.gguf"
llm = Llama(model_path=MODEL_PATH, n_ctx=2048)

def generate_action_plan(task):
    context = get_context_summary()

    prompt = f"""You are a Linux AI assistant.

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

    try:
        response = llm.create_chat_completion(
            messages=[
                {"role": "system", "content": "You are a helpful Linux assistant."},
                {"role": "user", "content": prompt.strip()}
            ]
        )
        raw = response['choices'][0]['message']['content'].strip()

        match = re.search(r'\{.*\}', raw, re.DOTALL)
        if match:
            return json.loads(match.group(0))
        else:
            return {"error": "No valid JSON object found in response."}

    except Exception as e:
        return {"error": str(e)}
