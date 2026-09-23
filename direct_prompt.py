import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

question = """
A college is planning an annual event and wants to compare two event packages.

Package A and Package B have prices stored in an external pricing system.
The question is:

Which package is cheaper after applying a 10% discount to each package,
and what is the difference in their final prices?

Answer the question directly. Do not use any tools.
"""

response = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
        {
            "role": "system",
            "content": "Answer the user's question directly using only the information available in the prompt."
        },
        {
            "role": "user",
            "content": question
        }
    ],
    temperature=0
)

print("\n===== DIRECT PROMPTING =====")
print(response.choices[0].message.content)