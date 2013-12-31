#!/usr/bin/env python
# Class parser for Markdown formatted lists
from re import compile
from tools import *
from myndmap import MYndMap
from myndmapnode import MYndMapNode

class ListParser(object):

    def __init__(self):
        self.base_indent = 4  # Number of spaces representing and indentation
        indent_pattern = '\s'
        self.compiler = compile(indent_pattern)
        self.markers = ['-','+','*']
        self.node_cnt = 0

    def isMainTopic(self, line):
        if line.startswith('#'):
            return True
        return False

    def get_indent(self, raw_note):
        assert type(raw_note) == str

        indent_lev = 0
        first_marker_pos = len(raw_note)
        note_marker = None

        for marker in self.markers:
            pos = raw_note.find(marker)

            if -1 < pos < first_marker_pos:
                first_marker_pos = pos
                note_marker = marker

        if len(raw_note) != first_marker_pos and None != note_marker:
            split = raw_note.split(note_marker)
            indent_lev = len(self.compiler.findall(split[0])) / self.base_indent

        return indent_lev

    def purge_empty_lines(self, notes):
        pass

    def get_node_id(self, indent_lev):
        id = '%d-%d' % (indent_lev, self.node_cnt)
        self.node_cnt += 1
        return id

    def parse(self, notes):
        assert type(notes) == list

        if not notes[0].startswith('#'):
            error('First line of the notes must start with # (The name of the list)')
            return

        self.myndmap = MYndMap()
        self.myndmap.set_root(notes[0])

        for line in notes[1:]:
            if line == '':
                continue
            # get indentation level
            ind = self.get_indent(line)

            self.myndmap.add_leaf(line, ind)
