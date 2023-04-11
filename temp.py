import os

from dotenv import load_dotenv

load_dotenv()

NAME = os.getenv("Daquiver")
print(NAME)
