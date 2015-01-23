#!/usr/bin/env python
"""MYndmap

Usage:
	myndmap.py FILE_INPUT FILE_OUTPUT [--dot | --wopi | --neato]

Arguments:
	FILE_INPUT 		Input text file name
	FILE_OUTPUT		Output image file name (with extention)

Options:
	-h --help	Show this screen.
	-d --dot	Dot graphic style
	-w --wopi	Wopi graphic style
	-n --neato	Neato graphic style

"""
version='0.1'

from docopt import docopt
from listparser import *
from plotter import *

if __name__ == '__main__':
	arguments = docopt(__doc__, version='MYndmap %s'.format(version))
	ls = ListParser()
	
	notes = [line for line in open(arguments['FILE_INPUT'], 'r')]
	ls.parse(notes)
	
	root = ls.myndmap.root
	
	graph = None

	if arguments['--dot'] is True:
		graph = DotGraphViz()
	
	if arguments['--wopi'] is True:
		graph = WopiGraphViz()
	
	if arguments['--neato'] is True:
		graph = NeatoGraphViz()
	
	if graph is None:
		graph = DotGraphViz()

	graph.plot(root)
	graph.save_svg(arguments['FILE_OUTPUT'])

