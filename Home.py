import streamlit as st
import pandas as pd
from pandas import read_csv
import numpy as np
import plotly as plt
import matplotlib.pyplot as plt
import geopandas as gp
import pydeck as pdk

# §§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§ #
# configurações da página
st.set_page_config(layout="wide",page_title="Focos de incêndio",page_icon=":fire:")



# §§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§ #
# titulo

col01,col02,col03 = st.columns(3)
with col01:
    pass
with col02:
    st.title (':red[§ P]rojeto :red[I]ntegrador :red[IV]')
    st.image('image/incendio pantanal mg.jpeg',width=600)
with col03:
    pass
# §§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§ #
# Descrição do projeto
expander = st.expander("***_Descrição do Projeto_***")
expander.write ("Projeto integrador IV - UNIVESP")
# §§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§ #

