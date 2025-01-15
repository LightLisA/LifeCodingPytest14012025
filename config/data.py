import os
from dotenv import load_dotenv


# Завантаження змінних з файлу .env
load_dotenv()


class Data:

    LOGIN = os.getenv('AUTH_LOGIN')
    PASSWORD = os.getenv('AUTH_PASSWORD')
