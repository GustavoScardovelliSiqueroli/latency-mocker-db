from app.services.terminal_service import TerminalService
from app.services.query_service import QueryService
from app.services.database_service import DatabaseService
from colorama import Fore

class TerminalController:
    def __init__(self, connection):
        self.terminal_service = TerminalService()
        self.database_service = DatabaseService(connection)
        self.times = {}
        self.q = QueryService
        self.column_quantity = 1
        self.rows_quantity = 1

    def start(self):

        try:
            self.times["create_table"] = self.terminal_service.time_exec_message(
                lambda:
                self.database_service.execute_query(
                    self.q.create_mocked_table(
                        self.set_column_quantity())),
                "How many columns should the table have?",
                "Table created with success!\n"
            )
        except Exception as e:
            print(f"{e}\n")

        query = self.q.mock_data_mocked_table(self.column_quantity)
        self.times["insert_1"] = self.terminal_service.time_exec_message(
            lambda:
            self.database_service.execute_query(query),
            "Inserting 1 row...",
            "1 row has been inserted\n"
        )

        query = self.q.mock_data_mocked_table(self.column_quantity, self.set_rows_quantity())
        self.times[f"insert_{self.rows_quantity}"] = self.terminal_service.time_exec_message(
            lambda:
            self.database_service.execute_query(
                query),
            f"Inserting {self.rows_quantity} rows...",
            f"{self.rows_quantity} rows has been inserted\n"
        )

        query = self.q.select_mocked_data()
        self.times[f"select_data"] = self.terminal_service.time_exec_message(
            lambda:
            self.database_service.execute_query(
                query),
            f"SELECTING ALL DATA...",
            f"All data is selected with success\n"
        )
        query = self.q.update_column_mocked_data()
        self.times[f"update_data"] = self.terminal_service.time_exec_message(
            lambda:
            self.database_service.execute_query(
                query),
            f"UPDATING ALL DATA...",
            f"All data is updated with success\n"
        )

        query = self.q.delete_mocked_data()
        self.times[f"delete_data"] = self.terminal_service.time_exec_message(
            lambda:
            self.database_service.execute_query(
                query),
            f"DELETING ALL DATA...",
            f"All data is deleted with success\n"
        )

        query = self.q.delete_table_mocked()
        self.times[f"delete_table"] = self.terminal_service.time_exec_message(
            lambda:
            self.database_service.execute_query(
                query),
            f"DELETING TABLE...",
            f"Table is deleted with success\n"
        )

        query = self.q.delete_database_mocked()
        self.times[f"delete_db"] = self.terminal_service.time_exec_message(
            lambda:
            self.database_service.execute_query(
                query),
            f"DELETING DATABASE...",
            f"database is deleted with success\n"
        )

        print(self.times)

    def test_func(self):
        print("ola, esse é o teste")
        return "mensagem de retorno do teste"

    def set_column_quantity(self):
        self.column_quantity = int(input("Resp: "))
        return self.column_quantity

    def set_rows_quantity(self):
        print(Fore.LIGHTBLUE_EX + f'-Script: How many rows?')
        self.rows_quantity = int(input("Resp: "))
        print()
        return self.rows_quantity
