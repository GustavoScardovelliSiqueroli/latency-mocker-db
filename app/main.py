from app.controllers.terminal_controller import TerminalController
from app.factories.connection_factory import ConnectionFactory
from app.services.database_service import DatabaseService
import os

def start():
    config_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'config.yaml'))
    factory = ConnectionFactory(config_path=config_path)
    connection = factory.create_connection()
    db_service = DatabaseService(connection)
    try:
        db_service.create_database_mock()
    except Exception as e:
        print(f"Error: '{e}'")

    connection.close()
    connection = factory.create_db_connection_mock()

    terminal_controller = TerminalController(connection)
    terminal_controller.start()

    return connection, db_service, terminal_controller


if __name__ == '__main__':
    start()
