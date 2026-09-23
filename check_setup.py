from config import client, MODEL

try:
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": "Reply with exactly: SETUP OK"
            }
        ],
        temperature=0
    )

    print(response.choices[0].message.content)

except Exception as e:
    print("SETUP FAILED")
    print(e)