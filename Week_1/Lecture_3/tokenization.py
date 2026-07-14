import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("GROQ_API_KEY environment variable is not set.")

client = Groq(api_key=my_api_key)

model = "llama-3.3-70b-versatile"
role = "user"
prompt1 = "Hi!"
prompt2 = "Describe what you can do?"
prompt3 = "Tell everything about your company in detail."

prompts = [prompt1,prompt2,prompt3]

messages = []
for prompt in prompts:
    message = {
    "role": role,
    "content": prompt
    }
    messages.append(message)

    response = client.chat.completions.create(
        model=model, messages=messages
    )

    answer = response.choices[0].message.content
    print(answer)
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

    token_usage = response.usage
    print(f"Given Prompt: {prompt}\nInput_Tokens = {token_usage.prompt_tokens}, Output_Tokens = {token_usage.completion_tokens}, Total_Tokens = {token_usage.total_tokens}")
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")