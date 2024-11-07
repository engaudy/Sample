import pandas as pd
from connection.database_connection import DatabaseConnection
from validation.validator import DataValidator

class DatabaseProcessor:
    def __init__(self, config):
        self.config = config
        self.db_connection = None
        self.data = None

    def connect(self):
        """Establish a database connection."""
        self.db_connection = DatabaseConnection(self.config)
        self.db_connection.connect()

    def fetch_data(self, query):
        """Execute a SQL query and retrieve data as a pandas DataFrame."""
        if self.db_connection is None:
            raise ConnectionError("No database connection available.")
        self.data = pd.read_sql(query, self.db_connection.connection)
        return self.data

    def close_connection(self):
        """Close the database connection."""
        if self.db_connection:
            self.db_connection.close_connection()

    def validate_data(self, expectations_file):
        """Initialize data validation process."""
        if self.data is not None:
            validator = DataValidator(self.data, expectations_file)
            validator.run_validations()
        else:
            print("No data available for validation.")
