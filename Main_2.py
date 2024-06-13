# Import necessary modules
import os
import base64
import json
from os.path import join, dirname
from dotenv import load_dotenv
from requests import post

# Define the path to the .env file
dotenv_path = join(dirname(__file__), '.env')

# Load the .env file to set environment variables
load_dotenv(dotenv_path)

# Get the client_id and client_secret from environment variables
client_id = os.getenv("Client_id")
client_secret = os.getenv("Client_secret")

def get_token():
    """
    Function to get the token
    """
    # Create the authorization string and encode it in base64
    auth_string = f"{client_id}:{client_secret}"
    auth_base64 = base64.b64encode(auth_string.encode("utf-8")).decode("utf-8")

    # Define the URL for the token request
    url = "https://accounts.spotify.com/api/token"

    # Define the headers for the token request
    headers = {
        "Authorization": f"Basic {auth_base64}",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    # Define the data for the token request
    data = {"grant_type": "client_credentials"}

    # Make the token request
    result = post(url, headers=headers, data=data)

    # Parse the result as JSON
    json_result = json.loads(result.content)

    # Return the access token from the result
    return json_result["access_token"]

def get_auth_header(token):
    """
    Function to get the auth header
    """
    # Return the Authorization header with the token
    return {"Authorization": f"Bearer {token}"}