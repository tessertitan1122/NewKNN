# from sklearn.neighbors import KneighborsClassifier
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title('การจำแนกข้อมูลด้วยเทคนิค Machine Learnning')
# st.image("./img/go1.jpg")
col1, col2, col3 = st.columns(3)

with col1:
   st.header("Versicolor")
   st.image("./img/iris1.jpg")

with col2:
   st.header("Verginiga")
   st.image("./img/iris2.jpg")

with col3:
   st.header("Setosa")
   st.image("./img/iris3.jpg")

html_7 = """
<div style="background-color:#c5f18a;padding:15px;border-radius:15px 15px 15px 15px;border-style:'solid';border-color:black">
<center><h5>ข้อมูล iris หรือข้อมูลดอกไม้สำหรับทำนาย</h5></center>
</div>
"""
st.markdown(html_7, unsafe_allow_html=True)
st.markdown("")
st.markdown("")