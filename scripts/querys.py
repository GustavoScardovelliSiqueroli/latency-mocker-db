create_mocked_query = lambda column_id_name, columns: f"""CREATE TABLE `mocked_table` (
    `{column_id_name}` INT NOT NULL AUTO_INCREMENT,
    {columns}
    PRIMARY KEY (`{column_id_name}`)
)
COLLATE='utf8mb4_general_ci';"""

create_column_varchar_255_query = lambda column_name: f"{column_name} TEXT ,"

"""
columns = `column_name_1`, `column_name_2` ...
values = 'value1', 'value2', 'value3' ...
"""
insert_table = lambda table_name, columns, values: f"""
INSERT INTO `{table_name}` ({columns}) VALUES {values};
"""