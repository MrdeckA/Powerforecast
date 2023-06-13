import streamlit as st
import pandas as pd
from io import StringIO
import plost
from streamlit_option_menu import option_menu

def draw_forecast_page():

    with open('style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    
    st.sidebar.header('Prédictions de la consommation énergétique')

    st.sidebar.subheader('Type de Visualisation')
    time_hist_color = st.sidebar.selectbox('Selectioner', ('Temporelle', 'Autre')) 

    st.sidebar.subheader("Fenêtre d'Analyse")
    donut_theta = st.sidebar.selectbox("Période", ('Globale', 'Mensuelle', 'Journalière','Personnalisée'))

    st.sidebar.subheader('Zone de la ville de Tetouan')
    plot_data = st.sidebar.multiselect('Selectionner une zone', ['Zone 1', 'Zone 2', 'Zone 3'], ['Zone 1', 'Zone 2', 'Zone 3'])
    plot_height = st.sidebar.slider('Specify plot height', 200, 500, 250)

    st.sidebar.markdown('''
    ---
        Created with ❤️ by [PowerForecast_Team](/).
    ''')


    # Row A
    # st.markdown('### Metrics')
    # col1, col2, col3 = st.columns(3)
    # col1.metric("Temperature", "70 °F", "1.2 °F")
    # col2.metric("Wind", "9 mph", "-8%")
    # col3.metric("Humidity", "86%", "4%")

    # Row B
    # seattle_weather = pd.read_csv('https://raw.githubusercontent.com/MrdeckA/Powerforecast/main/Tetuan%20City%20power%20consumption.csv')
    seattle_weather = pd.read_csv('https://raw.githubusercontent.com/tvst/plost/master/data/seattle-weather.csv', parse_dates=['date'])
    stocks = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/stocks_toy.csv')

    c1, c2 = st.columns((7,3))
    with c1:
        st.markdown('### Heatmap')
        plost.time_hist(
        data=seattle_weather,
        date='date',
        x_unit='week',
        y_unit='day',
        color=time_hist_color,
        aggregate='median',
        legend=None,
        height=345,
        use_container_width=True)
    with c2:
        st.markdown('### Donut chart')
        plost.donut_chart(
            data=stocks,
            theta=donut_theta,
            color='company',
            legend='bottom', 
            use_container_width=True)

    # Row C
    st.markdown('### Line chart')
    st.line_chart(seattle_weather, x = 'date', y = plot_data, height = plot_height)


