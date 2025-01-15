import os
from dotenv import load_dotenv


# Завантаження змінних з файлу .env
load_dotenv()


class Data:

    LOGIN = os.getenv('LOGIN')
    PASSWORD = os.getenv('PASSWORD')
