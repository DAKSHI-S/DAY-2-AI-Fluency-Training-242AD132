import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

question = """
A college is planning an annual event.

The following information is already known:

Package A costs ₹20,000.
Package B costs ₹25,000.

A 10% discount is applied to both packages.

Which package is cheaper, and what is the difference between their final prices?
"""

response = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
        {
            "role": "system",
            "content": (
                "Solve the problem carefully step by step before giving "
                "the final answer."
            )
        },
        {
            "role": "user",
            "content": question
        }
    ],
    temperature=0
)

print("\n===== CHAIN-OF-THOUGHT =====")
print(response.choices[0].message.content)