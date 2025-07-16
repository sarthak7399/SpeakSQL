from langchain_community.utilities import SQLDatabase
import pymysql # Ensure pymysql is imported if it's used internally by SQLDatabase.from_uri
import os # Assuming environment variables are passed or accessed

def initialize_database(db_user: str, db_password: str, db_host: str, db_port: str, db_name: str, wanna_print: bool = True):
    """
    Connects to the MySQL database and retrieves its schema information.

    Args:
        db_user (str): MySQL database username.
        db_password (str): MySQL database password.
        db_host (str): MySQL database host.
        db_port (str): MySQL database port.
        db_name (str): MySQL database name.

    Returns:
        tuple: A tuple containing:
            - db (SQLDatabase): The initialized LangChain SQLDatabase object.
            - database_schema (str): The schema information string from the database.
        Exits the program if the database connection fails.
    """
    print("--- Connecting to MySQL Database and Fetching Schema ---")
    try:
        db = SQLDatabase.from_uri(
            f"mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}",
            sample_rows_in_table_info=3 # Helps Gemini understand data types and typical values
        )
        database_schema = db.table_info

        if wanna_print:
            print("Database Schema:\n", database_schema)
            print("---------------------------------------------------\n")
        print("Database connected successfully.")
        return db, database_schema
    except Exception as e:
        print(f"Error connecting to database or fetching schema: {e}")
        print("Please ensure MySQL is running, your .env variables are correct, and pymysql is installed.")
        exit() # Exit if database connection fails, as further steps depend on it.

# --- How you would use this function in your main script: ---

# Assuming these variables are loaded from .env or defined elsewhere
# db_user = os.getenv("db_user")
# db_password = os.getenv("db_password")
# db_host = os.getenv("db_host")
# db_port = os.getenv("db_port")
# db_name = os.getenv("db_name")

# db, database_schema = initialize_database(db_user, db_password, db_host, db_port, db_name)