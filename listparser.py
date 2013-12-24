#!/usr/bin/env python
# Class parser for Markdown formatted lists
from re import compile
from tools import *
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
        
        myndmap = MYndMap()
        
        hooks = {}  # NodeID:NodeItem of all parent Nodes (Nodes that have children)
        items = {}  # Complete dict of all Nodes
        
        ind_root = -1
        root_id = self.get_node_id(ind_root)
        root = MindMapNode(root_id, None, notes[0], ind_root)
                
        items.update({root_id: root})
        hooks.update({ind_root: root})
        
        myndmap.set_root(notes[0])
                
        
        info('Root %s' % repr(root))                              

        for line in notes[1:]:
            # get indentation level
            ind = self.get_indent(line)
            node_id = self.get_node_id(ind)
            node = MindMapNode(node_id, None, line, ind)           

            info('Created node %s' % repr(node))            
            
            # update items
            items.update({node_id:node})
                        
            # update hooks
            hooks[ind] = node
            
            # update parent/child relationship
            if hooks.has_key(ind - 1):
                parent_id = hooks[ind - 1].id
            else:
                parent_id = root.id
            
            info('Adding child %s to parent: %s' % (node.id, parent_id))
            
            items[parent_id].children.append(node)
            node.parent = items[parent_id]
            
            info('Updated node %s' % repr(node))            

