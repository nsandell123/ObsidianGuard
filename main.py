import requests
import json
from config import API_KEY, GITHUB_TOKEN

# Function to read questions from the questions.txt file
def load_questions(filename):
    with open(filename, 'r') as file:
        questions = [line.strip() for line in file.readlines()]
    return questions

# Function to query the Greptile API
def query_greptile_api(question):
    url = "https://api.greptile.com/v2/query"
    
    # Hardcoded repository details for the Templater repo
    repo_url = "https://github.com/SilentVoid13/Templater"
    question = f"{question} Respond with no more than 2 sentences."

    payload = {
        "messages": [
            {
                "id": "1",
                "content": question,
                "role": "user"
            }
        ],
        "repositories": [
            {
                "remote": "github",
                "branch": "master",  # Using the master branch as specified
                "repository": "SilentVoid13/Templater"  # Hardcoded repo name
            }
        ],
        "stream": False,
        "genius": False
    }

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "X-GitHub-Token": GITHUB_TOKEN,
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)
    print(response.text)
    

# Main function to run the command-line utility
def main():
    questions = load_questions('questions.txt')
    
    for question in questions:
        print(f"Question: {question}")
        query_greptile_api(question)

if __name__ == "__main__":
    main()
