import json
import sys
import networkx as nx

from digi_lib import get_digi_graph, find_digi_id, replace_by_name

if __name__ == '__main__':
    G = get_digi_graph()

    source = sys.argv[1]
    target = sys.argv[2]

    if not source.isdigit():
        source = find_digi_id(source)
        if not source:
            raise NameError('Digimon name "%s" not found.' % sys.argv[1])

    if not target.isdigit():
        target = find_digi_id(target)
        if not target:
            raise NameError('Digimon name "%s" not found.' % sys.argv[2])

    paths = replace_by_name(nx.all_shortest_paths(G, source, target))
    for idx, path in enumerate(paths, start=1):
        print('%s. %s' % (idx, path))
