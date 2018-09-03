import json
import sys
import networkx as nx

from pprint import pprint

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

def find_digi_id(id_dict, name):
    for i in id_dict:
        if id_dict[i].lower() == name.lower():
            return i
    
    return 0

def replace_by_name(id_dict, paths_by_id):
    paths_by_name = []

    for path in paths_by_id:
        path_by_name = []
        for i in path:
            path_by_name.append(id_dict[i])
        paths_by_name.append(path_by_name)

    return paths_by_name


if __name__ == '__main__':
    G = get_digi_graph()
    with open('digimon_id.json') as f:
        digi_id = json.load(f)

    source = sys.argv[1]
    target = sys.argv[2]

    if not source.isdigit():
        source = find_digi_id(digi_id, source)
        if not source:
            raise NameError('Digimon name "%s" not found.' % sys.argv[1])

    if not target.isdigit():
        target = find_digi_id(digi_id, target)
        if not target:
            raise NameError('Digimon name "%s" not found.' % sys.argv[2])

    p_id = list(nx.all_shortest_paths(G, source, target))
    p_name = replace_by_name(digi_id, p_id)
    pprint(p_name)
