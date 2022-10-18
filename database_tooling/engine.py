import os

from sqlalchemy import create_engine

from dotenv import load_dotenv

load_dotenv('.env')

connection_string = os.environ.get("POSTGRESQL_CONNECTION_STRING")
engine = create_engine(connection_string, echo=True, future=True)
