import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import SIER_model as sier


def sier_chart():
    # 模型标题
    st.title('SIER Model')

    col1, col2 = st.columns(2)
    with col1:
        num1_chart = st.number_input('susceptible', min_value=0.0, value=0.9, step=0.01, key='input_1')
        num3_chart = st.number_input('infectious', min_value=0.0, value=0.0, step=0.01, key='input_3')
        num5_chart = st.number_input('update days', min_value=10, value=100, step=1, key='input_5')
        num6_chart = st.number_input('lambda', min_value=0.0, value=0.5, step=0.01, key='input_6')
    with col2:
        num2_chart = st.number_input('exposed', min_value=0.0, value=0.1, step=0.01, key='input_2')
        num4_chart = st.number_input('recovered', min_value=0.0, value=0.0, step=0.01, key='input_4')
        num7_chart = st.number_input('delta', min_value=0.0, value=0.1, step=0.01, key='input_7')
        num8_chart = st.number_input('gamma', min_value=0.0, value=0.2, step=0.01, key='input_8')

    if st.button('计算传染情况并并表征结果'):
        initial_rate = np.array([num1_chart, num2_chart, num3_chart, num4_chart])
        transfer_speed = np.array([num6_chart, num7_chart, num8_chart])
        print(initial_rate)
        print(transfer_speed)
        model = sier.SIER_model(initial_rate, transfer_speed)
        # array = np.arange(1, 101)
        array = np.arange(1, num5_chart + 1)
        rate = np.array([initial_rate])
        for i in array:
            model.update()
            rate = np.append(rate, [model.person_rate], axis=0)

        susceptible = rate[:, 0]
        exposed = rate[:, 1]
        infectious = rate[:, 2]
        recovered = rate[:, 3]
        array = np.arange(1, num5_chart + 2)


        fig, ax = plt.subplots()
        plt.plot(array, susceptible, marker=None, linestyle='-', color='#357EBDFF', label='Susceptible Rate',
                 linewidth=2)
        plt.plot(array, exposed, marker=None, linestyle='-', color='#EEA236FF', label='Exposed Rate', linewidth=2)
        plt.plot(array, infectious, marker=None, linestyle='-', color='#D43F3AFF', label='Infectious Rate', linewidth=2)
        plt.plot(array, recovered, marker=None, linestyle='-', color='#5CB85CFF', label='Recovered Rate', linewidth=2)

        ax.set_title('SIER Model')
        ax.set_xlabel('Days')
        ax.set_ylabel('Rate')
        ax.legend()
        ax.grid(True)
        st.pyplot(fig)


if __name__ == '__main__':
    sier_chart()
