from createCSV import *
from importJSON import *
from mySQLconnector import write_multiple_data, get_database_details


def create_records_g(file, file_path, is_group):
    data = read_json(file)
    lista = read_routes_from_json(data)
    output = []
    for i in lista:
        file_name = get_file_name(file_path)
        route = (str(get_vehicle_from_route((read_single_route(i)))["id"]) + "_trasa_" + str(i["id"]))

        locations = get_locations_from_route(read_single_route(i))
        add_data = get_all_add_data_from_route(read_single_route(i), is_group)

        counter = 1
        for j in locations:
            order = str(counter)
            location_id = j["id"]
            longitude = (j["coordinates"])["lng"]
            latitude = (j["coordinates"])["lat"]
            service_duration = add_data[counter - 1]["serviceDuration"]
            demand = add_data[counter - 1]["demand"]
            distance_from_previous_point = add_data[counter - 1]["distanceFromPreviousPoint"]
            road_duration_from_previous_point = add_data[counter - 1]["roadDurationFromPreviousPoint"]

            group = add_data[counter - 1]["groupId"] if is_group else "0"
            if group == "None":
                group = ""

            temp_output = (file_name, route, order, location_id, longitude, latitude, service_duration, demand,
                           distance_from_previous_point, road_duration_from_previous_point, group) if is_group else \
                (file_name, route, order, location_id, longitude, latitude, service_duration, demand,
                 distance_from_previous_point, road_duration_from_previous_point)
            output.append(temp_output)

            counter += 1
    return output


def get_sql_query():
    return "INSERT INTO " + str(get_database_details()[0]) + "." + str(get_database_details()[1]) + \
           " (file_name, route, order_in_route, location_id, longitude, latitude, serviceDuration, " \
          "demand, distanceFromPreviousPoint, roadDurationFromPreviousPoint) " \
          "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"


def get_sql_query_g():
    return "INSERT INTO " + str(get_database_details()[0]) + "." + str(get_database_details()[1]) + \
           " (file_name, route, order_in_route, location_id, longitude, latitude, serviceDuration, " \
          "demand, distanceFromPreviousPoint, roadDurationFromPreviousPoint, groupId) " \
          "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"


def write_data_to_db_g(file, file_path, is_group):
    write_multiple_data(get_sql_query_g(), create_records_g(file, file_path, True)) if is_group else \
        write_multiple_data(get_sql_query(), create_records_g(file, file_path, False))
