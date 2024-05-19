from dotenv import load_dotenv
import os


class Links:
    load_dotenv()
    HOST = os.getenv("URL_SITE")
    LOGIN_PADE = f"{HOST}/admin/login"
    DASHBOARD_PAGE = f"{HOST}/admin/dashboard"
    CREATE_POST_PAGE = f"{HOST}/admin/create"
