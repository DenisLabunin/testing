from dotenv import load_dotenv
import os


class Data:
    load_dotenv()
    LOGIN = os.getenv("LOGIN")
    PASSWORD = os.getenv("PASSWORD")
