import qianfan_helper as qf

import streamlit as st
import time


st.title('智能宠物取名系统')

animal_type = st.sidebar.selectbox('你的宠物是?',['猫','狗','猪','松鼠','鸭鸭'])

color = st.sidebar.text_input('宠物的颜色是?',max_chars=15)

clicked = st.sidebar.button('试试手气')

if clicked:
    st.markdown(qf.generate_pet_name(animal_type,color))
    time.sleep(2)
