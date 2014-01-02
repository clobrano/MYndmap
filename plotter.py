#!/usr/bin/env python
from abc import ABCMeta, abstractmethod
from pydot import Dot
from pydot import Edge
from pydot import Node
from myndmapnode import MYndMapNode

class GraphVizPlot:
    __metaclass__ = ABCMeta
    COLOR_LIST = ['red', 'blue', 'green', 'orange', '#E6E600', 'purple']
    LIGHT_COLORS = {None:None, 'red': '#FFB5C6', 'blue':'#B5B8FF', 'green':'#BEFFB5', 'orange':'#FFE9B5', '#E6E600':'#FFFFB5', 'purple':'#F0B5FF'}
    MAX_WORDS_PER_LINE = 5  ## In Node messages, max 5 words per line before a newline

    def __init__(self):
        self._graph = None
        self._color_index = 0

        self._dot_config = {'shape':'plaintext', 'style':None, 'color':True, 'fillcolor':True, 'fontname':'din', 'fontsize':'12'}
        self._edge_config = {'arrowhead':'vee'}

    def save_svg(self, filename):
        self._graph.write_svg(filename)

    def save_png(self, filename):
        self._graph.write_png(filename)

    @property
    def root(self):
        return self._graph

    @root.setter
    def root(self, root_dot):
        assert type(root_dot) == Dot
        self._graph = root_dot

    @abstractmethod
    def plot(self, parent_node):
        assert type(parent_node) == MYndMapNode

        parent_dot = self._get_dot(parent_node)  ## Nodes are logical tree's items, Dots are graphical tree's items

        for child_node in parent_node.children:
            if parent_node.is_root():
                child_node.color = GraphVizPlot.COLOR_LIST[self._color_index]
                self._color_index += 1

            if child_node.color is None:
                child_node.color = parent_node.color  ## The color property is 'inheredited' to keep the same color along the branches

            child_dot = self._get_dot(child_node)
            edge = self._get_edge(parent_dot, child_dot, child_node.color)
            self._update_graph(child_dot, edge)

            self.plot(child_node)


    def _get_dot(self, myndnode, style=False):
        assert type(myndnode) == MYndMapNode

        formatted_text = self._get_formatted_text(myndnode.rtf_note)

        dot = Node(formatted_text,
                   label=formatted_text,
                   shape=self._dot_config['shape'])

        if not self._dot_config['style'] is None:
            dot.add_style(self._dot_config['style'])

        if self._dot_config['color']:
            dot.set_color(myndnode.color)

        if self._dot_config['fillcolor']:
            dot.set_fillcolor(GraphVizPlot.LIGHT_COLORS[myndnode.color])

        if not self._dot_config['fontname'] is None:
            dot.set_fontname(self._dot_config['fontname'])

        if not self._dot_config['fontsize'] is None:
            dot.set_fontsize(self._dot_config['fontsize'])

        return dot

    def _get_formatted_text(self, raw_text):
        formatted_text = self._shrink_text(raw_text)
        return formatted_text

    def _shrink_text(self, text):
        words = text.split(' ')
        shrink_word_list = []

        for word, pos in zip(words, xrange(len(words))):
            if pos > 0 and pos % GraphVizPlot.MAX_WORDS_PER_LINE == 0:
                shrink_word_list.append('<BR/>')
            shrink_word_list.append(word)

        shrink_msg = ' '.join(shrink_word_list)

        return '<%s>' % shrink_msg

    def _get_edge(self, parent_dot, child_dot, color_dot):
        edge = Edge(parent_dot, child_dot, color=color_dot, arrowhead=self._edge_config['arrowhead'])
        return edge

    def _update_graph(self, child_dot, edge):
        assert child_dot is not None
        assert edge is not None
        self._graph.add_node(child_dot)
        self._graph.add_edge(edge)


class DotGraphViz(GraphVizPlot):

    def __init__(self):
        super(DotGraphViz, self).__init__()
        self.root = Dot(graph_type='digraph', layout='dot', rankdir='LR')

    def plot(self, root):
        super(DotGraphViz, self).plot(root)


class WopiGraphViz(GraphVizPlot):

    def __init__(self):
        super(WopiGraphViz, self).__init__()
        self.root = Dot(graph_type='digraph', layout='twopi', overlap='false', splines='true')

    def plot(self, root):
        super(WopiGraphViz, self).plot(root)

class NeatoGraphViz(GraphVizPlot):

    def __init__(self):
        super(NeatoGraphViz, self).__init__()
        self.root = Dot(graph_type='digraph', layout='neato', overlap='false', splines='true')

    def plot(self, root):
        super(NeatoGraphViz, self).plot(root)