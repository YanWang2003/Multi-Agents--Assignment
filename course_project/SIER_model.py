# 实现一种传染病模型，并给出实例演示。
# 实现SIER模型
import matplotlib.pyplot as plt
import numpy as np


# SIER model (susceptible, exposed, infectious, recovered)
class SIER_model:
    def __init__(self, initial_rate, transfer_speed):
        # initial_rate = [susceptible, exposed, infectious, recovered]
        # transfer_speed = [lambda, delta, gamma]
        self.person_rate = initial_rate
        self.transfer_speed = transfer_speed
    def update(self):
        trans_se = self.transfer_speed[0] * self.person_rate[0] * self.person_rate[1]
        trans_ei = self.transfer_speed[1] * self.person_rate[1]
        trans_ir = self.transfer_speed[2] * self.person_rate[2]
        self.person_rate = self.person_rate + np.array([-trans_se, trans_se - trans_ei, trans_ei - trans_ir, trans_ir])

if __name__ == '__main__':
    # initial_rate = [susceptible, exposed, infectious, recovered]
    # transfer_speed = [lambda, delta, gamma]

    initial_rate = np.array([0.9, 0.1, 0, 0])
    transfer_speed = np.array([0.5, 0.1, 0.2])
    sier = SIER_model(initial_rate, transfer_speed)
    array = np.arange(1, 101)
    rate = np.array([initial_rate])
    for i in array:
        sier.update()
        rate = np.append(rate, [sier.person_rate], axis=0)

    print(np.shape(rate))
    susceptible = rate[:100, 0]
    exposed = rate[:100, 1]
    infectious = rate[:100, 2]
    recovered = rate[:100, 3]
    print(susceptible)
    print(np.shape(susceptible))

    # 创建一个新的图形
    plt.figure()

    # 绘制折线图
    plt.plot(array, susceptible, marker=None, linestyle='-', color='#357EBDFF', label='Susceptible Rate', linewidth=2)
    plt.plot(array, exposed, marker=None, linestyle='-', color='#EEA236FF', label='Exposed Rate', linewidth=2)
    plt.plot(array, infectious, marker=None, linestyle='-', color='#D43F3AFF', label='Infectious Rate', linewidth=2)
    plt.plot(array, recovered, marker=None, linestyle='-', color='#5CB85CFF', label='Recovered Rate', linewidth=2)

    # 添加标题和标签
    plt.title('SIER Model')
    plt.xlabel('Days')
    plt.ylabel('Rate')

    # 显示图例
    plt.legend()

    # 显示网格
    plt.grid(True)

    # 显示图形
    plt.show()


