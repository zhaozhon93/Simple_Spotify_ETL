# Import necessary libraries
import pandas as pd
import Extract
import main

# Get the token from the main module
TOKEN = main.get_token()

def Transform(data):
    """
    Function to transform the raw data from Spotify's new releases into a DataFrame
    """
    # Initialize lists to store the extracted data
    release_date, Album_name, Album_type, Album_uri = [], [], [], []

    # Extracting only the relevant bits of data from the json object
    for i in data['albums']['items']:
        release_date.append(i['release_date'])
        Album_name.append(i['name'])
        Album_type.append(i['type'])
        Album_uri.append(i['uri'])

    # Create a dictionary from the lists
    df_dict = {
        "release_date": release_date,
        "Album_name": Album_name,
        "Album_type": Album_type,
        "Album_uri": Album_uri
    }

    # Convert the dictionary into a DataFrame
    df = pd.DataFrame(df_dict)

    # Return the DataFrame
    return df

if __name__ == '__main__':
    # If this script is run directly, print the transformed data
    print(Transform(Extract.return_data(TOKEN)))