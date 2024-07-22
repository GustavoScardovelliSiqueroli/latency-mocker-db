from factories.connection_factory import ConnectionFactory
from services.database_service import DatabaseService
from controllers.terminal_controller import TerminalController


def start():
    factory = ConnectionFactory(config_path='./confs.yaml')
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

    return connection, db_service


if __name__ == '__main__':
    start()
