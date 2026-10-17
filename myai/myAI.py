from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()

ask = input("ask me anything: ")
res = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{
        "role": "user",
        "content": ask
    }],
    max_tokens=50
)
print(res.choices[0].message.content)
answer_file = open("answer_file.txt", "w")
answer_file.write(f"Answer: {res.choices[0].message.content}")
answer_file.close()