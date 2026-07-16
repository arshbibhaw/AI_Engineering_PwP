import os
from dotenv import load_dotenv
from groq import Groq
from pydantic import BaseModel
import json

load_dotenv()

class Ticket(BaseModel):
    name: str
    email: str
    number: int
    city: str
    issue: str

schema = Ticket.model_json_schema()

text = "I have an issue with my account. My name is John Doe, my email is john.doe@example.com, my number is 1234567890, I live in New York, and I have been experiencing login problems. Can you help me resolve this issue as my account is having 5M+ US dollars."

my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("GROQ_API_KEY environment variable is not set.")

client = Groq(api_key=my_api_key)
model = "llama-3.3-70b-versatile"

user_role = "user"
user_prompt = f"From the {text}, Extract the following fields from the user input and return them in JSON format: name, email, number, city, issue."

system_role = "system"  
system_prompt = f"""Extract the following fields from the user input and return them in JSON format: name, email, number, city, issue. Ensure that the output adheres to the provided schema {schema}."""

system_message = {
    "role": system_role,
    "content": system_prompt
}

message = {
    "role": user_role,
    "content": user_prompt
}

messages = [system_message, message]

response_format = {
    "type": "json_object"
}

response = client.chat.completions.create(
    model=model,
    messages=messages,
    response_format=response_format
)

print("Raw JSON Response:")
answer = response.choices[0].message.content
print(answer)

print("\nLLM Response / Pydantic Object:")

raw_json = answer
data = json.loads(raw_json)
ticket = Ticket(**data)
print(ticket)

print(ticket.name)
print(ticket.email)
print(ticket.number)
print(ticket.city)
print(ticket.issue)