from dotenv import find_dotenv, load_dotenv
import os

load_dotenv(find_dotenv())

API_KEY = os.getenv("API_KEY")

BASE_URL = 'https://tasks.aidevs.pl/'

BASE_OPENAI_URL = 'https://api.openai.com/v1/'

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

