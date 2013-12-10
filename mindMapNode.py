#!/usr/bin/env python
# Class wrapper for a list item that represents also a node of the MindMap

class MindMapNode(object):

    def __init__(self, node_id, parent_id, raw_note, indent_lev):
        assert type(node_id)    == int
        assert type(parent_id)  == int
        assert type(raw_note)   == str  # unformatted text without indentation and initial mark (like -, *, +...)
        assert type(indent_lev) == int  # Number of indentations

        self.id = node_id
        self.parent_id = parent_id
        self.raw_note = raw_note
        self.lev_indent = indent_lev
        self.rich_text_note = ''
