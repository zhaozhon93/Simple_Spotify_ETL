import pandas as pd
import requests
from datetime import datetime
import main

TOKEN = main.get_token()


def return_data(token1):
    input_variables = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": "Bearer {token}".format(token=token1)
    }

    # Download all new release alblums in the past 7 days
    r = requests.get("https://api.spotify.com/v1/browse/new-releases",
                     headers=input_variables)

    data = r.json()
    return data



