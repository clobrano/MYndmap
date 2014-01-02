#!/usr/bin/env python
import pdb
from listparser import *
from plotter import *

if __name__ == '__main__':
    pdb.set_trace()
    ls = ListParser()

    notes = [line for line in open('plotter.md', 'r')]
    ls.parse(notes)

    root = ls.myndmap.root

    dotGraph = DotGraphViz()
    dotGraph.plot(root)
    dotGraph.save_svg('todo2.svg')

    wgraph = WopiGraphViz()
    wgraph.plot(root)
    wgraph.save_png('todo2.png')

    ngraph = NeatoGraphViz()
    ngraph.plot(root)
    ngraph.save_png('todo3.png')

