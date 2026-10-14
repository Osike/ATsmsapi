import os
from pathlib import Path

import africastalking
from dotenv import load_dotenv

load_dotenv(Path(__file__).resolve().parent / ".env")

username = os.getenv("AT_USERNAME")
api_key = os.getenv("AT_API_KEY")

if not username or not api_key:
    raise SystemExit("Set AT_USERNAME and AT_API_KEY in the .env file.")

# Initialize the SDK
africastalking.initialize(username, api_key)

# Access the SMS service
sms = africastalking.SMS

print("Africa's Talking is configured!")

message = "Hello! This is my first Python SMS application."

recipients = ["+254751204883"]

try:
    response = sms.send(message, recipients)
    print("API response:")
    print(response)
except Exception as error:
    print("Something went wrong:", error)
