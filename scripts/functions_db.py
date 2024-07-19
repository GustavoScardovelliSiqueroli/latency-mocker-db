import mysql.connector
from mysql.connector import Error
import scripts.querys as q
from colorama import Fore, Style, init


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
