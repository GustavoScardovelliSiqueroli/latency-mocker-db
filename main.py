import scripts.functions_db as f
from colorama import Fore, Style, init
import yaml
import time

init(autoreset=True, convert=True)
with open('confs.yaml') as file:
    confs = yaml.safe_load(file)

db_conf = confs['database']
print(db_conf)

def connect_db_create_mockdb():
    connection = f.create_server_connection(str(db_conf["host"]), str(db_conf["user"]), str(db_conf["password"]))
    print(Fore.LIGHTBLUE_EX + "-Script: Creating 'mock-test-db'...")
    try:
        f.create_database_mock(connection)
        connection.close()
    except:
        pass

if __name__ == "__main__":
    print(Fore.LIGHTBLUE_EX +  "\n-Script: Connecting to DB...")
    connect_db_create_mockdb()
    print()

    print(Fore.LIGHTBLUE_EX + "-Script: How many columns should the table have?")
    table_columns_quantity = 0
    while table_columns_quantity < 1:
        try:
            table_columns_quantity: int = int(input("Resp: "))
        except:
            print(Fore.RED + "Integer only\n")
            pass
    
    print()
    connection = f.create_db_connection(str(db_conf["host"]), str(db_conf["user"]), str(db_conf["password"]), "mock_test_db")
    resp = 0
    try:
        f.create_mocked_table(connection, table_columns_quantity)
        resp = 2                     
    except:
        print(Fore.LIGHTBLUE_EX + "-Script: \n1- Delete the table and create a new one \n2- Continue\n")        
        try:
            resp: int = int(input("Resp: "))
        except:
            pass

    while resp < 1:
        try:
            resp: int = int(input("Resp: "))
        except:
            pass

    print()
    if resp not in range(0,3):
        exit()
    
    if resp == 1:
        pass

    print(Fore.LIGHTBLUE_EX + "-Script: Generating query in SQL file...")
    insert_sql = f.mock_datas_mocked_table(table_columns_quantity)  
    f.generate_sql_file(insert_sql, './sql/large_table_data.sql')
    print(Fore.GREEN + "Generated with success..")

    print(Fore.LIGHTBLUE_EX + "-Script: MOCKING 1 ROW...\n")
    start_time_first_query = time.time()
    f.execute_sql_file(connection, './sql/large_table_data.sql') 
    end_time_fisrt_query = time.time()
    print("Runtime " + str(round(end_time_fisrt_query - start_time_first_query, 3)) + "\n")

    print(Fore.LIGHTBLUE_EX + "-Script: How many rows to insert?")
    rows_to_inser = int(input("Resp: "))

    print(Fore.LIGHTBLUE_EX + "\n-Script: Making query...")
    query = f.mock_datas_mocked_table(table_columns_quantity, rows_to_inser)
    print(Fore.GREEN + "Query is ready")
    print(Fore.LIGHTBLUE_EX + f"-Script: MOCKING {rows_to_inser} ROW...\n")
    start_time_many_query = time.time()
    f.execute_query(connection, query)
    end_time_many_query = time.time()
    print("Runtime " + str(round(end_time_many_query - start_time_many_query, 3)))

    print(Fore.LIGHTBLUE_EX + "\n-Script: How many time to insert?")
    times_to_insert = int(input("Resp: "))

    print(Fore.LIGHTBLUE_EX + "\n-Script: Query is running...")
    start_time_many_time_query = time.time()
    for i in range(times_to_insert):
        f.execute_query(connection, query)
    end_time_many_time_query = time.time()
    print("Runtime " + str(round(end_time_many_time_query - start_time_many_time_query, 3)))
    input()

    print(Fore.LIGHTBLUE_EX + "\n-Script: SELECTING ALL DATA...")
    start_time_select = time.time()
    f.select_mocked_data(connection)
    end_time_select = time.time()
    print("Runtime " + str(round(end_time_select - start_time_select, 3)))
    input()

    print(Fore.LIGHTBLUE_EX + "\n-Script: UPDATING ALL DATA...")
    start_time_update = time.time()
    f.update_column_mocked_data(connection)
    end_time_update = time.time()
    print("Runtime " + str(round(end_time_update - start_time_update, 3)))
    input()

    print(Fore.LIGHTBLUE_EX + "\n-Script: DELETING ALL DATA...")
    start_time_delete = time.time()
    f.delete_mocked_data(connection)
    end_time_delete = time.time()
    print("Runtime " + str(round(end_time_delete - start_time_delete, 3)))
    input()

    print(Fore.LIGHTBLUE_EX + "\n-Script: DELETING TABLE...")
    start_time_delete_table = time.time()
    f.delete_table_mocked(connection)
    end_time_delete_table = time.time()
    print("Runtime " + str(round(end_time_delete_table - start_time_delete_table, 3)))
    input()

    print(Fore.LIGHTBLUE_EX + "\n-Script: DELETING DATABASE...")
    start_time_delete_database = time.time()
    f.delete_database_mocked(connection)
    end_time_delete_database = time.time()
    print("Runtime " + str(round(end_time_delete_database - start_time_delete_database, 3)))
    input()





