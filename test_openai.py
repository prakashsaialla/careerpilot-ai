import requests

response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "llama3.2:1b",
        "prompt": "What is the capital of France?",
        "stream": False
    }
)

print(response.json())