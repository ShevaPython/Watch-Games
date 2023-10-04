from dotenv import load_dotenv
import os

load_dotenv()

# SECRET_KEY project django

SECRET_KEY = os.getenv("SECRET_KEY")

#my_data_instagram
My_Phone = os.getenv("My_Phone")
My_Password = os.getenv("My_Password")

#SMTP
GMAIL_PASSWORD = os.getenv("GMAIL_PASSWORD")
GMAIL = os.getenv("GMAIL")

#Connect Postgress

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")

#auth googl
SOCIAL_AUTH_GOOGLE_KEY=os.getenv("SOCIAL_AUTH_GOOGLE_KEY")
SOCIAL_AUTH_GOOGLE_SECRET = os.getenv("SOCIAL_AUTH_GOOGLE_SECRET")