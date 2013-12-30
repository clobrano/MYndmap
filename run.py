#!/usr/bin/env python
from networkx import networkx as nx
from matplotlib import pyplot as plt
from listparser import *

def plot(graph, node):
    for child in node.children:
        graph.add_node(node.rtf_note)
        graph.add_edge(node.rtf_note, child.rtf_note)
        print '\t'*(node.indent_lev+1), node.id, '->', child.id
        plot(graph, child)


if __name__ == '__main__':
    ls = ListParser()

    notes = [line for line in open('testNote.md', 'r')]
    ls.parse(notes)

    mymap = ls.myndmap

    root = mymap.root
    graph = nx.Graph()
    plot(graph, root)
    print(graph.nodes())
    print(graph.edges())
    nx.draw_graphviz(graph)
    plt.show()