import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn
import streamlit as st

with st.form("input_form",clear_on_submit=True):
    st.write("<h3>Upload your data on csv format ✨</h3>", unsafe_allow_html=True)
    data=st.file_uploader('download your csv file',type='csv')
    if st.form_submit_button("Basic infos"):
        if data is not None:
            df=pd.read_csv(data)
            st.text(df.infos())
    if st.form_submit_button("Basic statistics"):
        if data is not None:
            df=pd.read_csv(data)
            st.text(df.infos())
