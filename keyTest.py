import openai

a = openai.ChatCompletion.create(
    api_key=,
    model="gpt-3.5-turbo",
    temperature = .2,
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the Scottish Cup in 2023?"},
        {"role": "assistant", "content": "Celtic FC won the Scottish Cup in 2023."},
        {"role": "user", "content": "Who is its coach?"},
        {"role": "assistant","content":"Ange Postecoglou is its coach."},
        {"role":"user","content":"Who coached Celtic to the Scottish Cup final in 2023?"}
    ]
)
print(a)