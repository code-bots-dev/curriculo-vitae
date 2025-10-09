import streamlit as st
import requests
import json
import pandas as pd
import plotly.express as px

url_covid = "https://disease.sh/v3/covid-19/countries"
# add_selectbox = st.sidebar.selectbox(
#     "Selecione os dados a serem exibidos",
#     ("COVID-19", "Criptomoedas")
# )

add_selectbox = st.sidebar.radio(
    ":green[**Selecione os dados a serem exibidos**]",
    ("DashBoard", "ChatBot - IA")
)

if add_selectbox == 'DashBoard':
    request_covid= requests.get(url_covid)
    data_json = request_covid.json()

    df = pd.DataFrame(data_json)
    df = df[['country', 'cases', 'deaths']]

    charbar1, charbar2 = st.columns(2)
    with charbar1:
        top10_cases = df.sort_values(by='cases', ascending=False).head(10)

        # Gráfico interativo de casos
        fig_cases = px.bar(
            top10_cases,
            x='country',
            y='cases',
            text='cases',
            labels={'cases': 'Casos', 'country': 'País'},
            title='Top 10 países por casos de COVID-19',
            color_discrete_sequence=['yellow']
        )
        fig_cases.update_traces(texttemplate='%{text:,}', textposition='outside')
        st.plotly_chart(fig_cases, use_container_width=True)

    with charbar2:
        top10_deaths = df.sort_values(by='deaths', ascending=False).head(10)

        fig_deaths = px.bar(
            top10_deaths,  # ✅ correção aqui
            x='country',
            y='deaths',
            text='deaths',
            labels={'deaths': 'Mortes', 'country': 'País'},
            title='Top 10 países por mortes de COVID-19',
            color_discrete_sequence=['red']
        )
        fig_deaths.update_traces(texttemplate='%{text:,}', textposition='outside')
        st.plotly_chart(fig_deaths, use_container_width=True)

    lista_paises = []
    for items in data_json:
        lista_paises.append(
            items['country']
        )

    select_data = st.multiselect("Selecione o Pais", lista_paises, max_selections=1)

    if select_data:
        request_covid_pais = requests.get(f"{url_covid}/{select_data[0]}")
        cases = request_covid_pais.json()['cases']
        deaths = request_covid_pais.json()['deaths']

        df = pd.DataFrame({
            'Tipo': ['Casos', 'Mortes'],
            'Quantidade': [cases, deaths]
        })
        df = df.set_index('Tipo')
        st.bar_chart(df)
