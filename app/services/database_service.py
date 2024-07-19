from mysql.connector import Error


class DatabaseService:

    def __init__(self, connection) -> None:
        self.connection = connection

    def create_database_mock(self):
        cursor = self.connection.cursor()
        try:
            cursor.execute("CREATE DATABASE mock_test_db")
        except Error as err:
            print(f"Error: '{err}'")
            raise err

    def execute_query(self, query):
        cursor = self.connection.cursor()
        try:
            cursor.execute(query)
            self.connection.commit()
        except Error as err:
            print(f"Error: '{err}'")
            raise err
