#!/usr/bin/env python
"""
An example showing how to use the JavaScript Infoviz Toolkit (JIT)
JSON export

See the JIT documentation and examples at http://thejit.org

"""
__author__ = """Ollie Glass (ollieglaskovik@gmail.com)"""

import networkx as nx
from networkx.readwrite import json_graph

# add some nodes to a graph
G = nx.Graph()

G.add_node("one", type="normal")
G.add_node("two", type="special")
G.add_node("solo")

# add edges
G.add_edge("one", "two")
G.add_edge("two", 3, type="extra special")

# convert to JIT JSON
jit_json = json_graph.jit_data(G, indent=4)
print jit_json

# X = json_graph.jit_graph(jit_json)
# print "Nodes: %s" % X.nodes()
# print "Edges: %s" % X.edges()
