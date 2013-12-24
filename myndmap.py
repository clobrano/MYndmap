#!/usr/bin/env python
from tools import *
from myndmapnode import MYndMapNode

class MYndMap(object):

    def __init__(self):
        self.hooks = {}  # NodeID:NodeItem of all parent Nodes (Nodes that have children)
        self.nodes = {}  # Complete dict of all Nodes
        self.nodes_cnt = -1  # Node's number in the tree
        
        
    def get_node_id(indent_lev):
        assert type(indent_lev) = int
        
        id = '%d-%d' % (indent_lev, node_cnt)
        node_cnt += 1
        return id
        
        
    def set_root(self, root_note):
        assert type(root_note) == str
        assert root_note.startswith('#')
        
        root_indent = -1
        root_parent = None
        root_id = get_node_id(root_indent)
        
        self.root = MYndMapNode(root_id, root_parent, root_note, root_indent)
        
        self.hooks.update({root_indent: root})
        self.items.update({root_id: root})
        
        debug('Root %s' % repr(self.root))
        
        
        
     def update(self, node_note, node_indent):
        assert node_cnt >= 0  # At least one item (the root)
        
        # get node's parent
        if hooks.has_key(node_indent - 1):
            parent_id = hooks[node_indent - 1].id
        else:
            parent_id = self.root.id        
        
        node_id = get_node_id(node_indent)
        node_parent = self.items[node_parent]
        
        node = MYndMapNode(node_id, node_parent, node_note, node_indent)
        
        self.hooks.update({node_indent: node})
        self.items.update({node_id: node})
        
        
