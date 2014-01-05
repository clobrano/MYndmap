#!/usr/bin/env python
from listparser import *
from plotter import *

if __name__ == '__main__':
    ls = ListParser()

    notes = [line for line in open('todo.md', 'r')]
    ls.parse(notes)

    root = ls.myndmap.root

    dotGraph = DotGraphViz()
    dotGraph.plot(root)
    dotGraph.save_svg('dot.svg')

    wgraph = WopiGraphViz()
    wgraph.plot(root)
    wgraph.save_svg('wopi.svg')

    ngraph = NeatoGraphViz()
    ngraph.plot(root)
    ngraph.save_svg('neato.svg')

