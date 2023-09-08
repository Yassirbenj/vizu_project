import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn
import streamlit as st

with st.form("input_form",clear_on_submit=False):
    st.write("<h3>Upload your data on csv format ✨</h3>", unsafe_allow_html=True)
    data=st.file_uploader('download your csv file',type='csv')
    if data is not None:
        df=pd.read_csv(data)
        st.dataframe(df)
    if st.form_submit_button("Basic infos"):
        if data is not None:
            st.text(df.info())
    if st.form_submit_button("Basic statistics"):
        if data is not None:
            st.text(df.describe())
