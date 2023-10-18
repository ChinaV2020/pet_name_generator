import qianfan_helper as qf

import streamlit as st
import time
import os

st.title('智能宠物取名系统')

# 设置千帆的api key

ak = st.sidebar.text_input('千帆ak')
sk = st.sidebar.text_input('千帆sk')


animal_type = st.sidebar.selectbox('你的宠物是?',['猫','狗','猪','松鼠','鸭鸭'])

color = st.sidebar.text_input('宠物的颜色是?',max_chars=15)

if ak and sk:
    # 手动导入环境变量
    os.environ['QIANFAN_AK'] = str(ak)
    os.environ['QIANFAN_SK'] = str(sk)


clicked = st.sidebar.button('试试手气')

if clicked and ak and sk:
    st.markdown(qf.generate_pet_name(animal_type,color))
    time.sleep(2)
else:
    st.toast('请输入千帆的key再操作!')


