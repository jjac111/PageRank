from graph import *
from walk import *
import numpy as np
import pandas as pd


G = graph()
eigen_vector = nx.pagerank(G)

# print(sorted(eigen_vector, key=eigen_vector.get, ))
# print(sorted(round(x,2) for x in eigen_vector.values()))


r, history, r_c, history_c = walk(G, 'repeat')

norm_r = [float(i)/sum(r[:-1]) for i in r[:-1]]
norm_r_c = [float(i)/sum(r_c[:-1]) for i in r_c[:-1]]
nx_pagerank = [i for i in eigen_vector.values()]

print(norm_r)
print(norm_r_c)
print(nx_pagerank)

mse = (np.square(np.array(norm_r) - np.array(nx_pagerank))).mean()
mse_c = (np.square(np.array(norm_r_c) - np.array(nx_pagerank))).mean()

print(f'Mean square error between NetworkX PageRank & random walk: {mse}\n')
print(f'Mean square error between NetworkX PageRank & random walk with count: {mse_c}\n')

print(pd.DataFrame(history))
print(pd.DataFrame(history_c))

