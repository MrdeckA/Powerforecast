import streamlit as st
import pandas as pd
from io import StringIO
import plost
import pickle
from streamlit_option_menu import option_menu
from src.data_analysis import importation_of_dataset  , box_plot , add_month_or_hour, boxplot_months
import numpy as np


def read_pred_results(file_pkl):
    with open(file_pkl, 'rb') as fp:
        df_predictions = pickle.load(fp)
    return df_predictions
    

def draw_forecast_page():
    path_ = "Tetuan City power consumption.csv"
    path_ = importation_of_dataset(path_)




    # Différents fichiers de résultats
    # Zone 1
    file_z1_xgboost = "predictions/Zone1/xgboost_predictions_Consumption_Z1.pkl"
    file_z1_lstm1h = "predictions/Zone1/lstm1H_predictions_Consumption_Z1.pkl"
    file_z1_lstm = "predictions/Zone1/lstm_predictions_Consumption_Z1.pkl"
    # Zone 2
    file_z2_xgboost = "predictions/Zone2/xgboost_predictions_Consumption_Z2.pkl"
    file_z2_lstm1h = "predictions/Zone2/lstm1H_predictions_Consumption_Z2.pkl"
    file_z2_lstm = "predictions/Zone2/lstm_predictions_Consumption_Z2.pkl"
    # Sone 3
    file_z3_xgboost = "predictions/Zone3/xgboost_predictions_Consumption_Z3.pkl"
    file_z3_lstm1h = "predictions/Zone3/lstm1H_predictions_Consumption_Z3.pkl"
    file_z3_lstm = "predictions/Zone3/lstm_predictions_Consumption_Z3.pkl"
    
    # chargement des différentes données
    df_z1_xgboost = read_pred_results(file_z1_xgboost)
    df_z1_lstm1h = read_pred_results(file_z1_lstm1h)
    df_z1_lstm = read_pred_results(file_z1_lstm)
    
    df_z2_xgboost = read_pred_results(file_z2_xgboost)
    df_z2_lstm1h = read_pred_results(file_z2_lstm1h)
    df_z2_lstm = read_pred_results(file_z2_lstm)
    
    df_z3_xgboost = read_pred_results(file_z3_xgboost)
    df_z3_lstm1h = read_pred_results(file_z3_lstm1h)
    df_z3_lstm = read_pred_results(file_z3_lstm)
    
    l_pred_col=["XGBoost", "LSTM_1H", "LSTM_1H_1variable"]
    ax_titles=["Prédictions XGBoost", "Prédictions LSTM_1H",
                        "Prédictions LSTM_1H_1variable"]

    # with open('style.css') as f:
    #     st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    
    # st.sidebar.header('Prédictions de la Consommation')


    # st.sidebar.subheader('Zone de la ville de Tetouan')
    # plot_data = st.sidebar.multiselect('Selectionner une zone', ['Zone 1', 'Zone 2', 'Zone 3'], ['Zone 1', 'Zone 2', 'Zone 3'])
    # st.sidebar.subheader('')

    # plot_height = st.sidebar.slider('Specify plot height', 200, 500, 250)




    


    # st.sidebar.markdown('''
    # ---
    #     Created with ❤️ by [PowerForecast_Team]
    # ''')


    # Row A
    # st.markdown('### Metrics')
    # col1, col2, col3 = st.columns(3)
    # col1.metric("Temperature", "70 °F", "1.2 °F")
    # col2.metric("Wind", "9 mph", "-8%")
    # col3.metric("Humidity", "86%", "4%")

    with st.container():
       st.write("")
       st.write(f""" ### Prédictions des différents modèles pas zone  """)
       st.info("""
          :point_down: **Résultats obtenus par zone**
      """)
      
    with st.container():
        zone_col, window_col= st.columns(2)
        
        with zone_col:
            zones = st.radio('**Zones de la ville de Tétouan**',
                             ('Zone 1', 'Zone 2', 'Zone 3'))
        

        with window_col:
            window = st.radio("**Fenêtre d'analyse**",
                              ('Globale', 'Personnalisée'))  




    if zones=="Zone 1":
        # Plage de dates des données
        first_day = np.array([df_z1_xgboost.index[0], df_z1_lstm.index[0],
                              df_z1_lstm1h.index[0]]).max()
        last_day = np.array([df_z1_xgboost.index[-1], df_z1_lstm.index[-1],
                             df_z1_lstm1h.index[-1]]).min()
        
        # Merge the dataframe
        df_z1_xgboost.rename(columns={"prediction":"XGBoost"}, inplace=True)
        df_z1_lstm1h.rename(columns={"prediction":"LSTM_1H"}, inplace=True)
        df_z1_lstm.rename(columns={"prediction":"LSTM_1H_1variable"}, inplace=True)
        df_data = pd.concat([df_z1_xgboost, df_z1_lstm1h[["LSTM_1H"]],
                             df_z1_lstm[["LSTM_1H_1variable"]]], axis=1)
        target="Consumption_Z1"
    if zones=="Zone 2":
        # Plage de dates des données
        first_day = np.array([df_z2_xgboost.index[0], df_z2_lstm.index[0],
                              df_z2_lstm1h.index[0]]).max()
        last_day = np.array([df_z2_xgboost.index[-1], df_z2_lstm.index[-1],
                             df_z2_lstm1h.index[-1]]).min()
        
        # Merge the dataframe
        df_z2_xgboost.rename(columns={"prediction":"XGBoost"}, inplace=True)
        df_z2_lstm1h.rename(columns={"prediction":"LSTM_1H"}, inplace=True)
        df_z2_lstm.rename(columns={"prediction":"LSTM_1H_1variable"}, inplace=True)
        df_data = pd.concat([df_z2_xgboost, df_z2_lstm1h[["LSTM_1H"]],
                             df_z2_lstm[["LSTM_1H_1variable"]]], axis=1)
        target="Consumption_Z2"
        
    if zones=="Zone 3":
        # Plage de dates des données
        first_day = np.array([df_z3_xgboost.index[0], df_z3_lstm.index[0],
                              df_z3_lstm1h.index[0]]).max()
        last_day = np.array([df_z3_xgboost.index[-1], df_z3_lstm.index[-1],
                             df_z3_lstm1h.index[-1]]).min()
        
        # Merge the dataframe
        df_z3_xgboost.rename(columns={"prediction":"XGBoost"}, inplace=True)
        df_z3_lstm1h.rename(columns={"prediction":"LSTM_1H"}, inplace=True)
        df_z3_lstm.rename(columns={"prediction":"LSTM_1H_1variable"}, inplace=True)
        df_data = pd.concat([df_z3_xgboost, df_z3_lstm1h[["LSTM_1H"]],
                             df_z3_lstm[["LSTM_1H_1variable"]]], axis=1)
        target="Consumption_Z3"
        
    if window == 'Globale':           
        with st.container():
            if kind == 'Temporelle':
                with st.spinner(text="En cours ..."):
                    st.pyplot(mpl_display_ts_multiple_predictions(
                        df_data, l_pred_col=l_pred_col,
                        true_y=target, x_label='', y_label="Consumption (KW)",
                        title="", ax_titles=ax_titles))
            else:
                df_data = create_datetime_features(df_data=df_data)
                with st.container():
                    st.write("**Consommation en KW par mois**")
                    st.pyplot(sns_display_boxplot(df_data, x="Month", l_pred_col=l_pred_col,
                                                  true_y=target, y_label='',
                                                  title="",
                                                  ax_titles=ax_titles,
                                                  x_label="Numéro de mois de l'année"))
                with st.container():
                    st.write("**Consommation en KW par heure**")
                    st.pyplot(sns_display_boxplot(df_data, x="Hour", l_pred_col=l_pred_col,
                                                  true_y=target, y_label='',
                                                  title="",
                                                  ax_titles=ax_titles,
                                                  x_label="Heures de la journée"))
    else:
       # Sélectionner un intervalle de dates
       st.info("""
           :point_down: **Période de visualisation personnalisée.**
       """)
       date_range = \
           st.date_input("Choisisez une période de visualisation",
                         value=(first_day,
                                first_day+pd.DateOffset(days=7)),
                         min_value=first_day, max_value=last_day)
       if len(date_range) == 1:
           date_range = (date_range[0], 
                         min(date_range[0]+pd.DateOffset(days=7), last_day))
       
       if kind == 'Temporelle':
           df_sub_data = df_data[date_range[0]:date_range[1]]
           with st.spinner(text="En cours ..."):
               st.pyplot(mpl_display_ts_multiple_predictions(
                   df_sub_data, l_pred_col=l_pred_col,
                   true_y=target, x_label='', y_label="Consumption (KW)",
                   title="", ax_titles=ax_titles))
       else:
           df_data = create_datetime_features(df_data=df_data)
           df_sub_data = df_data[date_range[0]:date_range[1]]
           with st.container():
               st.write("**Consommation en KW par heure**")
               st.pyplot(sns_display_boxplot(df_sub_data, x="Hour", l_pred_col=l_pred_col,
                                             true_y=target, y_label='',
                                             title="",
                                             ax_titles=ax_titles,
                                             x_label="Heures de la journée")) 
      


    








































    # Row B
    # seattle_weather = pd.read_csv('https://raw.githubusercontent.com/MrdeckA/Powerforecast/main/Tetuan%20City%20power%20consumption.csv')
    seattle_weather = pd.read_csv('https://raw.githubusercontent.com/tvst/plost/master/data/seattle-weather.csv', parse_dates=['date'])
    stocks = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/stocks_toy.csv')
        # option = st.radio("Période de visualistion   :", ("Mois", "Jour", "Heure"))

    first_day = path_.index[0]
    last_day = path_.index[-1]
    
    date_range = \
    st.date_input("Choisisez une période de visualisation",
    value=(first_day, first_day+pd.DateOffset(days=30)), min_value=first_day, max_value=last_day)
            
    if len(date_range) == 1:
        date_range = (date_range[0], date_range[0]+pd.DateOffset(days=30))
            
    df_sub_data = path_[date_range[0]:date_range[1]]

  

    


