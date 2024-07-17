import mysql.connector
from mysql.connector import Error
import scripts.querys as q
from colorama import Fore, Style, init


def create_server_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
        print(Fore.GREEN + "MySQL Database connection successful\n")
    except Error as err:
        print(Fore.RED + f"Error: '{err}'\n")

    return connection

def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print(Fore.GREEN + "Database created successfully")
    except Error as err:
        print(Fore.YELLOW + f"Error: '{err}'")
        raise

def create_database_mock(connection):
    create_database(connection, "CREATE DATABASE mock_test_db");

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Error as err:
        raise err


def create_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
    except Error as err:
        print(Fore.RED + f"Error: '{err}'")

    return connection

def create_mocked_table(connection, number_of_column: int):
    all_columns = ""

    for x in range(number_of_column):
        column_name = f"column{x}"
        all_columns += f"""

    {q.create_column_varchar_255_query(column_name)}"""

    query =  q.create_mocked_query("id_mocked", all_columns)
    try:
        execute_query(connection, query)
    except Error as err:
        print(Fore.YELLOW + f"Error: '{err}'")
        raise err

def mock_datas_mocked_table(column_quantity: int, row_quantity = 1):
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

    insert = q.insert_table("mocked_table", all_columns, all_values)
    return insert

def generate_sql_file(query, path_sql):
    with open(path_sql, 'w') as file:
        file.write(query)

def execute_sql_file(connection, file_path):
    cursor = connection.cursor()
    with open(file_path, 'r') as file:
        sql_script = file.read()
    try:
        cursor.execute(sql_script)
        connection.commit()
        print(Fore.GREEN + "SQL script executed successfully")
    except Error as err:
        print(Fore.RED + f"Error: '{err}'")
        raise err

