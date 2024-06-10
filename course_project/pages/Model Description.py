import streamlit as st

st.markdown('### Model Descripition')


st.markdown('## 1.多机器人追逃模型')
# 模型readme文件展示
with open('notes/agents_run_readme.md', 'r', encoding='utf-8') as md_file:
    md_content = md_file.read()
st.markdown(md_content, unsafe_allow_html=True)


st.markdown('## 2.Boids模型')
# 模型readme文件展示
with open('notes/boids_model_readme.md', 'r', encoding='utf-8') as md_file:
    md_content = md_file.read()
st.markdown(md_content, unsafe_allow_html=True)


st.markdown('## 3.SIER传染病模型')
# 模型readme文件展示
with open('notes/SIER_readme.md', 'r', encoding='utf-8') as md_file:
    md_content = md_file.read()
st.markdown(md_content, unsafe_allow_html=True)
# 模型示意图展示
st.image('notes/SIER_readme.PNG', caption='SIER Model', use_column_width=True)

st.markdown('## 4.NW小世界模型')
# 模型readme文件展示
with open('notes/NW.md', 'r', encoding='utf-8') as md_file:
    md_content = md_file.read()
st.markdown(md_content, unsafe_allow_html=True)

st.markdown('## 5.WS小世界模型')
# 模型readme文件展示
with open('notes/WS.md', 'r', encoding='utf-8') as md_file:
    md_content = md_file.read()
st.markdown(md_content, unsafe_allow_html=True)