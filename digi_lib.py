import json
import networkx as nx

with open('digimon_id.json') as f:
    ID_DICT = json.load(f)

def get_digi_graph():
    with open('digivolution_chart.json') as f:
        digi_chart_json = json.load(f)

    # Restructure digi_chart_json
    digi_chart = []
    for t in digi_chart_json.items():
        for i in t[1]:
            digi_chart.append((t[0], i))

    G = nx.Graph()
    G.add_edges_from(digi_chart)

    return G

def find_digi_id(name):
    for i in ID_DICT:
        if ID_DICT[i].lower() == name.lower():
            return i
    
    return 0

def replace_by_name(paths_by_id):
    paths_by_name = []

    for path in paths_by_id:
        if type(path) == list:
            path_by_name = []
            for i in path:
                path_by_name.append(ID_DICT[i])
            paths_by_name.append(path_by_name)
        else:
            paths_by_name.append(ID_DICT[path])

    return paths_by_name
