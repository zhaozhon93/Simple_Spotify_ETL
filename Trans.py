import pandas as pd
import Extract
import main

TOKEN = main.get_token()

def Transform(data):
    release_date = []
    Album_name = []
    Album_type = []
    Album_uri = []
    # Extracting only the relevant bits of data from the json object
    for i in data['albums']['items']:
        release_date.append(i['release_date'])
        Album_name.append(i['name'])
        Album_type.append(i['type'])
        Album_uri.append(i['uri'])

    df_dict = {
        "release_date": release_date,
        "Album_name": Album_name,
        "Album_type": Album_type,
        "Album_uri": Album_uri
    }
    df = pd.DataFrame(df_dict, columns=["release_date", "Album_name", "Album_type", "Album_uri"])

    return df


if __name__ == '__main__':
    print(Transform(Extract.return_data(TOKEN)))

