import streamlit as st
import matplotlib.pyplot as plt
import WS_model as ws
import networkx as nx


def ws_chart():
    st.title('Watts Strogatz Network')

    num1_chart = st.number_input('结点总数', min_value=1, value=None, step=1, key='input_1')
    num2_chart = st.number_input('结点初始连接数', min_value=2, value=None, step=2, key='input_2')
    num3_chart = st.number_input('重新连接成功概率', min_value=0.0, max_value=1.0, value=None, step=0.01, key='input_3')

    if st.button('绘制示意图并计算相关系数'):
        validation = ws.ws_check(num1_chart, num2_chart, num3_chart)
        if not validation:
            st.error('输入数据存在矛盾 无法生成网络')
        else:
            example = ws.WS(num1_chart, num2_chart, num3_chart)
            # layout in a circle
            fig, ax = plt.subplots()
            ax = plt.gca()
            position = nx.shell_layout(example.G)
            nx.draw(example.G, position, ax=ax, with_labels=True, node_color='skyblue', edge_color='k')
            plt.title("Watts Strogatz Network")
            st.pyplot(fig)

            st.write('Average Distance', round(example.dis_cal(), 2))
            ave, glo = example.clu_cal()
            st.write('Average Clustering Efficient', round(ave, 2))
            st.write('Global Clustering Efficient', round(glo, 2))


if __name__ == '__main__':
    ws_chart()

