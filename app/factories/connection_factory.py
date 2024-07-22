import mysql.connector
import yaml
from pathlib import Path


class ConnectionFactory:
    def __init__(self, config_path='config.yaml'):
        self.config_path = config_path
        self.config = self.load_config()

    def load_config(self):
        config_path = Path(self.config_path).resolve()
        with open(config_path, 'r') as file:
            config = yaml.safe_load(file)
        return config['database']

    def create_connection(self):
        db_config = self.config
        return mysql.connector.connect(
            host=db_config["host"],
            user=db_config["user"],
            password=str(db_config["password"])
        )

    def create_db_connection_mock(self):
        db_config = self.config
        return mysql.connector.connect(
            host=db_config["host"],
            user=db_config["user"],
            password=str(db_config["password"]),
            database="mock_test_db",
        )
