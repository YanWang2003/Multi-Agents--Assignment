import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import boids_model as bd


def bd_chart():
    # 模型标题
    st.title('Boids Network')


    col1, col2 = st.columns(2)
    with col1:
        num1_chart = st.number_input('鸟群数量', min_value=1, value=50, step=1, key='input_1')
    with col2:
        num2_chart = st.number_input('更新次数', min_value=10, value=3000, step=1, key='input_2')

    if st.button('计算并表征结果'):
        if type(num1_chart) != int:
            st.error('输入数据存在矛盾 无法生成')
        elif num1_chart <= 0:
            st.error('输入数据存在矛盾 无法生成')
        else:
            np.random.seed(13)
            boids = bd.BoidsModel(num1_chart)
            dis = np.array([])
            cos = np.array([])
            iteration = np.arange(num2_chart)
            for i in range(num2_chart):
                boids.update()
                dis = np.append(dis, boids.ave_dis_calculation())
                cos = np.append(cos, boids.ave_cos_spe_calculation())

            col1, col2 = st.columns(2)
            with col1:
                # st.write('Boids Network Average Distance')
                fig, ax = plt.subplots()
                plt.plot(iteration, dis, marker=None, color='#FB6467FF', linestyle='-', linewidth=3.5)
                ax.set_title('Boids Network Average Distance')
                ax.set_xlabel('Iteration')
                ax.set_ylabel('Distance')
                st.pyplot(fig)
            with col2:
                # st.write('Boids Network Average Speed Cosine Similarity')
                fig1, ax1 = plt.subplots()
                ax1.plot(iteration, cos, marker=None, color='green', linestyle='-', linewidth=3.5)
                ax1.set_title('Boids Network Average Speed Cosine Similarity')
                ax1.set_xlabel('Iteration')
                ax1.set_ylabel('Cosine Similarity')
                st.pyplot(fig1)


if __name__ == '__main__':
    bd_chart()

