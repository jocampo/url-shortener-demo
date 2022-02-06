import os

from dotenv import load_dotenv

from config.environments import Environment

# Takes configs from .env file and loads them into the os.environ dict
load_dotenv()  # take environment variables from .env.


# TODO: temporary placeholder for db url
def load_database_config():
    f"""
    Takes the db settings from the environment variables and concatenates them into the database url
    :except {AssertionError} if a required field for the database url is missing
    :return: valid database URL
    """
    env = os.environ["ENV"]
    if env == Environment.LOCAL:
        return "sqlite:///url_shortener.db"

    db_user = os.environ["DB_USER"]
    db_pass = os.environ["DB_PASSWORD"]
    db_name = os.environ["DB_NAME"]
    db_port = os.environ["DB_PORT"]
    db_host = os.environ["DB_HOST"]

    assert db_user and db_port and db_host and db_name, "Missing required fields for db connection... aborting"

    return f"postgresql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}"


DATABASE_URL = load_database_config()
