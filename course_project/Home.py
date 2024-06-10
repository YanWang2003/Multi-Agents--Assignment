# input "streamlit run Home.py" in the shell to run this program
import streamlit as st


st.set_page_config(
    page_title="Home Page",
)


st.write("# 多智能体系统实验展示")

# 两类模型
# 1. 输入 生成
# 2. 输入 生成(初始化) 更新
st.markdown(
    """
    #### 学号：61821130 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 姓名：汪研
    ### 实验内容
    1. (2.1)实现并展示WS小世界模型构建，并计算平均路径长度和聚类系数
    2. (2.2)实现并展示NW小世界模型构建，并计算平均路径长度和聚类系数
    3. (5.3)实现SIER传染病模型，并设计演示示例
    4. (6.1)实现Boids模型，并设计演示示例
    5. (6.3)解决多机器人追逃问题，并给出实例演示
"""
)
