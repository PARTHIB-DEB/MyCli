from ollama import Client
client = Client(host='http://localhost:11434')
response = client.chat(model='Qwen2-0.5B', messages=[
  {
    'role': 'user',
    'content': 'Why is the sky blue?',
  },
])