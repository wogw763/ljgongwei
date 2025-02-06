"""
requirements.txt
pip install -i https://mirrors.aliyun.com/pypi/simple/ streamlit
pip install -i https://mirrors.aliyun.com/pypi/simple/ watchdog


"""

import streamlit as st

st.title('CounterExample')
if 'key' not in st.session_state:
    st.session_state['key'] = 0
increment = st.button('Increment')
if increment:
    st.session_state['key'] += 1
st.write('Count =', st.session_state['key'])
st.title('sdfgf')

"""
git status 查看仓库
git init 创建仓库
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/wogw763/Streamlit_project.git
git push -u origin main
操作方法如下
1.git init 
2.初始化
git add .
git commit -m 'init'
3.查看是否有绑定仓库
git remote -v
4.绑定仓库
git remote add origin git@github.com:wogw763/Streamlit_GongWing.git
git remote add origin https://github.com/wogw763/Streamlit_GongWing.git
git remote set-url origin https://github.com/wogw763/Streamlit_GongWing.git
5.推送到远端仓库
git push -u origin main
"""
