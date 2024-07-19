from factories.connection_factory import ConnectionFactory
from services.database_service import DatabaseService


def main():
    pass


def start():
    factory = ConnectionFactory()
    connection = factory.create_connection()
    db_service = DatabaseService(connection)
    db_service.create_database_mock()
    connection.close()
    connection = factory.create_db_connection_mock()
    return connection


if __name__ == '__main__':
    main()
