import os
from dotenv import load_dotenv

load_dotenv()

APP_USER = os.getenv("APP_USER")
APP_PASSWORD = os.getenv("APP_PASSWORD")
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")