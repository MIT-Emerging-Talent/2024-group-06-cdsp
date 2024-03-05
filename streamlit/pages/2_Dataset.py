import streamlit as st
import pandas as pd

data = pd.read_csv('attacks-on-health-care-systems-cleaned.csv') # read data from csv file
st.set_page_config(layout="wide") # set layout to wide

st.dataframe(data)