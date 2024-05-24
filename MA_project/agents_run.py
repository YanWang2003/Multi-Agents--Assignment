import numpy as np


class AgentsRun:
    def __init__(self, Tom_num: int, Jerry_num: int, graph_nodes: int):
        self.Tom_num = Tom_num
        self.Jerry_num = Jerry_num
        self.graph_nodes = graph_nodes
        self.step = 0

        # 路径图 graph_connection[i][j]= 0 表示i-->j无路径，=1表示i-->j有路径 此矩阵大小(graph_nodes, graph_nodes)
        self.graph_connection = np.random.choice([0, 1], size=(graph_nodes, graph_nodes))

        # 抓捕者位置矩阵 tom_loc[i][j]=1 表示抓捕者i在节点j 此矩阵大小(Tom_num, graph_nodes)
        # tom_loc * graph_connection得到的矩阵new[i][j]=1表示表示抓捕者i走一步可以走到节点j 此矩阵大小(Tom_num, graph_nodes)
        self.tom_loc = np.zeros(shape=(Tom_num, graph_nodes))
        for i in range(0, Tom_num):
            self.tom_loc[i][np.random.randint(0, graph_nodes)] = 1

        # 逃跑者位置矩阵 jerry_loc[i][j]=1 表示抓捕者i在节点j 此矩阵大小(Jerry_num, graph_nodes)
        # 第1行全0表示已经被猫吃掉而不存在
        # jerry_loc * graph_connection得到的矩阵new[i][j]=1表示表示抓捕者i走一步可以走到节点j 此矩阵大小(Jerry_num, graph_nodes)
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
    # 每一个step可以走一步 Tom选择方法：若旁边有老鼠 则走向旁边，如果没有，则随机
    # Jerry选择方法：若旁边有猫 则远离，如果没有，则随机
    def update(self):
        return 1

if __name__ == '__main__':
    agents_run = AgentsRun(10, 10, 40)
    while True:
        agents_run.update()
        if agents_run.check_winner() != 2:
            break
    print("winner is: ", "Tom" if agents_run.graph_nodes == 0 else "Jerry")

