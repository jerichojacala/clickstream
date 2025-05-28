import requests
import json
import random
import time
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

# Your deployed API Gateway REST endpoint
url = "https://panyxd8w1f.execute-api.us-east-2.amazonaws.com/dev/ingest"
api_key = os.getenv("API_KEY")

# Sample clickstream events
actions = ["page_view", "login", "logout", "add_to_cart", "checkout", "scroll", "search"]

# Generate fake clickstream events
def generate_event():
    return {
        "event": random.choice(actions),
        "user_id": random.randint(1, 100),
        "timestamp": datetime.utcnow().isoformat() + "Z",
    }

# Send clickstream events in a loop
while True:
    event = generate_event()
    print("Sending event:", event)
    headers = {'x-api-key': api_key}
    try:
        response = requests.post(url, json=event)
        print("Status:", response.status_code)
        print("Response:", response.text)
    except Exception as e:
        print("Error sending event:", e)

    time.sleep(random.uniform(1, 2))  # Wait 1–2 seconds
