# Configuration file for the application
DB_HOST = 'localhost'
DB_NAME = 'learning_project'
DB_USER = 'postgres'
DB_PASSWORD = 'password'

# Define a function to connect to the database
def connect_to_db():
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        return conn
    except psycopg2.OperationalError as e:
        print(f'Failed to connect to database: {e}')