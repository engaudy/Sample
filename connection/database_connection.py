import pyodbc

# Class to manage the database connection
class DatabaseConnection:
    def __init__(self, config):
        self.config = config
        self.connection = None

    def connect(self):
        try:
            self.connection = pyodbc.connect(self.config.get_connection_string())
            print("Successfully connected to the database.")
        except Exception as e:
            print("Error connecting to the database:", e)

    def close_connection(self):
        if self.connection:
            self.connection.close()
            print("Connection closed.")
