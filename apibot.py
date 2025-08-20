from openai import OpenAI

client = OpenAI(
    api_key="Your_API_Key",
    base_url="https://api.groq.com/openai/v1"
)

while True:
    user_input = input("User: ")
    if user_input == "quit":
        print("Bot: GodSpeed!")
        break
    response = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[
            {"role": "system", "content": "You are a car enthusiast bot, provide information only about cars and motorsports."},
            {"role": "user", "content": user_input}
        ]
    )
    print("Bot:", response.choices[0].message.content)
