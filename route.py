# REST API Calls

import requests

ENDPOINT = "https://generate-coding-challenge-server-rellb.ondigitalocean.app"


# Register the user and get the token and challenge
def register_user(
    endpoint: str,
    name: str,
    nuid: str
) -> tuple[str, list]:
    
    register_endpoint = f'{endpoint}/register'
    
    response = requests.post(
        url = register_endpoint,
        json = {
            "name": name,
            "nuid": nuid
        }
    )
    
    if response.status_code == 200:
        data = response.json()
        
        token = data["token"]
        challenge = data["challenge"]
        
        return token, challenge
    
    else:
        raise Exception(f"Error Registering User: {response.status_code}")


# Get the token if I forgot it  
def forgot_token(
    endpoint: str,
    nuid: str
) -> str:
    
    forgot_token_endpoint = f'{endpoint}/forgot_token/{nuid}'
    
    response = requests.get(
        url = forgot_token_endpoint
    )
    
    if response.status_code == 200:
        token = response.text
        
        return token
    
    else:
        raise Exception(f"Error Retrieving Token: {response.status_code}")
    
    
# Get the challenge if I forgot it
def get_challenge(
    endpoint: str,
    token: str
) -> list[str]:
    
    get_challenge_endpoint = f'{endpoint}/challenge/{token}'
    
    response = requests.get(
        url = get_challenge_endpoint
    )
    
    if response.status_code == 200:
        data = response.json()
        
        challenge = data["challenge"]
        
        return challenge
    
    else:
        raise Exception(f"Error Retrieving Challenge: {response.status_code}")
    

# Submit the solution and get feedback
def submit_solution(
    endpoint: str,
    solution: list[str],
    token: str
) -> tuple[bool, str]:
    
    submit_solution_endpoint = f'{endpoint}/submit/{token}'
    
    response = requests.post(
        url = submit_solution_endpoint,
        json = solution
    )
    
    if response.status_code == 200:
        data = response.json()
        
        correct = data["correct"]
        feedback = data["message"]
        
        return correct, feedback
    
    else:
        raise Exception(f"Error Submitting Solution: {response.status_code}")