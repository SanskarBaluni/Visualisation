import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')

header=st.beta_container()
dataset=st.beta_container()
features=st.beta_container()


import plotly
import plotly.express as px
import plotly.graph_objects as go
plt.rcParams['figure.figsize']=17,8

import cufflinks as cf
import plotly.offline as pyo
from plotly.offline import init_notebook_mode,plot,iplot

import folium

with header:
    st.title('Health Dataset Visualization')
with dataset:
df=pd.read_excel(r"D:\Edge Download\Covid cases in India.xlsx")
st.dataset(df)
