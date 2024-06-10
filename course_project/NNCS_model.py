import networkx as nx
import matplotlib.pyplot as plt


# create the Nearest Neighbor Coupled Network
class NNCN:

    def __init__(self, node_number: int, connect_per_node: int):
        # initialize the graph as an empty graph
        half_connect_per_node = int(connect_per_node / 2)
        self.G = nx.Graph()
        # generate node connection table
        self.G.add_node(node_number)
        # generate edge table
        edge_table = []
        for i in range(1, node_number+1):
            for j in range(1, half_connect_per_node+1):
                k = (i+j) % node_number
                if k == 0:
                    edge_table.append((i, node_number))
                else:
                    edge_table.append((i, (i+j) % node_number))
        self.G.add_edges_from(edge_table)


# show the Nearest Neighbor Coupled Network
if __name__ == '__main__':
    example = NNCN(10, 3)
    # layout in a circle
    position = nx.shell_layout(example.G)
    nx.draw(example.G, position, with_labels=True, node_color='skyblue', node_size=700, edge_color='k')
    plt.title("Nearest Neighbor Coupled Network")
    plt.show()
