import requests
from config import API_KEY, GITHUB_TOKEN  # Importing from config.py

url = "https://api.greptile.com/v2/repositories"

payload = {
    "remote": "github",
    "repository": "SilentVoid13/Templater",
    "branch": "master",
    "reload": True,
    "notify": True
}

# Use API_KEY and GITHUB_TOKEN from the config file
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "X-GitHub-Token": GITHUB_TOKEN,
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(f"Status Code: {response.status_code}")
print(f"Response Text: {response.text}")
