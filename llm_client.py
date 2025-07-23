import os
from dotenv import load_dotenv
from openai import OpenAI  # new client


load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

response = client.responses.create(
    model="gpt-4o",
    instructions="You are an assistant that talks like a pirate.",
    input="say hello",
)

print(response.output_text)
print(response)

