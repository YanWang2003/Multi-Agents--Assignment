import numpy as np
from scipy.spatial.distance import squareform, pdist
# spe_a = det_matrix@self.loc_birds / det_matrix.sum(axis=1).reshape(-1, 1) - self.loc_birds

a = np.array([[1, 1], [2, 2], [0, 2], [2, 0]])
dis_matrix = squareform(pdist(a))
dis_matrix = dis_matrix < 2
new = dis_matrix.sum(axis=1)
print(new)
print(dis_matrix)
c = dis_matrix @ a

m = [[4], [2], [2], [2]]
m1 = [[4,2], [2,2], [2,2], [2,2]]
d = c / new.reshape(-1, 1)

print(c)
print(d)
print(c/m)
print(c/m1)

