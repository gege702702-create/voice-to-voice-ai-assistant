"""
config.py
---------
Reads settings (such as the Cohere API key) from a .env file.
"""

import os
from dotenv import load_dotenv

# Load variables from the .env file in the same folder
load_dotenv()

COHERE_API_KEY = os.getenv("COHERE_API_KEY")

if not COHERE_API_KEY:
    raise ValueError(
        "COHERE_API_KEY was not found. "
        "Make sure you created a .env file and put your key in it (see .env.example)."
    )
