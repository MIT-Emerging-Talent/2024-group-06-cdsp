import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(layout="wide") # set layout to wide

data = pd.read_csv('./streamlit/attacks-on-health-care-systems-cleaned.csv') # read data from csv file



overview = '''
# Attacks on Healthcare Facilities
## Overview

It's deeply troubling to see the uptick in violence against healthcare facilities in recent years, especially in areas torn apart by conflict. This alarming trend strikes at the very heart of medical neutrality, putting critical healthcare services at great risk. The consequences of such violence are immediate and devastating, with healthcare workers and patients often caught in the crossfire. But the impact goes beyond the immediate; it stretches into the future, affecting the availability and quality of medical care for those who need it most. Reports show a disturbing pattern of aggression, ranging from heavy artillery to targeted assaults on medical staff and the very infrastructure meant to heal and save lives. There's a pressing need to dive deep into this issue, to unravel the motivations behind these attacks and their far-reaching effects. Understanding this is crucial in crafting effective measures to safeguard healthcare services and enforce the principles of international humanitarian law.

'''
st.markdown(overview)

st.markdown('''
            ### Number of attacks on healthcare facilities over the years
            ''')
st.markdown('''
            #### Between 2017 and 2024
            ''')
aggregated_data = data.groupby('year').size()
st.bar_chart(aggregated_data, color='#FFFF00')


coreIssues = '''
## Core Issues
'''
st.markdown(coreIssues)

coreIssue1 = '''
1. **Disruption of Healthcare Services:** The nature of these attacks implies a profound disruption in healthcare delivery. Essential services are crippled, healthcare workers are placed in peril, and the infrastructure necessary for patient care is compromised or destroyed outright.
'''
st.markdown(coreIssue1)

st.markdown('''
            #### Types of Attacks on Healthcare Facilities
            ''')


attack_types_columns = [
    "Sexual assault",
    "Violence with individual weapons",
    "facility or transport",
    "Criminalization of health care",
    "Armed or violent search of health care personnel",
    "Unknown",
    "Chemical agent",
    "Obstruction to health care delivery",
    "Removal of health care assets",
    "Assault",
    "Setting fire",
    "Violence with heavy weapons",
    "Abduction/Arrest/Detention of health personnel or patients",
    "Other",
    "Militarization of a health care asset",
    "Psychological violence/threat of violence/intimidation"
]
attack_frequencies = data[attack_types_columns].sum()


# Convert the Series to a DataFrame for easier plotting
df = attack_frequencies.reset_index()
df.columns = ['Attack Type', 'Frequency']

# Altair plot
chart = alt.Chart(df).mark_bar().encode(
    x='Frequency:Q',
    y=alt.Y('Attack Type:N', sort='-x')  # Sort bars by frequency
).properties(
    height=400,  # Adjust chart size
    width=600
)

st.altair_chart(chart, use_container_width=True)


coreIssue2 = '''
2. **Geographical Distribution of Attacks:** Data pointing to the locations of these incidents can shed light on regions most affected by such violence. Identifying these hotspots is crucial for understanding the broader impact on global healthcare in conflict zones.
'''
st.markdown(coreIssue2)


st.markdown('''
            #### Countries with Most Number of Attacks on Healthcare Facilities
            ''')

aggregated_data = data.groupby('Country').size().reset_index().rename(columns={0: 'count'}).sort_values(by='count', ascending=False)

st.altair_chart(alt.Chart(aggregated_data).mark_bar(color='#FFFF00').encode(
    x=alt.X('Country', sort=None, title="Country"),
    y=alt.Y('count', title="attacks"), # Use the named column for the count of attacks
), use_container_width=True)


st.markdown('''
## Additional Insights
''')

st.markdown('''
            The dataset reveals a troubling pattern of attacks on healthcare facilities, showcasing instances from various conflict zones. These attacks disrupt medical services, leading to significant casualties and infrastructure damage.
            ''')

st.markdown('''
            #### Total Death to Attacks ratio per Country
            ''')

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





st.markdown(
    '''
    #### Total Injured to Attacks ratio per Country
    '''
)

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