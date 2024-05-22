from dotenv import load_dotenv
import os

load_dotenv()


class Data:
    LOGIN = os.getenv("LOGIN")
    PASSWORD = os.getenv("PASSWORD")
