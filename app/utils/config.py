import os


SERVICE_ROOT = os.path.abspath(os.path.dirname(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(SERVICE_ROOT, os.pardir))
SERVICE_NAME = os.environ.get("SERVICE_NAME", "severino-api")
COMMIT = os.environ.get("COMMIT") or "COMMIT"
DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT", "3306")
DB_POOL_SIZE = int(os.environ.get("DB_POOL_SIZE", "-1"))
DATABASE_URL = os.environ.get("DATABASE_URL") or "sqlite:///./sql_app.db"




