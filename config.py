import os

class Config(object):
    # Flask
    SECRET_KEY = os.environ.get("SECRET_KEY")

    # SQL Database
    SQL_SERVER = os.environ.get("SQL_SERVER")
    SQL_DATABASE = os.environ.get("SQL_DATABASE")
    SQL_USER_NAME = os.environ.get("SQL_USER_NAME")
    SQL_PASSWORD = os.environ.get("SQL_PASSWORD")

    SQLALCHEMY_DATABASE_URI = (
    "mssql+pyodbc://{user}:{password}@{server}:1433/{database}"
    "?driver=ODBC+Driver+18+for+SQL+Server"
    "&Encrypt=yes"
    "&TrustServerCertificate=no"
    ).format(
        user=SQL_USER_NAME,
        password=SQL_PASSWORD,
        server=SQL_SERVER,
        database=SQL_DATABASE
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Blob Storage
    BLOB_ACCOUNT = os.environ.get("BLOB_ACCOUNT")
    BLOB_CONTAINER = os.environ.get("BLOB_CONTAINER")
    BLOB_STORAGE_KEY = os.environ.get("BLOB_STORAGE_KEY")

    # Microsoft Auth (leave placeholders for now)
    CLIENT_SECRET = "ENTER_CLIENT_SECRET_HERE"
    CLIENT_ID = "ENTER_CLIENT_ID_HERE"
    AUTHORITY = "https://login.microsoftonline.com/common"
    REDIRECT_PATH = "/getAToken"
    SCOPE = ["User.Read"]

    SESSION_TYPE = "filesystem"
