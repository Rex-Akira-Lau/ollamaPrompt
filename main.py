from ollama import chat

stream = chat(
    model='deepseek-r1',
    messages=[{'role': 'user', 'content': '为什么天这么蓝'}],
    stream=True,
)

for chunk in stream:
  print(chunk['message']['content'], end='', flush=True)