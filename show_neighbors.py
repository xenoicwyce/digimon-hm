import json
import sys
import networkx as nx

from digi_lib import get_digi_graph, find_digi_id, replace_by_name

if __name__ == '__main__':
    G = get_digi_graph()

    node = sys.argv[1]
    if not node.isdigit():
        node = find_digi_id(node)

    neighbors = replace_by_name(G.neighbors(node))
    print(neighbors)
