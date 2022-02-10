import json


def read_routes_from_json(data):
    lista = []
    for i in data["routes"]:
        lista.append(i)
    return lista


def read_json(file):
    data = json.load(file)
    return data


def read_single_route(route):
    data = route
    lista = [data["vehicle"]]
    for i in data["points"]:
        lista.append(i)
    return lista


def get_vehicle_from_route(route):
    return route[0]


def get_vehicle_start_coord_from_route(route):
    return (((route[0])["startingPoint"])["location"])["coordinates"]


def get_locations_from_route(route):
    data = route[1:len(route)]
    lista = []
    for i in data:
        lista.append(i["location"])  # + i["distanceFromPreviousPoint"])
    return lista


def get_all_add_data_from_route(route, is_group):
    data = route[1:len(route)]
    lista = []
    lista.clear()
    if is_group:
        for i in data:
            lista.append({"serviceDuration": str(i["serviceDuration"]), "groupId": str(i["groupId"]),
                          "demand": str(i["demand"]), "distanceFromPreviousPoint": str(i["distanceFromPreviousPoint"]),
                          "roadDurationFromPreviousPoint": str(i["roadDurationFromPreviousPoint"])})
    else:
        for i in data:
            lista.append({"serviceDuration": str(i["serviceDuration"]),
                          "demand": str(i["demand"]), "distanceFromPreviousPoint": str(i["distanceFromPreviousPoint"]),
                          "roadDurationFromPreviousPoint": str(i["roadDurationFromPreviousPoint"])})
    return lista


def get_vehicle_name(vehicle):
    return vehicle["id"]


def read_dump_coord(data):
    coord = ((data["dump"])["location"])["coordinates"]
    return coord
