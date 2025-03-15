from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()
print("DEBUG: ", os.getenv("OPENAI_API_KEY"))
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key=OPENAI_API_KEY)

response = client.responses.create(
    model="gpt-4o",
    instructions="Act as a personal trainer and provide a workout plan for a beginner. Don't assume any prior knowledge.",
    input="Are semicolons optional in JavaScript?",
)

print(response.output_text)