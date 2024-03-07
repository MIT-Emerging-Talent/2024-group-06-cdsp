import streamlit as st
import pandas as pd
import altair as alt

data = pd.read_csv('attacks-on-health-care-systems-cleaned.csv') # read data from csv file

st.set_page_config(layout="wide") # set layout to wide
def country_report(country, col):

    country_df = data[data['Country'] == country]

    country_attack_count = sum(data['Country'] == country)
    deaths = int(country_df['Total Death'].sum())
    injuries = int(country_df['Total Injured'].sum())
    
    # Calculate the attack-to-death ratio as a float
    attack_to_death_ratio = country_attack_count / deaths
    integer_part = int(attack_to_death_ratio)
    fractional_part = round(attack_to_death_ratio - integer_part, 2)
    ratio_string = f"{integer_part}:{fractional_part}"

    report = f'''
    #####   **{country_attack_count}** hospital **{' attack has' if country_attack_count == 1 else 'attacks have'}** been reported. The number of casualities are **{deaths + injuries}** (injured = **{injuries}**, dead = **{deaths}**).
    - Violence with heavy weapons: **{int(country_df['Violence with heavy weapons'].sum())}**
    - Violence with individual weapons: **{int(country_df['Violence with individual weapons'].sum())}**
    - Abduction/Arrest/Detention of health personnel or patients: **{int(country_df['Abduction/Arrest/Detention of health personnel or patients'].sum())}**
    - Obstruction to health care delivery: **{int(country_df['Obstruction to health care delivery'].sum())}**
    - Psychological violence/threat of violence/intimidation: **{int(country_df['Psychological violence/threat of violence/intimidation'].sum())}**
    - Other: **{int(country_df['Other'].sum())}**

    #### Summary:
    | Attacks {country_attack_count}   | Total Deaths: {deaths}  | Total Injured: {injuries} | Attack to Death ratio: {ratio_string} |
    | -------------------------------- | ----------------------- | ------------------------- | --------------------------------------- | 
    '''

    col.title(country)

    col.markdown(report)


    col.write("---")
    col.write(' Every year in '+ country)
    # aggregated_data = data.groupby(by=["Country", ])["year"].sum()
    aggregated_data = country_df.groupby('year').size()
    col.bar_chart(aggregated_data, color='#FFFF00')

    # col.dataframe(country_df.groupby('Attack Type').size())

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
    attack_frequencies = country_df[attack_types_columns].sum()


    # Convert the Series to a DataFrame for easier plotting
    df = attack_frequencies.reset_index()
    df.columns = ['Attack Type', 'Frequency']
    df.sort_values(by=["Frequency"], inplace = True, ascending=False)
    col.subheader("Top 5 Attack Types")
    col.dataframe(df[:5].reset_index(drop=True))
    # pie chart 
    chart = alt.Chart(df[:5]).mark_arc().encode(
        theta=alt.Theta(field="Frequency", type="quantitative"),
        color=alt.Color(field="Attack Type", type="nominal"),
    )
    col.altair_chart(chart, theme="streamlit", use_container_width=True)

    col.subheader("Attacks per weekday")
    col.bar_chart(country_df.groupby('weekday').size(), color='#FFFF00')


country = st.sidebar.selectbox(" Select a country", data.Country.unique())
comparing_mode = st.sidebar.toggle('Compare two countries')

if comparing_mode == False:
    col1, col2 , = st.columns([2,0.1])
else:
    col1, col2 , = st.columns([1,1])
    other_country = st.sidebar.selectbox(" Select another country", data.Country.unique(), key="other_country", index=1)
    country_report(other_country, col2)


country_report(country, col1)
 