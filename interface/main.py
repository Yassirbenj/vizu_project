import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn
import streamlit as st

with st.form("input_form",clear_on_submit=False):
    st.write("<h3>Upload your data on csv format ✨</h3>", unsafe_allow_html=True)
    data=st.file_uploader('download your csv file',type='csv')
    if data is not None:
        df=pd.read_csv(data)
    if st.form_submit_button("Basic infos"):
        if data is not None:
            st.text(f'<h4> Your table contain {len(df.index)} rows. Below a view of the first 5 lines of your table </h4>',unsafe_allow_html=True)
            st.dataframe(df.head())
            st.text("<h4>Below the types of each column </h4>",unsafe_allow_html=True)
            st.dataframe(df.dtypes)
    if st.form_submit_button("Basic statistics"):
        if data is not None:
            st.text("<h4>Below basic statistics of each column </h4>",unsafe_allow_html=True)
            st.dataframe(pd.DataFrame(df.describe()))
