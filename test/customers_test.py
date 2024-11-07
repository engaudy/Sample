import sys
import os

# Adding the project root directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from config import ConfigLoader
from processing import DatabaseProcessor
import os

# Main execution
if __name__ == "__main__":
    env = os.getenv("APP_ENV", "development")
    print(f"Starting application in '{env}' environment.")

    try:
        config = ConfigLoader.load_config(env)
        print(f"Connecting to database '{config.database}' at '{config.server}' for '{env}' environment.")

        processor = DatabaseProcessor(config)
        processor.connect()

        query = "SELECT * FROM dbo.Customers"
        processor.fetch_data(query)

        expectations_file = "./validation/great_expectations.yml"
        processor.validate_data(expectations_file)

    except Exception as e:
        print("Critical error:", e)

    finally:
        processor.close_connection()
