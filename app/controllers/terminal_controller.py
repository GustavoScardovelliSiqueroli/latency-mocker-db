from app.services.terminal_service import TerminalService
from app.services.query_service import QueryService
from app.services.database_service import DatabaseService
from app.services.csv_service import CsvService
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
        query = self.q.create_mocked_table(self.set_column_quantity())
        try:
            self.times["create_table"] = self.terminal_service.time_exec_message(
                lambda:
                self.database_service.execute_query(query),
                "Creating table...",
                "Table created with success!\n"
            )
            self.times["create_table"].update({"quantity":f"{self.column_quantity} columns"})
        except Exception as e:
            print(f"{e}\n")

        query = self.q.mock_data_mocked_table(self.column_quantity)
        self.times["insert_1"] = self.terminal_service.time_exec_message(
            lambda:
            self.database_service.execute_query(query),
            "Inserting 1 row...",
            "1 row has been inserted\n"
        )
        self.times["insert_1"].update({"quantity": "1 row"})

        query = self.q.mock_data_mocked_table(self.column_quantity, self.set_rows_quantity())
        self.times[f"insert_{self.rows_quantity}"] = self.terminal_service.time_exec_message(
            lambda:
            self.database_service.execute_query(
                query),
            f"Inserting {self.rows_quantity} rows...",
            f"{self.rows_quantity} rows has been inserted\n"
        )
        self.times[f"insert_{self.rows_quantity}"].update({"quantity": f"{self.rows_quantity} rows"})

        query = self.q.select_mocked_data()
        self.times[f"select_data"] = self.terminal_service.time_exec_message(
            lambda:
            self.database_service.execute_query(
                query),
            f"SELECTING ALL DATA...",
            f"All data is selected with success\n"
        )
        self.times[f"select_data"].update({"quantity": "*"})

        query = self.q.update_column_mocked_data()
        self.times[f"update_data"] = self.terminal_service.time_exec_message(
            lambda:
            self.database_service.execute_query(
                query),
            f"UPDATING ALL DATA...",
            f"All data is updated with success\n"
        )
        self.times[f"update_data"].update({"quantity": "*"})

        query = self.q.delete_mocked_data()
        self.times[f"delete_data"] = self.terminal_service.time_exec_message(
            lambda:
            self.database_service.execute_query(
                query),
            f"DELETING ALL DATA...",
            f"All data is deleted with success\n"
        )
        self.times[f"delete_data"].update({"quantity": "*"})

        query = self.q.delete_table_mocked()
        self.times[f"delete_table"] = self.terminal_service.time_exec_message(
            lambda:
            self.database_service.execute_query(
                query),
            f"DELETING TABLE...",
            f"Table is deleted with success\n"
        )
        self.times[f"delete_table"].update({"quantity": "*"})

        query = self.q.delete_database_mocked()
        self.times[f"delete_db"] = self.terminal_service.time_exec_message(
            lambda:
            self.database_service.execute_query(
                query),
            f"DELETING DATABASE...",
            f"database is deleted with success\n"
        )
        self.times[f"delete_db"].update({"quantity": "*"})

        CsvService.data_to_csv(self.times)

    def set_column_quantity(self):
        print(Fore.LIGHTBLUE_EX + f"How many columns should the table have?")
        self.column_quantity = int(input("Resp: "))
        print()
        return self.column_quantity

    def set_rows_quantity(self):
        print(Fore.LIGHTBLUE_EX + f'-Script: How many rows?')
        self.rows_quantity = int(input("Resp: "))
        print()
        return self.rows_quantity
