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
prompt = "Suggest me what can I name you?"

# SYSTEM ROLE
message_system = {
    "role": "system",
    "content": "You are my Personal Assistant and my name is Arsh"
}

message = {
    "role": role,
    "content": prompt
}

messages = [message_system,message]

# SETTING TEMPERATURE
response = client.chat.completions.create(
    model=model, messages=messages, temperature=1
)

# print(response)

print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

answer = response.choices[0].message.content
print(answer)