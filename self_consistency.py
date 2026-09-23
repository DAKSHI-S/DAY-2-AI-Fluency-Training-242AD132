import os
from collections import Counter
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

question = """
Package A costs ₹20,000 and Package B costs ₹25,000.
A 10% discount is applied to both packages.

Which package is cheaper after the discount, and what is the
difference between their final prices?

Return only the final answer in this format:
Package: <A or B>; Difference: <amount>
"""

print("===== SELF-CONSISTENCY TEST =====")
print("Temperature: 0.8\n")

answers = []

for i in range(5):

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "system",
                "content": (
                    "Solve the arithmetic problem carefully. "
                    "Return only the requested final answer format."
                )
            },
            {
                "role": "user",
                "content": question
            }
        ],
        temperature=0
    )

    answer = response.choices[0].message.content.strip()

    answers.append(answer)

    print(f"Run {i + 1}: {answer}")

counts = Counter(answers)

majority_answer, count = counts.most_common(1)[0]

print("\n===== RESULT =====")
print(f"Majority answer: {majority_answer}")
print(f"Votes: {count} out of {len(answers)}")