from dotenv import load_dotenv
import os

load_dotenv()

# SECRET_KEY project django

SECRET_KEY = os.getenv("SECRET_KEY")