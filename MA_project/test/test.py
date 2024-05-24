"""from sklearn.neighbors import NearestNeighbors
import numpy as np

# 创建一些示例数据
X = np.array([[1, 2], [1, 3], [2, 2], [2.5, 3], [3, 1], [4, 2]])

# 实例化一个NearestNeighbors对象
k = 3  # 你想找出的最近邻数量
nbrs = NearestNeighbors(n_neighbors=k, algorithm='ball_tree').fit(X)

# 指定一个点来找出其最近邻
point = np.array([[2, 1.5]])  # 你想要找出最近邻的点
distances, indices = nbrs.kneighbors(point)

# 输出最近邻的距离和索引
print("最近邻的距离：", distances)
print("最近邻的索引：", indices)
print(type(distances))"""
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# 生成示例数据
num_frames = 100
num_points = 10
data = np.random.rand(num_frames, num_points, 2)  # 生成100个时间点，每个时间点有10个点的二维坐标数据

# 创建画布和坐标轴
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 更新函数，用于更新每一帧的数据
def update(frame):
    ax.clear()
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_zlim(0, num_frames)  # 将 z 轴范围设置为时间点的范围
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Time')

    for i in range(num_points):
        x = data[frame, i, 0]
        y = data[frame, i, 1]
        z = frame
        ax.scatter(x, y, z)
    return ax

# 创建动画
ani = FuncAnimation(fig, update, frames=num_frames, blit=False)

# 保存动画为 GIF 文件
ani.save('animation.gif', writer='pillow')

# 在 PyCharm 中查看 GIF 文件"""



"""import matplotlib.pyplot as plt
import numpy as np
from moviepy.video.io.bindings import mplfig_to_npimage
import moviepy.editor as mpy

# 用matplotlib绘制一个图形

duration = 2

fig_mpl, ax = plt.subplots(1, figsize=(5, 3), facecolor='white')
xx = np.linspace(-2,2,200) # x向量
zz = lambda d: np.sinc(xx**2)+np.sin(xx+d) # （变化的）Z向量
ax.set_title("Elevation in y=0")
ax.set_ylim(-1.5,2.5)
line, = ax.plot(xx, zz(0), lw=3)

# 用MoviePy制作动（为每个t更新曲面）。制作一个GIF

def make_frame_mpl(t):
    line.set_ydata( zz(2*np.pi*t/duration))  # 更新曲面
    return mplfig_to_npimage(fig_mpl) # 图形的RGB图像

animation =mpy.VideoClip(make_frame_mpl, duration=duration)
animation.write_gif("sinc_mpl.gif", fps=20)"""



"""# draw the example plots
duration = 2
fig_mpl, ax = plt.subplots(1, figsize=(5, 3), facecolor='white')
ax.set_title("Example of Boids Model")
ax.set_xlim(-600, 600)
ax.set_ylim(-600, 600)

# 生成示例散点数据
num_points = 100
x_data = np.random.uniform(-600, 600, num_points)
y_data = np.random.uniform(-600, 600, num_points)
scatter = ax.scatter(x_data, y_data)

# 用MoviePy制作动画（为每个t更新散点图）。制作一个GIF

def make_frame_mpl(t):
    # 更新散点位置
    x_data_new = np.random.uniform(-600, 600, num_points)
    y_data_new = np.random.uniform(-600, 600, num_points)
    scatter.set_offsets(np.column_stack((x_data_new, y_data_new)))
    return mplfig_to_npimage(fig_mpl)  # 图形的RGB图像

animation = mpy.VideoClip(make_frame_mpl, duration=duration)
animation.write_gif("generated_gifs/scatter_mpl.gif", fps=20)"""





import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# 生成示例数据
num_frames = 100
num_points = 10
data = np.random.rand(num_frames, num_points, 2)  # 生成100个时间点，每个时间点有10个点的二维坐标数据

# 创建画布和坐标轴
fig, ax = plt.subplots()

# 更新函数，用于更新每一帧的数据
def update(frame):
    ax.clear()
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')

    for i in range(num_points):
        x = data[frame, i, 0]
        y = data[frame, i, 1]
        ax.scatter(x, y)
    return ax

# 创建动画
ani = FuncAnimation(fig, update, frames=num_frames, blit=False)

# 保存动画为 GIF 文件
ani.save('animation.gif', writer='pillow')
