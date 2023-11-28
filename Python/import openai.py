import openai
openai.api_key = "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"
x = 12
language = "romanian"
prompt = "be sarcastic"
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    prompt = [
        {"role": "system", "content": f"You are a helpful assistant. You answer in {language} "},
        {"role": "user", "content": f"{prompt}"}
    ], max_tokens = 50
)

print(response.choices[0].message["content"])