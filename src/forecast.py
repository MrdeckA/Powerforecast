import streamlit as st
import pandas as pd
from io import StringIO
import plost
from streamlit_option_menu import option_menu
from src.data_analysis import importation_of_dataset  , box_plot , add_month_or_hour, boxplot_months


    

def draw_forecast_page():
    path_ = "Tetuan City power consumption.csv"
    path_ = importation_of_dataset(path_)

    with open('style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    
    st.sidebar.header('Prédictions de la consommation énergétique')


    st.sidebar.subheader('Zone de la ville de Tetouan')
    plot_data = st.sidebar.multiselect('Selectionner une zone', ['Zone 1', 'Zone 2', 'Zone 3'], ['Zone 1', 'Zone 2', 'Zone 3'])
    st.sidebar.subheader('')

    plot_height = st.sidebar.slider('Specify plot height', 200, 500, 250)




    


    st.sidebar.markdown('''
    ---
        Created with ❤️ by [PowerForecast_Team]
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
    option = st.radio("Période de visualistion   :", ("Mois", "Jour", "Heure"))

    first_day = path_.index[0]
    last_day = path_.index[-1]
    

    date_range = \
    st.date_input("Choisisez une période de visualisation",
    value=(first_day, first_day+pd.DateOffset(days=30)), min_value=first_day, max_value=last_day)
            
    if len(date_range) == 1:
        date_range = (date_range[0], date_range[0]+pd.DateOffset(days=30))
            
    df_sub_data = path_[date_range[0]:date_range[1]]

    c1, c2 = st.columns((7,3))
    with c1:
        st.markdown('### Heatmap')
        # plost.time_hist(
        # data=seattle_weather,
        # date='date',
        # x_unit='week',
        # y_unit='day',
        # color=time_hist_color,
        # aggregate='median',
        # legend=None,
        # height=345,
        # use_container_width=True)
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


