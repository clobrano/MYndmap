#!/usr/bin/env python
# Class wrapper for a list item that represents also a node of the MindMap

class MYndMapNode(object):

    def __init__(self, node_id, parent, raw_note, indent_lev):
        assert type(node_id)    == str
        assert type(raw_note)   == str  # unformatted text without indentation and initial mark (like -, *, +...)
        assert type(indent_lev) == int  # Number of indentations

        self.id = node_id
        self.parent = parent
        self.raw_note = r'%s' % raw_note
        self.indent_lev = indent_lev
        self.rtf_note = self.raw_note.strip()[2:]
        self.children = []
        self._color = None

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        assert type(color) == str
        self._color = color

    def __repr__(self):
        if not self.parent is None:
            parent_id = self.parent.id
        else:
            parent_id = "None"

        return '{id:%s, parent_id:%s, children:%d, ind:%d, note:%s, color:%s}' % (self.id, parent_id, len(self.children), self.indent_lev, self.rtf_note, self.color)

