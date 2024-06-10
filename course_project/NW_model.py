# 实现并展示NW小世界模型构建，并计算平均路径长度和聚类系数。
import random
import networkx as nx
import matplotlib.pyplot as plt
import NNCS_model as nncs


# create the Newman Watts Network
class NW:

    def __init__(self, node_number: int, connect_per_node: int, repeat_time: int, probability):
        # initialize the graph as a Nearest Neighbor Coupled Network
        self.G = nncs.NNCN(node_number, connect_per_node).G
        # update the edge connection to change the network into NW Network
        for i in range(repeat_time):
            if random.random() < probability:
                # choose a valid node set
                while 1:
                    node_a = random.randint(1, node_number)
                    node_b = random.randint(1, node_number)
                    if node_a != node_b and not self.G.has_edge(node_a, node_b):
                        break
                self.G.add_edge(node_a, node_b)

    # calculate the average distance
    def dis_cal(self):
        return nx.average_shortest_path_length(self.G)

    # calculate the clustering efficient
    def clu_cal(self):
        return nx.average_clustering(self.G), nx.transitivity(self.G)


# Newman Watts Network validation check
def nw_check(node_number: int, connect_per_node: int, repeat_time: int, probability):
    try:
        if probability >= 1 or probability <= 0:
            return False
        if connect_per_node < 2 or connect_per_node > node_number-1 or connect_per_node%2 != 0:
            return False
        return True
    except:
        return False


# show the Newman Watts Network
if __name__ == '__main__':
    example = NW(10, 4, 4, 0.9)
    # layout in a circle
    position = nx.shell_layout(example.G)
    nx.draw(example.G, position, with_labels=True, node_color='skyblue', node_size=700, edge_color='k')
    plt.title("Newman Watts Network")
    plt.show()
    print("Newman Watts Network")
    print("average distance", example.dis_cal())
    print("average clustering efficient, global clustering efficient", example.clu_cal())
