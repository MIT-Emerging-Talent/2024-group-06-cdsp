import streamlit as st
import pandas as pd
import altair as alt
# import numpy as np

st.set_page_config(layout="wide") # set layout to wide

data = pd.read_csv('attacks-on-health-care-systems-cleaned.csv') # read data from csv file




st.title("Attacks on Hospitals")



st.header("Number of attacks on healthcare facilities over the years")
st.subheader("Between 2017 and 2024")
aggregated_data = data.groupby('year').size()
st.bar_chart(aggregated_data, color='#FFFF00')


st.header("Countries with Most Number of Attacks on Healthcare Facilities")
st.subheader("By country")

aggregated_data = data.groupby('Country').size().reset_index().rename(columns={0: 'count'}).sort_values(by='count', ascending=False)

st.altair_chart(alt.Chart(aggregated_data).mark_bar(color='#FFFF00').encode(
    x=alt.X('Country', sort=None, title="Country"),
    y=alt.Y('count', title="attacks"), # Use the named column for the count of attacks
), use_container_width=True)




st.header("Total Death to Attacks ratio per Country ")
st.subheader("By country")

aggregated_death_data = data.groupby(by=["Country"])[["Total Death",'Total Injured']].sum().reset_index().rename(columns={0: 'count'})
# First bar chart for the count of attacks
chart1 = alt.Chart(aggregated_data).mark_bar(color='#FFFF00').encode(
    x=alt.X('Country', sort=None, title="Country"),
    y=alt.Y('count', title="attacks", )
)

# Second bar chart for the total deaths
chart2 = alt.Chart(aggregated_death_data).mark_bar(color='#FF0000').encode(
    x=alt.X('Country', sort=None, title="Country"),
    y=alt.Y('Total Death', title="Total Deaths")
)

# Overlay the two charts
combined_chart = chart1 + chart2

# Display the combined chart
st.altair_chart(combined_chart, use_container_width=True)





st.header("Total Injured to Attacks ratio per Country ")
st.subheader("By country")

# First bar chart for the count of attacks
chart1 = alt.Chart(aggregated_data).mark_bar(color='#FFFF00').encode(
    x=alt.X('Country', sort=None, title="Country"),
    y=alt.Y('count', title="attacks", )
)

# Second bar chart for the total deaths
chart2 = alt.Chart(aggregated_death_data).mark_bar(color='#FF5733').encode(
    x=alt.X('Country', sort=None, title="Country"),
    y=alt.Y('Total Injured', title="Total Injured"),
)

# Overlay the two charts
combined_chart = chart1 + chart2

# Display the combined chart
st.altair_chart(combined_chart, use_container_width=True)