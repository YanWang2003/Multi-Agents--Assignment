import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy.spatial.distance import squareform, pdist, cdist


# initialize and update the frame in the Boids Model
class BoidsModel:

    # initialize the location and speed of birds
    def __init__(self, birds_num: int):
        # set bird number
        self.birds_num = birds_num
        # birds location
        self.loc_birds = np.random.rand(birds_num, 2) * 90
        # birds speed, the scalar speed is a constant
        angles = 2 * math.pi * np.random.rand(birds_num)
        self.spe_birds = np.array(list(zip(np.sin(angles), np.cos(angles))))
        self.spe_birds_sca = 1
        # detect boundary (exclude, parallel, congregate)
        self.det_bod = np.array([40, 40, 100])
        # detect weight (exclude, parallel, congregate)
        self.det_wei = np.array([1, 1, 1])

    # update the speed and location in each frame
    def update(self):
        # calculate the distance between each other
        dis_matrix = squareform(pdist(self.loc_birds))
        # calculate the rule speed
        self.spe_birds = self.speed_calculate(dis_matrix)
        self.loc_birds += self.spe_birds

    # calculate the speed through 3 rules
    def speed_calculate(self, dis_matrix):
        # 远离质心速度
        det_matrix_a = dis_matrix < self.det_bod[0]
        spe_a = self.loc_birds - det_matrix_a@self.loc_birds / det_matrix_a.sum(axis=1).reshape(-1, 1)
        # 范围内平均速度
        det_matrix_b = dis_matrix < self.det_bod[1]
        spe_b = det_matrix_b@self.spe_birds / det_matrix_b.sum(axis=1).reshape(-1, 1)
        # 向心速度
        det_matrix_c = dis_matrix < self.det_bod[2]
        spe_c = det_matrix_c@self.loc_birds / det_matrix_a.sum(axis=1).reshape(-1, 1) - self.loc_birds
        # rule speed
        spe_rule = spe_a*self.det_wei[0] + spe_b*self.det_wei[0] + spe_c*self.det_wei[0]
        # normalization (this is a trick)
        norms = np.linalg.norm(spe_rule, axis=1)
        spe_rule = spe_rule / norms[:, np.newaxis]
        return 2 * spe_rule

    # calculate the average distance between birds
    def ave_dis_calculation(self):
        dis_matrix = squareform(pdist(self.loc_birds))
        np.fill_diagonal(dis_matrix, 0)
        upper_triangle_indices = np.triu_indices(dis_matrix.shape[0], k=1)
        avg_distance = np.mean(dis_matrix[upper_triangle_indices])
        return avg_distance

    # calculate the average speed cosine similarity speed between birds
    def ave_cos_spe_calculation(self):
        whole = cdist(self.spe_birds, self.spe_birds, metric='euclidean')
        ave_cos_speed = np.sum(whole) / (whole.size-self.birds_num)
        return ave_cos_speed


if __name__ == "__main__":
    np.random.seed(13)
    boids = BoidsModel(50)
    for i in range(3000):
        boids.update()
        print(i, boids.ave_dis_calculation(), boids.ave_cos_spe_calculation())
