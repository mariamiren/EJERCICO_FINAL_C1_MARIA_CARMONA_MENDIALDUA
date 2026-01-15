from dotenv import load_dotenv
import os

load_dotenv()

user = os.environ.get('MYSQL_USER')
password = os.environ.get('MYSQL_PASSWORD')
host = os.environ.get('MYSQL_HOST')
port = os.environ.get('MYSQL_HOST_PORT')
database = os.environ.get('MYSQL_DB')


DATABASE_CONNECTION_URI = f"mysql://{user}:{password}@{host}:{port}/{database}"