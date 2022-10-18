import os

from dotenv import load_dotenv

# Use load_env to trace the path of .env:
load_dotenv('.env')

# Get the values of the variables from .env using the os library:
password = os.environ.get("POSTGRESQL_CONNECTION_STRING")

print(password)
