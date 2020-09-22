import networkx as nx
import pandas as pd
from config import *
from matplotlib import pyplot as plt

def graph():
    matrix = pd.read_csv(matrix_path, header=None).transpose()

    G = nx.from_pandas_adjacency(matrix, create_using=nx.DiGraph)

    pos = nx.spring_layout(G, k=0.5, seed=2)

    nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'),
                           node_color = 'b', node_size = 500)
    nx.draw_networkx_labels(G, pos)
    nx.draw_networkx_edges(G, pos, edgelist=G.edges(), edge_color='r', arrows=True)

    plt.show()

    return G
