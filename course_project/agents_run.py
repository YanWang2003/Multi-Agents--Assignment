import numpy as np
import networkx as nx
from networkx.convert_matrix import to_numpy_array
import random


def generate_connected_graph(n_nodes):
    """
    生成一个具有n_nodes个顶点的随机连通无向图
    图初始为一个完全图，然后随机移除边直到不形成环路但仍保持连通（得到一颗生成树）
    返回邻接矩阵
    """
    G = nx.complete_graph(n_nodes)  # 创建一个完全图
    # 移除边直到图连通但不是完全图
    while True:
        # 随机选择一条边尝试移除
        edge_to_remove = random.choice(list(G.edges))
        G.remove_edge(*edge_to_remove)  # 移除边
        # 检查图是否仍然连通
        if not nx.is_connected(G):
            # 如果不连通，则恢复这条边
            G.add_edge(*edge_to_remove)
            break  # 结束循环，此时图应该是连通的
    adj_matrix = to_numpy_array(G)
    return adj_matrix


class AgentsRun:
    def __init__(self, Tom_num: int, Jerry_num: int, graph_nodes: int):
        self.Tom_num = Tom_num
        self.Jerry_num = Jerry_num
        self.graph_nodes = graph_nodes
        self.step = 0

        # 路径图 graph_connection[i][j]= 0 表示i-->j无路径，=1表示i-->j有路径 此矩阵大小(graph_nodes, graph_nodes)
        self.graph_connection = generate_connected_graph(self.graph_nodes)
        np.fill_diagonal(self.graph_connection, 1)

        """# self.graph_connection = np.random.choice([0, 1], size=(graph_nodes, graph_nodes), p=[0.9, 0.1])
        self.graph_connection = np.zeros(shape=(graph_nodes, graph_nodes))
        upper_triangle_indices = np.triu_indices(graph_nodes, k=1)
        self.graph_connection[upper_triangle_indices] = np.random.choice([0, 1],
                                                                         size=upper_triangle_indices[0].shape,
                                                                         p=[0.8, 0.2])
        self.graph_connection += self.graph_connection.T - np.diag(self.graph_connection.diagonal())
        np.fill_diagonal(self.graph_connection, 1)"""


        # 抓捕者位置矩阵 tom_loc[i][j]=1 表示抓捕者i在节点j 此矩阵大小(Tom_num, graph_nodes)
        # tom_loc * graph_connection得到的矩阵new[i][j]=1表示表示抓捕者i走一步可以走到节点j 此矩阵大小(Tom_num, graph_nodes)
        self.tom_loc = np.zeros(shape=(Tom_num, graph_nodes))
        for i in range(0, Tom_num):
            self.tom_loc[i][np.random.randint(0, graph_nodes)] = 1

        # 逃跑者位置矩阵 jerry_loc[i][j]=1 表示抓捕者i在节点j 此矩阵大小(Jerry_num, graph_nodes)
        # 1行全0表示已经被猫吃掉而不存在
        # jerry_loc * graph_connection得到的矩阵new[i][j]=1表示表示逃跑者i走一步可以走到节点j 此矩阵大小(Jerry_num, graph_nodes)
        self.jerry_loc = np.zeros(shape=(Jerry_num, graph_nodes))
        for i in range(0, Jerry_num):
            self.jerry_loc[i][np.random.randint(0, graph_nodes)] = 1

    # 判断谁赢
    def check_winner(self):
        # 超时且jerry没被抓完则Jerry赢
        if self.step >= 100 and np.sum(self.jerry_loc) > 0:
            return 1
        # 未超时且jerry抓完则Tom赢
        if self.step < 100 and np.sum(self.jerry_loc) == 0:
            return 0
        # 输赢未定
        else:
            return 2

    # 每一个step当Tom和Jerry在同一位置 Jerry被抓捕
    # 每一个step可以走一步
    # Tom选择方法：依次遍历结点，若找到相连且有老鼠的结点，则走向此结点，如果没有遍历到符合要求的结点，随机选择一个相邻结点前往
    # Jerry选择方法：依次遍历结点，如果找到一个没有猫的相邻结点，则走向此结点
    def update(self):
        update_tom = self.tom_loc @ self.graph_connection
        print('update tom \n', update_tom)
        update_jerry = self.jerry_loc @ self.graph_connection
        self.step += 1

        previous_tom_loc = self.tom_loc

        # Tom Update
        for i in range(self.Tom_num):
            tom_find = False
            for j in range(self.graph_nodes):
                # 如果到j点可以走通并且j点有Jerry
                if update_tom[i][j] == 1 and np.sum(self.jerry_loc[:, j]) != 0:
                    self.tom_loc[i] = np.zeros(shape=self.graph_nodes)
                    self.tom_loc[i][j] = 1
                    tom_find = True
                    print('find great point')
                    break
            # 如果没有可以走通并且j点有Jerry的点，随机选择一点走
            if not tom_find:
                while 1:
                    j = np.random.randint(0, self.graph_nodes)
                    if update_tom[i][j] == 1:
                        self.tom_loc[i] = np.zeros(shape=self.graph_nodes)
                        self.tom_loc[i][j] = 1
                        break


        # Jerry Update
        for i in range(self.Jerry_num):
            if np.sum(self.jerry_loc[i]) != 0:
                jerry_find = False
                for j in range(self.graph_nodes):
                    # 如果可以走通并且没有Toms
                    if update_jerry[i][j] == 1 and np.sum(previous_tom_loc[:, j]) == 0:
                        self.jerry_loc[i] = np.zeros(shape=self.graph_nodes)
                        self.jerry_loc[i][j] = 1
                        jerry_find = True

        print(f"第{self.step}步抓捕前 Tom位置\n", self.tom_loc)
        print(f"第{self.step}步抓捕前 Jerry位置\n", self.jerry_loc)

        # Tom try to eat Jerry
        for i in range(self.graph_nodes):
            if np.sum(self.jerry_loc[:, i]) != 0 and np.sum(self.tom_loc[:, i]) != 0:
                print(f'eat begin in{self.step}th step')
                print(f'eat{np.sum(self.jerry_loc[:, i])} Jerrys')
                self.jerry_loc[:, i] = np.zeros(shape=self.Jerry_num)

        print(f"第{self.step}步抓捕后 Tom位置\n", self.tom_loc)
        print(f"第{self.step}步抓捕后 Jerry位置\n", self.jerry_loc)

        return 1


if __name__ == '__main__':
    # 固定随机数生成范围
    # np.random.seed(20)
    # random.seed(20)
    agents_run = AgentsRun(14, 1, 5)

    print("邻接矩阵：\n", agents_run.graph_connection)
    print(f"第{agents_run.step}步 Tom位置\n", agents_run.tom_loc)
    print(f"第{agents_run.step}步 Jerry位置\n", agents_run.jerry_loc)


    print("Jerry初始数：\n", np.sum(agents_run.jerry_loc))
    print("Tom初始数：\n", np.sum(agents_run.tom_loc))

    while True:
        agents_run.update()

        if agents_run.check_winner() != 2:
            break

    print("游戏结束时更新次数：", agents_run.step)
    print("游戏结束时Jerry数", np.sum(agents_run.jerry_loc))
    print("winner is: ", "Tom" if agents_run.check_winner() == 0 else "Jerry")

