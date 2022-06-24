import errno
from importJSON import *
import csv
import os


def write_all_data_to_csv(file, file_path, is_group):
    data = read_json(file)
    lista = read_routes_from_json(data)
    dump_coord = read_dump_coord(data)
    dir_f = str(create_dir(file_path))
    nazwa_scalony = "Trasa_calosc.txt"
    path_scalony = os.path.normpath(os.path.join(dir_f, nazwa_scalony))
    vehicle_name = "Brak"

    with open(path_scalony, 'w', encoding='UTF8', newline='') as csv_sc:
        naglowek = ["order", "address", "lng", "lat", "dist_from_prev", "group"] if is_group \
            else ["order", "address", "lng", "lat", "dist_from_prev"]
        writer_sc = csv.writer(csv_sc)
        for i in lista:
            nazwa = (str(get_vehicle_from_route((read_single_route(i)))["id"]) + "_trasa_" + str(i["id"]) + ".csv")
            path = os.path.normpath(os.path.join(dir_f, nazwa))

            if len(get_locations_from_route(read_single_route(i))) > 0:
                print(path)
                with open(path, 'w', encoding='UTF8', newline='') as csv_f:
                    writer = csv.writer(csv_f)
                    writer.writerow(naglowek)
                    if get_vehicle_from_route((read_single_route(i)))["id"] != vehicle_name:
                        vehicle_name = get_vehicle_from_route((read_single_route(i)))["id"]
                        csv_line = [vehicle_name, "Start",
                                    str(get_vehicle_start_coord_from_route((read_single_route(i)))["lng"]),
                                    str(get_vehicle_start_coord_from_route((read_single_route(i)))["lat"]), "0", "0"]
                        writer_sc.writerow(csv_line)
                        writer_sc.writerow("")
                    locations = get_locations_from_route(read_single_route(i))

                    add_data = get_all_add_data_from_route(read_single_route(i), is_group)
                    counter = 1
                    if is_group:
                        for j in locations:
                            group = add_data[counter-1]["groupId"]
                            if group == "None":
                                group = ""
                            csv_line = [str(counter), str(j["id"]).replace(",", ""), (j["coordinates"])["lng"], (j["coordinates"])["lat"],
                                        add_data[counter-1]["distanceFromPreviousPoint"], group]
                            writer.writerow(csv_line)
                            writer_sc.writerow(csv_line)
                            counter += 1
                    else:
                        for j in locations:
                            csv_line = [str(counter), str(j["id"]).replace(",", ""), (j["coordinates"])["lng"], (j["coordinates"])["lat"],
                                        add_data[counter - 1]["distanceFromPreviousPoint"]]
                            writer.writerow(csv_line)
                            writer_sc.writerow(csv_line)
                            counter += 1
                    writer_sc.writerow("")
                    csv_line = ("R", "RIPOK", str(dump_coord["lng"]), str(dump_coord["lat"]), 0, 0)
                    writer_sc.writerow(csv_line)
                    writer_sc.writerow("")
                    csv_f.close()
        csv_sc.close()


def get_file_name(file_path):
    name = os.path.basename(file_path)
    name_pos = name.find(".")
    return name[0:name_pos]


def create_dir(file_path):
    dir_f = get_file_name(file_path)
    try:
        os.makedirs(dir_f)
        print("Utworzono katalog: " + dir_f)
    except OSError as e:
        print("\nKatalog " + dir_f + " już istnieje, nadpisuję pliki:")
        if e.errno != errno.EEXIST:
            raise
    return dir_f
