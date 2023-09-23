import openai
import csv
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv("GPTAPI_Key")

def ChatGPTResponse(prompt):
    return openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=1000,
        temperature=.5,
    )
