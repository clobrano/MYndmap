#!/usr/bin/env python
# Class parser for Markdown formatted lists
from re import compile
from minMapNode import MindMapNode

class ListParser(object):

    def __init__(self):
        indent = 4  # Number of spaces representing and indentation
        indent_pattern = '\s{%d, %d}' % indent
        self.compiler = compile(indent_pattern)
        self.markers = ['-','+','*']


    def isMainTopic(self, line):
        if line.startswith('#'):
            return True
        return False

    def getIndentLev(self, raw_note):
        assert type(raw_note) == str

        indent_lev = 0
        first_marker_pos = len(raw_note)
        note_marker = None

        for marker in self.markers:
            pos = raw_note.find(marker)
            if pos < first_marker_pos:
                first_marker_pos = pos
                note_marker = marker

        if len(raw_note) != first_marker_pos and None != note_marker:
            indentation = raw_note.split(marker)[0]
            indent_lev = len(self.compiler.findall(indentation))

        return indent_lev

    def parse(self, note):
        assert type(note) == list
        assert note[0].startswith('#')

        curr_node_id = 0
        root = MindMapNode(node_id=curr_node_id, parent_id=None, note=line, indent_lev=0)
        parent = root
        prev_node = None

        for line in note[1:]:
            curr_node_id += 1
            indent_lev = getIndentLev(line)

            if prev_node:
                if prev_node.indent_lev < indent_lev:
                    parent = prev_node

            node = MindMapNode(node_id = curr_node_id,
                               parent_id = parent.id,
                               note = line,
                               indent_lev = indent_lev)








