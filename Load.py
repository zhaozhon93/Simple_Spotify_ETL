import Extract
import Trans
import main
import sqlalchemy
import pandas as pd
from sqlalchemy.orm import sessionmaker
import requests
import json
from datetime import datetime
import datetime
import sqlite3



TOKEN = main.get_token()

DATABASE_LOCATION = "sqlite:///Top_tracks.sqlite"

load_df=Extract.return_data(TOKEN)
Transformed_df = Trans.Transform(load_df)
data = Transformed_df.values.tolist()
#Loading into Database
engine = sqlalchemy.create_engine(DATABASE_LOCATION)
# Base =sqlalchemy.orm.declarative_base()
# Base.metadata.create_all(engine)
conn = sqlite3.connect('Top_tracks.sqlite')
cursor = conn.cursor()

sql_query_1 = """
    CREATE TABLE IF NOT EXISTS Top_tracks(
        release_date VARCHAR(200),
        Album_name VARCHAR(200),
        Album_type VARCHAR(200),
        Album_uri VARCHAR(200),
        CONSTRAINT primary_key_constraint PRIMARY KEY (Album_uri)
    )
"""

cursor.execute(sql_query_1)

cursor.executemany("INSERT INTO Top_tracks VALUES(?, ?, ?,?)", data)
conn.commit()

conn.close()