import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy.spatial.distance import squareform, pdist
from numpy.linalg import norm

width, height = 640, 480


class Boids:
    '''initialize the boids simulation'''

    def __init__(self, N):
        # initialize the boids simulation
        # 位置
        self.pos = height * np.random.rand(2 * N).reshape(N, 2)
        angles = 2 * math.pi * np.random.rand(N)
        # 矢量速度
        self.vel = np.array(list(zip(np.sin(angles), np.cos(angles))))
        # 鸟类个数
        self.N = N
        # 控制速度恒定为2
        self.velFix = 2.0
        # 排斥和内聚（以及平行）的检测距离
        self.minDist = 15
        self.maxDist = 55
        # 平行，排斥，内聚速度的权重
        self.al = 1.0
        self.se = 1.0
        self.co = 1.0
        self.maxRuleVel = 0.5
        self.maxVel = 2.0
        # 噪声
        self.noise = 0.2
        # 平均速度和平均距离（初始设置为0）
        self.aveVel = 0
        self.aveDist = 0

    def move(self):
        # update the simulation by one time step
        # 距离矩阵，使用 squareform(pdist(self.pos))能直接输出类鸟间相对距离的矩阵，输出的矩阵对角线为0且对称
        self.distMatrix = squareform(pdist(self.pos))
        self.aveDist = self.distMatrix.sum() / (self.N) ** 2
        # apply rules
        self.vel += self.applyRules()
        self.fix(self.vel, self.velFix)
        # 加上噪声
        angles = 2 * math.pi * np.random.rand(self.N)
        self.vel += np.array(list(zip(np.sin(angles), np.cos(angles)))) * self.noise * self.velFix
        # 控制速度一定
        self.fix(self.vel, self.velFix)
        self.aveVel = norm(self.vel.sum(axis=0) / self.N)
        self.pos += self.vel
        # 周期边界条件
        self.applyBC()

    def limitVec(self, vec, maxVal):
        # limit the magnitide of the 2D vector
        mag = norm(vec)
        # 将速度换成maxVal
        if mag > maxVal:
            vec[0], vec[1] = vec[0] * maxVal / mag, vec[1] * maxVal / mag

    def limit(self, X, maxVal):
        # limit the magnitide of 2D vectors in array X to maxVal
        for vec in X:
            self.limitVec(vec, maxVal)

    def fixVec(self, vec, velFix):
        # limit the magnitide of the 2D vector
        mag = norm(vec)
        # 将速度换成velFix
        vec[0], vec[1] = vec[0] * velFix / mag, vec[1] * velFix / mag

    def fix(self, X, velFix):
        # limit the magnitide of 2D vectors in array X to maxVal
        for vec in X:
            self.fixVec(vec, velFix)

    def applyBC(self):
        # apply boundary conditions
        deltaR = -0.
        for coord in self.pos:
            if coord[0] > width + deltaR:
                coord[0] = -deltaR

            if coord[0] < -deltaR:
                coord[0] = width + deltaR

            if coord[1] > height + deltaR:
                coord[1] = -deltaR

            if coord[1] < -deltaR:
                coord[1] = height + deltaR

    def applyRules(self):
        # rule 1:separation
        D = self.distMatrix < self.minDist
        # 求解质心位置，并且产生远离质心的速度
        vel = self.pos * D.sum(axis=1).reshape(self.N, 1) - D.dot(self.pos)
        vel = vel * self.se
        self.limit(vel, self.maxRuleVel)
        D = self.distMatrix < self.maxDist
        # rule 2:alignment
        # 求范围内平均速度
        vel2 = D.dot(self.vel)
        self.limit(vel2, self.maxRuleVel)
        vel += vel2 * self.al
        # rule 3: cohesion
        # 朝着质心移动
        vel3 = D.dot(self.pos) - self.pos  # 质心-自己位置
        self.limit(vel3, self.maxRuleVel)
        vel += vel3 * self.co
        return vel


def main():
    print('starting boids...')
    # set the initial number of boids
    N = 50
    boids = Boids(N)
    # set up plot
    fig = plt.figure(1)
    ax = plt.axes(xlim=(0, width), ylim=(0, height))
    # 设定身体大小为8
    pts, = plt.plot([], [], markersize=8, c='k', marker='o', ls='None')
    # 设定头部大小为3
    beak, = plt.plot([], [], markersize=3, c='r', marker='o', ls='None')
    aveVels = []
    aveDists = []
    frameNums = []

    def update(frameNum, boids):
        # update function for animation
        # print(frameNum)
        if frameNum % 50 == 0:
            print('当前帧数{}'.format(frameNum))
            print('平均速度为{}'.format(boids.aveVel))
            aveVels.append(boids.aveVel)
            aveDists.append(boids.aveDist)
            frameNums.append(frameNum)
        boids.move()
        pts.set_data(boids.pos.reshape(2 * boids.N)[::2],
                     boids.pos.reshape(2 * boids.N)[1::2])
        vec = boids.pos + 4 * boids.vel / boids.maxVel
        beak.set_data(vec.reshape(2 * boids.N)[::2],
                      vec.reshape(2 * boids.N)[1::2])
        plt.plot(boids.pos[0][0], boids.pos[0][1], c='y', marker=',', markersize=2)
        plt.plot(boids.pos[10][0], boids.pos[10][1], c='b', marker=',', markersize=2)
        plt.plot(boids.pos[20][0], boids.pos[20][1], c='r', marker=',', markersize=2)
        return pts, beak

    # 产生动画，这个函数原理是，每隔interval ms就将fargs传入func，从而产生动画效果，适合制作动图
    anim = animation.FuncAnimation(fig=fig, func=update, fargs=[boids], frames=100, interval=20, cache_frame_data=False)
    anim.save('boids_model_example.gif', writer='pillow')
    plt.show()
    fig2 = plt.figure(2)
    plt.subplot(1, 2, 1)
    plt.plot(frameNums, aveVels, c='b')
    plt.subplot(1, 2, 2)
    plt.plot(frameNums, aveDists, c='b')
    nameB = 'boidsTest'
    plt.savefig(nameB + '.jpg')
    plt.show()
    paraDict = {'weight,height': (width, height), '数量N': boids.N, '速度velFix': boids.velFix,
                '噪声noise': boids.noise, '避免碰撞距离minDist': boids.minDist, '内聚距离maxDist': boids.maxDist}
    file = open(nameB + '.txt', 'w')
    for k, v in paraDict.items():
        file.write(str(k) + ' ' + str(v) + '\n')
    file.close()


if __name__ == '__main__':
    main()