#!/usr/bin/env python
from tools import *
from myndmapnode import MYndMapNode

class MYndMap(object):

    def __init__(self):
        self.hooks = {}  # NodeID:NodeItem of all parent Nodes (Nodes that have children)
        self.nodes = {}  # Complete dict of all Nodes
        self.node_cnt = 0  # Node's number in the tree


    def get_node_id(self, indent_lev):
        assert type(indent_lev) == int

        id = '%d' % (self.node_cnt)
        self.node_cnt += 1
        return id


    def set_root(self, root_note):
        assert type(root_note) == str
        assert root_note.startswith('#')

        root_indent = -1
        root_parent = None
        root_id = self.get_node_id(root_indent)

        self.root = MYndMapNode(root_id, root_parent, root_note, root_indent)

        self.hooks.update({root_indent: self.root})
        self.nodes.update({root_id: self.root})

        print('root: %s' % repr(self.root))


    def add_leaf(self, node_note, node_indent):
        assert self.node_cnt >= 0  # At least one item (the root)

        # get node's parent
        if self.hooks.has_key(node_indent - 1):
            parent_id = self.hooks[node_indent - 1].id
        else:
            parent_id = self.root.id

        node_id = self.get_node_id(node_indent)
        node_parent = self.nodes[parent_id]

        node = MYndMapNode(node_id, node_parent, node_note, node_indent)

        node_parent.children.append(node)

        print('add node: %s' % repr(node))

        self.hooks.update({node_indent: node})
        self.nodes.update({node_id: node})


    def __repr__(self):
        repr = 'hooks:{0}\nnodes:{1}\nnode count:{2}'.format(self.hooks, self.nodes, self.node_cnt)
        return repr
