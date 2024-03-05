import streamlit as st
import pandas as pd

data = pd.read_csv('attacks-on-health-care-systems-cleaned.csv') # read data from csv file

st.set_page_config(layout="wide") # set layout to wide

col1, col2 , = st.columns(2)

country = col1.selectbox(" Select a country", data.Country.unique())

col1.write(country)

# Filter the DataFrame to include only rows where the 'Country' column is 'Ukraine'
country_df = data[data['Country'] == country]

# Sum up the values of the column you're interested in. For example, summing 'Attacks' for Ukraine.
country_attack_count = sum(data['Country'] == country)
deaths = int(country_df['Total Death'].sum())
injuries = int(country_df['Total Injured'].sum())

# Display the sum in Streamlit
col1.header(f"Total Attacks: {country_attack_count}")
col1.header(f"Total Deaths: {deaths}")
col1.header(f"Total Injured: {injuries}")
# Calculate the attack-to-death ratio as a float
attack_to_death_ratio = country_attack_count / deaths
# Separate the integer and fractional parts
integer_part = int(attack_to_death_ratio)
fractional_part = round(attack_to_death_ratio - integer_part, 2)
# Format the ratio as a string in the form "a:b"
ratio_string = f"{integer_part}:{fractional_part}"
col1.header(f"Attack to Death ratio: '{ratio_string}'")

col1.write("---")
col1.write(' Every year in '+ country)
# aggregated_data = data.groupby(by=["Country", ])["year"].sum()
aggregated_data = country_df.groupby('year').size()
col1.bar_chart(aggregated_data, color='#FFFF00')

# =========================================================================================== #

other_country = col2.selectbox(" Select a country", data.Country.unique(), key="other_country", index=1)

col2.write(other_country)

# Filter the DataFrame to include only rows where the 'Country' column is 'Ukraine'
other_country_df = data[data['Country'] == other_country]

# Sum up the values of the column you're interested in. For example, summing 'Attacks' for Ukraine.
other_country_attack_count = sum(data['Country'] == other_country)
other_country_deaths = int(other_country_df['Total Death'].sum())
other_country_injuries = int(other_country_df['Total Injured'].sum())

# Display the sum in Streamlit
col2.header(f"Total Attacks: {other_country_attack_count}")
col2.header(f"Total Deaths: {other_country_deaths}")
col2.header(f"Total Injured: {other_country_injuries}")
# Calculate the attack-to-death ratio as a float
attack_to_death_ratio = other_country_attack_count / other_country_deaths
# Separate the integer and fractional parts
integer_part = int(attack_to_death_ratio)
fractional_part = round(attack_to_death_ratio - integer_part, 2)
# Format the ratio as a string in the form "a:b"
ratio_string = f"{integer_part}:{fractional_part}"
col2.header(f"Attack to Death ratio: '{ratio_string}'")


col2.write("---")

col2.write(' Every year in '+ other_country)
# aggregated_data = data.groupby(by=["Country", ])["year"].sum()
other_country_aggregated_data = other_country_df.groupby('year').size()
col2.bar_chart(other_country_aggregated_data, color='#FFFF00')

