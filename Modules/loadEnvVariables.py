import os
from dotenv import load_dotenv

def load_environment_variables():
    """
    Loads environment variables from a .env file and returns them as a dictionary.

    Returns:
        dict: A dictionary containing the loaded environment variables.
              Returns None for any variable that is not found.
    """
    print("--- Loading Environment Variables ---")
    load_dotenv() # This loads variables from a .env file

    env_vars = {
        'GOOGLE_API_KEY': os.getenv('GOOGLE_API_KEY'),
        'db_user': os.getenv("db_user"),
        'db_password': os.getenv("db_password"),
        'db_host': os.getenv("db_host"),
        'db_port': os.getenv("db_port"),
        'db_name': os.getenv("db_name")
    }

    # Optional: Print a warning if any critical variable is missing
    for key, value in env_vars.items():
        if value is None:
            print(f"Warning: Environment variable '{key}' not found. Please check your .env file.")

    print("Environment variables loaded.")
    return env_vars

# --- How you would use this function in your main script: ---

# env_vars = load_environment_variables()
# GOOGLE_API_KEY = env_vars.get('GOOGLE_API_KEY')
# db_user = env_vars.get('db_user')
# db_password = env_vars.get('db_password')
# db_host = env_vars.get('db_host')
# db_port = env_vars.get('db_port')
# db_name = env_vars.get('db_name')