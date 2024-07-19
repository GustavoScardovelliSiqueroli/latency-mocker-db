def create_mocked_query(column_id_name,
                        columns): return f"""CREATE TABLE `mocked_table` 
                        (`{column_id_name}` INT NOT NULL AUTO_INCREMENT,
                        {columns} PRIMARY KEY (`{column_id_name}`)
                        ) COLLATE='utf8mb4_general_ci';"""


def create_column_varchar_255_query(column_name): return f"{column_name} TEXT ,"


def insert_table(table_name, columns, values): return f"INSERT INTO `{table_name}` ({columns}) VALUES {values};"


def select_table(table_name): return f"SELECT * FROM {table_name};"


def update_column_table(table_name, column_name): return f"UPDATE {table_name} SET {column_name} = " + '"UPDATED";'


def delete_data_table(table_name
                      ): return (f"DELETE FROM {table_name}" +
                                 " WHERE column0 = "
                                 + '"asdyagyudgasduasgduyasgduasgudgasudagsu'
                                   'dygasudasbdashdiasdnasidnasidnasd";')


def delete_table(table_name): return f"DROP TABLE {table_name};"


def delete_database(database_name): return f"DROP DATABASE {database_name};"


class QueryService:

    @staticmethod
    def create_mocked_table(number_of_column: int):
        all_columns = ""

        for x in range(number_of_column):
            column_name = f"column{x}"
            all_columns += f"""

        {create_column_varchar_255_query(column_name)}"""

        query = create_mocked_query("id_mocked", all_columns)
        return query

    @staticmethod
    def mock_data_mocked_table(column_quantity: int, row_quantity=1):
        all_columns = ""
        all_values = ""
        for i in range(column_quantity):
            all_columns += f"`column{i}`,"
        all_columns = all_columns[:-1]

        for i in range(column_quantity):
            all_values += "'asdyagyudgasduasgduyasgduasgudgasudagsudygasudasbdashdiasdnasidnasidnasd', "

        all_values = f"({all_values[:-2]}), "
        line_main = all_values
        if row_quantity > 1:
            for i in range(row_quantity - 1):
                all_values += line_main

        all_values = f"{all_values[:-2]}"

        insert = insert_table("mocked_table", all_columns, all_values)
        return insert

    @staticmethod
    def select_mocked_data():
        return select_table("mocked_table")

    @staticmethod
    def update_column_mocked_data():
        return update_column_table("mocked_table", "column0")

    @staticmethod
    def delete_mocked_data():
        return delete_data_table("mocked_table")

    @staticmethod
    def delete_table_mocked():
        return delete_table("mocked_table")

    @staticmethod
    def delete_database_mocked():
        return delete_database("mock_test_db")
