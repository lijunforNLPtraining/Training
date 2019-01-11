

import  math







station_information = {}





def get_succsssors(froninter, graph):
    return graph[froninter]


def is_goal(node, destination):
    return node ==  destination

def geo_distance(origin, destination):
    """
    Calculate the Haversine distance.

    Parameters
    ----------
    origin : tuple of float
        (lat, long)
    destination : tuple of float
        (lat, long)

    Returns
    -------
    distance_in_km : float

    Examples
    --------
    >>> origin = (48.1372, 11.5756)  # Munich
    >>> destination = (52.5186, 13.4083)  # Berlin
    >>> round(distance(origin, destination), 1)
    504.2
    """
    lat1, lon1 = origin
    lat2, lon2 = destination
    radius = 6371  # km

    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = (math.sin(dlat / 2) * math.sin(dlat / 2) +
         math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) *
         math.sin(dlon / 2) * math.sin(dlon / 2))
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    d = radius * c

    return d

def sort_pathes(pathes,sort_func,beam=1):
    return  sorted(pathes,key= sort_func)[:beam]

def get_station_distance(station1,station2):
    return geo_distance(station_information[station1],station_information[station2])


def get_path_distance(path):
    distance = 0
    for station in path:
        for station2 in path:
            if station == station:continue
            distance += get_station_distance(station,station2)
    return  distance
    

def comprehensive_sort(pathes):
    return sort_pathes(pathes, lambda p: (len(p) + get_path_distance(p)), beam=30)

def mini_change_station(pathes):
    return sort_pathes(pathes, lambda p: len(p), beam=-1)

def min_distance(pathes):
    return sort_pathes(pathes, lambda p:get_path_distance(p), beam=-1)

