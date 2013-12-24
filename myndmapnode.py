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
        self.rich_text_note = self.raw_note.strip()
        self.children = []
        
    def __repr__(self):
        if not self.parent is None:
            parent_id = self.parent.id
        else:
            parent_id = "None"
            
        return '{id:%s, parent_id:%s, ind:%d, note:%s}' % (self.id, parent_id, self.indent_lev, self.rich_text_note)

