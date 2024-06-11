from dotenv import load_dotenv
import os
from os.path import join, dirname
import base64
from requests import post
import json

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

load_dotenv()

client_id = os.environ.get("Client_id")
client_secret = os.environ.get("Client_secret")

def get_token():
    auth_string = client_id + ":" + client_secret
    auth_bytes  = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes),"utf-8")

    url ="https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"

    }
    data = {"grant_type": "client_credentials"}
    result =post(url,headers = headers,data = data)
    json_result = json.loads(result.content)
    token = json_result["access_token"]
    return token

def get_auth_header(token):
    return {"Authorization": "Bearer " + token}


Token =get_token()




