import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY') or 'fallback_secret'
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL') or 'sqlite:///app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY') or ''

    MAIL_SERVER = os.getenv('MAIL_SERVER') or 'localhost'
    MAIL_PORT = int(os.getenv('MAIL_PORT') or 587)
    MAIL_USERNAME = os.getenv('MAIL_USERNAME') or ''
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD') or ''
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
