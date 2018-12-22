import sqlite3


def select_data_from_bd_unic (db, table_name, column_name):
    connections = sqlite3.connect(db)
    query = "SELECT " + column_name + " FROM " + table_name
    result = connections.execute(query)
    list1 = []
    for row_number, row_data in enumerate(result):
        for column_number, data in enumerate(row_data):
            list1.append(data)
            myset = set(list1)
            list1 = list(myset)
    return list1
    connections.close()

def select_data_from_bd (db, table_name, column_name):
    connections = sqlite3.connect(db)
    query = "SELECT " + column_name + " FROM " + table_name
    result = connections.execute(query)
    list1 = []
    for row_number, row_data in enumerate(result):
        for column_number, data in enumerate(row_data):
            list1.append(data)
    return list1
    connections.close()

def select_data_f1_dep_selected_f2(db, select_field, select_from_table, where_field, where_value):
    connections = sqlite3.connect(db)
    query = "SELECT " + select_field + " FROM " + select_from_table + " WHERE " + where_field + " = \"" + where_value + "\""
    result = connections.execute(query)
    list1 = []
    for row_number, row_data in enumerate(result):
        for column_number, data in enumerate(row_data):
            list1.append(data)
    return list1
    connections.close()

def select_data_f1_dep_selected_f2_unic(db, select_field, select_from_table, where_field, where_value):
    connections = sqlite3.connect(db)
    query = "SELECT " + select_field + " FROM " + select_from_table + " WHERE " + where_field + " = \"" + where_value + "\""
    result = connections.execute(query)
    list1 = []
    for row_number, row_data in enumerate(result):
        for column_number, data in enumerate(row_data):
            list1.append(data)
            myset = set(list1)
            list1 = list(myset)
    return list1
    connections.close()

def filter_comboBox_dep_where(db, table_name, column_name, where_field, where_value):
    if where_value == "--All--":
        list2 = select_data_from_bd_unic(db, table_name, column_name)
    else:
        list2 = select_data_f1_dep_selected_f2_unic(db, column_name, table_name,
                                                                     where_field, where_value)
    list1 = []
    for elem2 in list2:
        list1.append(elem2)
    return list1
