import numpy as np

# 创建一个 N*2 的示例数组
array = np.array([[1, 2],
                  [3, 4],
                  [5, 6]])

# 计算每一行的大小
norms = np.linalg.norm(array, axis=1)

# 将每一行的元素除以其对应的大小
normalized_array = array / norms[:, np.newaxis]

print(normalized_array)

from scipy.spatial.distance import cdist
import numpy as np

# 定义两个集合，每个集合包含两个二维向量
XA = np.array([[1, 2],
               [3, 4]])
XB = np.array([[5, 6],
               [7, 8]])

# 计算两个集合中向量之间的欧氏距离
distances = cdist(XA, XB, metric='euclidean')

print("Euclidean distances between XA and XB:")
print(distances)

