import os
from dotenv import load_dotenv
from config.database_config import DatabaseConfig

# Loading environment variables from the .env file
load_dotenv()

class ConfigLoader:
    @staticmethod
    def load_config(env="development"):
        """Carga la configuración de la base de datos según el entorno especificado."""
        if env == "development":
            return DatabaseConfig(
                server=os.getenv("DEV_DB_SERVER", "localhost"),
                database=os.getenv("DEV_DB_DATABASE", "MovieRentalDB"),
                username=os.getenv("DEV_DB_USERNAME", "SA"),
                password=os.getenv("DEV_DB_PASSWORD", "MyStrongPass123")
            )
        elif env == "production":
            return DatabaseConfig(
                server=os.getenv("PROD_DB_SERVER"),
                database=os.getenv("PROD_DB_DATABASE"),
                username=os.getenv("PROD_DB_USERNAME"),
                password=os.getenv("PROD_DB_PASSWORD")
            )
        else:
            raise ValueError(f"Unknown environment: {env}")
