import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn
import streamlit as st


data=st.file_uploader('download your csv file',type='csv')
df=pd.read_csv(data)
st.text(df.head())
