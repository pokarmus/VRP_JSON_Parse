import json

import mysql.connector

host = None
port = None
database = None
user = None
password = None
table = None
params_path = "db.json"


def get_connection(from_file=True):
    set_connection_params(from_file)
    return mysql.connector.connect(user=user, password=password, host=host,
                                   port=port, database=database)


def write_multiple_data(sql, data):
    connection = get_connection()
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
        return lista


def set_connection_params(from_file=True):
    if from_file:
        params = read_db_params()[0]
        global host, port, database, user, password, table
        host = params["host"]
        port = params["port"]
        database = params["schema"]
        table = params["table"]
        user = params["user"]
        password = params["password"]


def get_database_details():
    set_connection_params()
    details = [database, table]
    return details
