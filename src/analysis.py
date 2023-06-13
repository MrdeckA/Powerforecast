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
from src.data_analysis import importation_of_dataset  , box_plot , add_month_or_hour, boxplot_months, boxplot_min




















def data_analysis_func():
    import pandas as pd

    with open('style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    
    st.sidebar.header('Dashboard')

    st.sidebar.subheader('Type de Visualisation')
    viz_type = st.sidebar.radio('Selectioner', ('Temporelle', 'Autre'), index = 0) 

    st.sidebar.subheader("Fenêtre d'Analyse")
    window = st.sidebar.selectbox("Période", ('Globale', 'Annuelle', 'Mensuelle', 'Journalière'))

    st.sidebar.subheader('Zone de la ville de Tetouan')
    zones = st.sidebar.multiselect('Selectionner une zone', ['Zone 1', 'Zone 2', 'Zone 3'], ['Zone 1', 'Zone 2', 'Zone 3'])
    plot_height = st.sidebar.slider('Specify plot height', 200, 500, 250)

    st.sidebar.markdown('''
    ---
        Created with ❤️ by [Hêviosso_Tech].
    ''')

# \Powerforecast-main\Tetuan City power consumption.csv
# Tetuan City power consumption.csv
    # Charger les données à partir du fichier csv
    path_ = "Tetuan City power consumption.csv"
    path_ = importation_of_dataset(path_)

    add_month_or_hour(path_)
    st.set_option('deprecation.showPyplotGlobalUse', False)


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


        elif window == "Annuelle":
            # rand_month = int(random.randint(1,12))
            # number = st.number_input('Indiquer un numéro de mois (de 1 à 12)',
            #                          step=1, min_value=1, max_value=12,
            #                          format="%d", value=rand_month)
            # if (number < 1) or (number > 12):
            #     number = rand_month
            # if (number < 1) or (number > 12):
            #     number = rand_month
            # df_sub_data = path_[path_['months']==number]
            if "Zone 1" in zones:
                with st.container():
                    st.pyplot(boxplot_months(path_, x_='months', y_='Zone 1 Power Consumption')) #title="Zone 1 power consumption (KW)"
            if "Zone 2" in zones:
                with st.container():
                    st.pyplot(boxplot_months(path_, x_='months', y_='Zone 2 Power Consumption'))
            if "Zone 3" in zones:
                with st.container():
                    st.write("**Zone 1 : consommation annuelle**")
                    st.pyplot(boxplot_months(path_, x_='months', y_='Zone 3 Power Consumption'))


        elif window == "Mensuelle":
            rand_month = random.randint(1,12)
            number = st.number_input('Indiquer un numéro de mois (de 1 à 12)',
                                     step=1, min_value=1, max_value=12,
                                     format="%d", value=1)
            if (number < 1) or (number > 12):
                number = rand_month
            df_sub_data = path_[path_['months']==number]
            if "Zone 1" in zones:
                with st.container():
                    st.write("**Zone 1 : consommation du mois**")
                    st.pyplot(boxplot_months(df_sub_data, x_='months', y_='Zone 1 Power Consumption')) #title="Zone 1 power consumption (KW)"
            
            if "Zone 2" in zones:
                with st.container():
                    st.write("**Zone 2 : consommation du mois**")
                    st.pyplot(boxplot_months(df_sub_data, x_='months', y_='Zone 2 Power Consumption'))
            if "Zone 3" in zones:
                with st.container():
                    st.write("**Zone 3 : consommation du mois**")
                    st.pyplot(boxplot_months(df_sub_data, x_='months', y_='Zone 3 Power Consumption'))


        elif window == 'Journalière':
            first_day = path_.index[0]
            last_day = path_.index[-1]
            
            date_range = \
            st.date_input("Choisisez une période de visualisation",
            value=(first_day, first_day+pd.DateOffset(days=30)), min_value=first_day, max_value=last_day)
                    
            if len(date_range) == 1:
                date_range = (date_range[0], date_range[0]+pd.DateOffset(days=30))
                    
            df_sub_data = path_[date_range[0]:date_range[1]]
            with st.container():
                if "Zone 1" in zones:
                    st.write("**Zone 1 : consommation en fonction des heures**")
                    st.pyplot(boxplot_min(df_sub_data, x_='hour',
                                                y_='Zone 1 Power Consumption',
                                                ))
                
                if "Zone 2" in zones:
                    st.write("**Zone 2 : consommation en fonction des heures**")
                    st.pyplot(boxplot_min(df_sub_data, x_='hour',
                                                y_='Zone 2 Power Consumption',
                                                ))
                
                if "Zone 3" in zones:
                    st.write("**Zone 3 : consommation en fonction des heures**")
                    st.pyplot(boxplot_min(df_sub_data, x_='hour',
                                                y_='Zone 3 Power Consumption',
                                                ))
                    
    # else:


    