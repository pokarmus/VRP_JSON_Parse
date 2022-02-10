import sys

from createCSV import *
from writeToDB import write_data_to_db_g

if __name__ == '__main__':

    data = ""
    json_type = sys.argv[1]
    import_type = sys.argv[2]
    file_path = sys.argv[3]

# Testowy skrypt

    # file = open('src/test_1plik_we_2poj.txt', 'r', encoding='utf8')
    # #file = open('src/test_1plik_we.txt', 'r', encoding='utf8')
    # write_all_data_to_csv_g(file, 'src/XXGr', True)
    # file.close()
    # file = open('src/test_1plik_we_2poj.txt', 'r', encoding='utf8')
    # write_data_to_db_g(file, "src/test_1plik_we_2poj.txt", False)
    # file.close()

# Koniec testowego

    if json_type == "VRP 1.0":
        if import_type.lower().__contains__("csv"):
            file = open(file_path, 'r', encoding='utf8')
            write_all_data_to_csv_g(file, file_path, False)
            file.close()
        if import_type.lower().__contains__("db"):
            file = open(file_path, 'r', encoding='utf8')
            write_data_to_db_g(file, file_path, False)
            file.close()

    else:
        if json_type == "VRP 1.0G":
            if import_type.lower().__contains__("csv"):
                file = open(file_path, 'r', encoding='utf8')
                write_all_data_to_csv_g(file, file_path, True)
                file.close()
            if import_type.lower().__contains__("db"):
                file = open(file_path, 'r', encoding='utf8')
                write_data_to_db_g(file, file_path, True)
                file.close()
