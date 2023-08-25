from dotenv import load_dotenv
import os

load_dotenv()

# SECRET_KEY project django

SECRET_KEY = os.getenv("SECRET_KEY")

#my_data_instagram
My_Phone = os.getenv("My_Phone")
My_Password = os.getenv("My_Password")