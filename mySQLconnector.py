import json

import mysql.connector

host = None
port = None
database = None
user = None
password = None
table = None
params_path = "db.json"


def get_connection(host, port, database, user, password):
    return mysql.connector.connect(user=user, password=password, host=host,
                                   port=port, database=database)


def get_connection_from_params():
    set_connection_params_from_file()
    return mysql.connector.connect(user=user, password=password, host=host,
                                   port=port, database=database)


def read_data(query):
    connection = get_connection_from_params()
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    connection.close()
    return result


def write_multiple_data(sql, data):
    connection = get_connection_from_params()
    cursor = connection.cursor()
    cursor.executemany(sql, data)

    connection.commit()
    print("\n", cursor.rowcount, "record inserted to DB.")
    connection.close()


def read_db_params():
    with open(params_path, 'r', encoding='UTF8') as f:
        data = json.load(f)
        lista = []
        for i in data:
            lista.append(i["params"])
        # for j in lista["params"]:
        return lista


def set_connection_params_from_file():
    params = read_db_params()[0]
    global host, port, database, user, password, table
    host = params["host"]
    port = params["port"]
    database = params["schema"]
    table = params["table"]
    user = params["user"]
    password = params["password"]


def get_database_details():
    set_connection_params_from_file()
    details = [database, table]
    return details
