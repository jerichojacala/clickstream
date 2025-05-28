import requests
import json

url = "https://panyxd8w1f.execute-api.us-east-2.amazonaws.com/dev/ingest"  # Replace with your real URL

data = {
    "event": "login",
    "user_id": 42,
    "timestamp": "2025-05-25T18:00:00Z"
}

response = requests.post(url, json=data)
print("Status:", response.status_code)
print("Response:", response.json())