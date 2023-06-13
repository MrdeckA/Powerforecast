# import streamlit as st
# import pandas as pd
# from io import StringIO
# import plost
# from streamlit_option_menu import option_menu
# from src import test_analys


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import random
import datetime
from src.data_analysis import importation_of_dataset  , box_plot , add_month_or_hour, boxplot_months




















def data_analysis_func():
    import pandas as pd

    with open('style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    
    st.sidebar.header('Dashboard')

    st.sidebar.subheader('Type de Visualisation')
    viz_type = st.sidebar.radio('Selectioner', ('Temporelle', 'Autre'), index = 1) 

    st.sidebar.subheader("Fenêtre d'Analyse")
    window = st.sidebar.selectbox("Période", ('Globale', 'Mensuelle', 'Journalière','Personnalisée'))

    st.sidebar.subheader('Zone de la ville de Tetouan')
    zones = st.sidebar.multiselect('Selectionner une zone', ['Zone 1', 'Zone 2', 'Zone 3'], ['Zone 1', 'Zone 2', 'Zone 3'])
    plot_height = st.sidebar.slider('Specify plot height', 200, 500, 250)

    st.sidebar.markdown('''
    ---
        Created with ❤️ by [PowerForecast_Team](/).
    ''')

# \Powerforecast-main\Tetuan City power consumption.csv
# Tetuan City power consumption.csv
    # Charger les données à partir du fichier csv
    path_ = "Tetuan City power consumption.csv"
    path_ = importation_of_dataset(path_)

    add_month_or_hour(path_)

    if viz_type == "Temporelle":
        if window == "Globale":
            with st.container():
                if "Zone 1" in zones:
                    with st.container():
                        st.pyplot(box_plot(path_, 'Zone 1 Power Consumption'))
                
                if "Zone 2" in zones:
                    with st.container():
                        st.pyplot(box_plot(path_, 'Zone 2 Power Consumption'))

                if "Zone 3" in zones:
                    with st.container():
                        st.pyplot(box_plot(path_, 'Zone 3 Power Consumption'))
                        # st.pyplot(box_plot(path_, y='Zone 3 Power Consumption'))


        elif window == "Mensuelle":
            rand_month = int(random.randint(1.12))
            number = st.number_input('Indiquer un numéro de mois (de 1 à 12)',
                                     step=1, min_value=1, max_value=12,
                                     format="%d", value=rand_month)
            if (number < 1) or (number > 12):
                number = rand_month
            if (number < 1) or (number > 12):
                number = rand_month
            df_sub_data = path_[path_['months']==number]
            with st.container():
                st.pyplot(boxplot_months(df_sub_data, 'Zone 1 Power Consumption',
                                         title="Zone 1 power consumption (KW)"))
            with st.container():
                st.pyplot(boxplot_months(df_sub_data, 'Zone 2 Power Consumption',
                                         title="Zone 2 power consumption (KW)"))
            with st.container():
                st.pyplot(boxplot_months(df_sub_data, 'Zone 3 Power Consumption',
                                         title="Zone 3 power consumption (KW)"))


    # Row A
    # st.markdown('### Metrics')
    # col1, col2, col3 = st.columns(3)
    # col1.metric("Temperature", "70 °F", "1.2 °F")
    # col2.metric("Wind", "9 mph", "-8%")
    # col3.metric("Humidity", "86%", "4%")

    # Row B
    # data_set = pd.read_csv('https://raw.githubusercontent.com/MrdeckA/Powerforecast/main/Tetuan%20City%20power%20consumption.csv',parse_dates=['DateTime'])
    # data_set = pd.read_csv('https://raw.githubusercontent.com/tvst/plost/master/data/seattle-weather.csv', parse_dates=['date'])
    # stocks = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/stocks_toy.csv')

    # c1, c2 = st.columns((7,3))
    # with c1:
    #     st.markdown('### Heatmap')
    #     st.write(test_analys.profile())
    