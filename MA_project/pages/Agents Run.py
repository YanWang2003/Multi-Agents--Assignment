import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import agents_run as ar


def ar_chart():
    # 模型标题
    st.title('Agents Run Model')

    num1_chart = st.number_input('Toms数量', min_value=1, value=14, step=1, key='input_1')
    num2_chart = st.number_input('Jerrys数量', min_value=1, value=20, step=1, key='input_2')
    num3_chart = st.number_input('路径图结点数', min_value=1, value=5, step=1, key='input_3')

    if st.button('初始化模型并更新显示追逃结果'):
        agents_run = ar.AgentsRun(num1_chart, num2_chart, num3_chart)
        while True:
            agents_run.update()
            if agents_run.check_winner() != 2:
                break

        st.write('游戏结束时更新次数', agents_run.step)
        st.write("游戏结束时Jerry数量", np.sum(agents_run.jerry_loc))
        st.write("Winners are: ", "Toms" if agents_run.check_winner() == 0 else "Jerrys")


if __name__ == '__main__':
    ar_chart()

