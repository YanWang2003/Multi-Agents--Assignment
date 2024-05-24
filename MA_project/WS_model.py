# 实现并展示WS小世界模型构建，并计算平均路径长度和聚类系数。
import random
import networkx as nx
import matplotlib.pyplot as plt
import NNCS_model as nncs


# create the Watts Strogatz Network
class WS:

    def __init__(self, node_number: int, connect_per_node: int, probability):
        # initialize the graph as a Nearest Neighbor Coupled Network
        self.G = nncs.NNCN(node_number, connect_per_node).G
        # update the edge connection to change the network into WS Network
        half_connect_per_node = int(connect_per_node / 2)
        for i in range(1, node_number + 1):
            for j in range(1, half_connect_per_node + 1):
                # change this edge connection with a specific probability
                if random.random() < probability:
                    # calculate the label of another node
                    k = (i + j) % node_number
                    if k == 0:
                        k = node_number
                    # choose the new label of another node, from(i, k) to (i, new_node)
                    while 1:
                        new_node = random.randint(1, node_number)
                        if new_node != i and new_node != k:
                            break
                    self.G.remove_edge(i, k)
                    self.G.add_edge(i, new_node)

    # calculate the average distance
    def dis_cal(self):
        return nx.average_shortest_path_length(self.G)

    # calculate the clustering efficient
    def clu_cal(self):
        return nx.average_clustering(self.G), nx.transitivity(self.G)


# Watts Strogatz Network validation check
def ws_check(node_number: int, connect_per_node: int, probability):
    try:
        if probability >= 1 or probability <= 0:
            return False
        if connect_per_node < 2 or connect_per_node > node_number - 1 or connect_per_node % 2 != 0:
            return False
        return True
    except:
        return False


# show the Watts Strogatz Network
if __name__ == '__main__':
    example = WS(10, 6, 0.3)
    # layout in a circle
    position = nx.shell_layout(example.G)
    nx.draw(example.G, position, with_labels=True, node_color='skyblue', node_size=700, edge_color='k')
    plt.title("Watts Strogatz Network")
    plt.show()
    print("Watts Strogatz Network")
    print("average distance", example.dis_cal())
    print("average clustering efficient, global clustering efficient", example.clu_cal())
