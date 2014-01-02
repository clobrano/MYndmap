#!/usr/bin/env python
from pydot import Dot, Node, Edge
from listparser import *
from plotter import *

color_list = ['red', 'blue', 'green', 'orange', '#E6E600', 'purple']
light_colors = {'red': '#FFB5C6', 'blue':'#B5B8FF', 'green':'#BEFFB5', 'orange':'#FFE9B5', '#E6E600':'#FFFFB5', 'purple':'#F0B5FF'}
color_index = 0
first_level_children = 0

def get_formatted_text(raw_text):
    msg_words = raw_text.split(' ')
    msg_word_len = len(msg_words)
    formatted_msg_words = []
    for word,idx in zip(msg_words, xrange(len(msg_words))):
        if (idx > 0) and (idx % 5) == 0:
            formatted_msg_words.append('<BR/>')
        formatted_msg_words.append(word)
    shrink_msg = ' '.join(formatted_msg_words)

    return '<%s>' % shrink_msg

def get_node(myndnode):
    global light_colors
    formatted_text = get_formatted_text(myndnode.rtf_note)

    if myndnode.parent is None:
        node = Node(myndnode.rtf_note,
                shape='plaintext',
                #style='rounded',
                color='black',
                fontcolor='black',
                fontname='din',
                fontsize='22')
        #graph.root = node
        return node

    print formatted_text
    return Node(myndnode.id,
                label=formatted_text,
                shape='plaintext',
                #style='rounded, filled', color=myndnode.color, fillcolor=light_colors[myndnode.color],
                fontname='din',
                fontsize='12')

def get_edge(parent, child, color):
    edge = Edge(parent, child, color=color, arrowhead='vee')
    return edge

def plot(graph, parent_node):
    global color_list
    global color_index
    global first_level_children

    if parent_node.parent is None:
        first_level_children = len(parent_node.children)

    parent = get_node(parent_node)

    for child in parent_node.children:
        if parent_node.parent is None:

            child.color = color_list[color_index]
            color_index += 1

        if child.color is None:
            child.color = parent_node.color

        node_x = get_node(child)
        edge_x = get_edge(parent, node_x, color=child.color)
        graph.add_node(node_x)
        graph.add_edge(edge_x)

        print '\t'*(parent_node.indent_lev+1), parent_node.id, parent_node.rtf_note, parent_node.color, '->', child.id, child.rtf_note, child.color
        plot(graph, child)


if __name__ == '__main__':
    ls = ListParser()

    notes = [line for line in open('plotter.md', 'r')]
    ls.parse(notes)

    root = ls.myndmap.root

    #graph = Dot(graph_type='digraph', layout='twopi', overlap='false', splines='true')
    #graph = Dot(graph_type='digraph', layout='neato', overlap='false', splines='true')
    graph = Dot(graph_type='digraph', rankdir='LR')
    plot(graph, root)
    graph.write_svg('todo.svg')
    graph.write_png('todo.png')

    dotGraph = DotGraphViz()
    dotGraph.plot(root)
    dotGraph.save_svg('todo2.svg')

    wgraph = WopiGraphViz()
    wgraph.plot(root)
    wgraph.save_png('todo2.png')

