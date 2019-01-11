#基于人的社交网络的page rank算法
import networkx as nx
from sys import platform as sys_pf
if sys_pf == 'darwin':
 import matplotlib
import matplotlib
matplotlib.use("TkAgg")
import random
from matplotlib.pyplot import show
from string import ascii_letters

def generate_name():
    return ''.join([random.choice(ascii_letters.upper()) for _ in range(3)])

social_graph = {
    "Yao": ['Guo', 'Wang', 'Tian', 'Tim'] + [generate_name() for _ in range(4)],
    "Guo": ['Li'] + [generate_name() for _ in range(5)],
    "Wang": ["Li_2"] + [generate_name() for _ in range(5)],
    "Li_2": [generate_name() for _ in range(5)],
    "Li": [generate_name() for _ in range(1)],
}

social_network = nx.Graph(social_graph)
nx.draw(social_network, with_labels=True)
show()

sorted_list = sorted(nx.pagerank(social_network).items(), key=lambda x: x[1], reverse=True)
print(sorted_list)

















