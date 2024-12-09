import requests
from generate_fhir_ref import generate_referral
from dotenv import load_dotenv
import os
import argparse

# Load environment variables
load_dotenv()
api_url = os.getenv("API_URL")

if not api_url:
    raise ValueError("API_URL is not set in .env file")

def send_referral(api_url, referral):
    """
    Send the referral data to the specified API endpoint.
    """
    headers = {'Content-Type': 'application/json'}
    try:
        response = requests.post(api_url, headers=headers, json=referral)
        response.raise_for_status()
        print(f"Success: {response.status_code}, Response: {response.json()}")
    except requests.exceptions.RequestException as e:
        print(f"Error sending referral: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Send FHIR Referrals to an API")
    parser.add_argument('--count', type=int, default=1, help='Number of referrals to send')
    args = parser.parse_args()

    for _ in range(args.count):
        referral = generate_referral()
        send_referral(api_url, referral)
