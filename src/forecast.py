import streamlit as st
import pandas as pd
from io import StringIO
import plost
import pickle
import pickle
from streamlit_option_menu import option_menu
from src.data_analysis import importation_of_dataset  , box_plot , add_month_or_hour, boxplot_months
import numpy as np
import matplotlib.pyplot as plt

df = ""

def mpl_display_ts_multiple_predictions(df_data, l_pred_col, true_y, x_label='', y_label='',
                                        title="Power consumption prediction",
                                        ax_titles=None):
    
    n_pred = len(l_pred_col)
    fig, ax = plt.subplots(n_pred, 1, figsize=(10, 8), constrained_layout=True,
                           sharex=True, sharey=True)
   
    
    if ax_titles is None or len(ax_titles) < n_pred:
        ax_titles=['Prediction {}'.format(i) for i in range(n_pred)]

    for i in range(n_pred):
        df_data.plot(y=true_y, ax=ax, color='k', linewidth=1)
        df_data.plot(y=l_pred_col[i], ax=ax, color='b', 
                              style='.',linewidth=0.1, alpha=0.2)
        ax.set_title(ax_titles[i])
        ax.legend(["Raw Data", l_pred_col[i]], bbox_to_anchor=(1.02, 1), 
                     loc='upper left', borderaxespad=0)
        ax.set_ylabel(y_label)
    fig.suptitle(title)
    # return (fig, df_data[:5], df_data)
    return (fig, df_data[:5])

def read_pred_results(file_pkl):
    with open(file_pkl, 'rb') as fp:
        df_predictions = pickle.load(fp)
    return df_predictions

def draw_forecast_page():
    path_ = "Tetuan City power consumption.csv"
    path_ = importation_of_dataset(path_)

    first_day = path_.index[0]
    last_day = path_.index[-1]
    


    # Différents fichiers de résultats
    # Akpakpa
    file_z1_lstm1h = "predictions/Zone1/lstm1H_predictions_Consumption_Z1.pkl"

    # Calavi
    file_z2_lstm1h = "predictions/Zone2/lstm1H_predictions_Consumption_Z2.pkl"

    # Sone 3
    file_z3_lstm1h = "predictions/Zone3/lstm1H_predictions_Consumption_Z3.pkl"



     # chargement des différentes données
    df_z1_lstm1h = read_pred_results(file_z1_lstm1h)
    
    df_z2_lstm1h = read_pred_results(file_z2_lstm1h)
    
    df_z3_lstm1h = read_pred_results(file_z3_lstm1h)


    l_pred_col=["LSTM_1H"]
    ax_titles=["Prédictions LSTM_1H"]
    


    
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
                             ('Akpakpa', 'Calavi', 'Ganhi'))
        

        with window_col:
            window = st.radio("**Fenêtre d'analyse**",
                              ('Globale', 'Personnalisée')) 
            

    

   









    if zones=="Akpakpa":
        # Plage de dates des données
        first_day = df_z1_lstm1h .index[0]
        last_day = df_z1_lstm1h.index[-1]
        
        # Merge the dataframe
        df_z1_lstm1h.rename(columns={"prediction":"LSTM_1H"}, inplace=True)
        # df_data = pd.concat([df_z1_lstm1h[["LSTM_1H"]]], axis=1)        
        df_data = df_z1_lstm1h[["LSTM_1H"]]
        target="LSTM_1H"

    if zones=="Calavi":
        # Plage de dates des données
        first_day = df_z2_lstm1h.index[0]
        last_day = df_z2_lstm1h.index[-1]
        
        # Merge the dataframe
        df_z2_lstm1h.rename(columns={"prediction":"LSTM_1H"}, inplace=True)
        # df_data = pd.concat([df_z2_lstm1h[["LSTM_1H"]]], axis=1)*
        df_data = df_z2_lstm1h[["LSTM_1H"]]
        target="LSTM_1H"
        
    if zones=="Ganhi":
        # Plage de dates des données
        first_day = df_z3_lstm1h.index[0]
        last_day = df_z3_lstm1h.index[-1]
        
        # Merge the dataframe
        df_z3_lstm1h.rename(columns={"prediction":"LSTM_1H"}, inplace=True)
        #df_data = pd.concat([df_z3_lstm1h[["LSTM_1H"]]], axis=1)
        df_data = df_z3_lstm1h[["LSTM_1H"]]
        target="LSTM_1H"
        
    if window == 'Globale':           
        with st.container():
            with st.spinner(text="En cours ..."):
                    st.write(mpl_display_ts_multiple_predictions(
                        df_data, l_pred_col=l_pred_col,
                        true_y=target, x_label='', y_label="Consumption (KW)",
                        title="", ax_titles=ax_titles)[1])
                    st.pyplot(mpl_display_ts_multiple_predictions(
                        df_data, l_pred_col=l_pred_col,
                        true_y=target, x_label='', y_label="Consumption (KW)",
                        title="", ax_titles=ax_titles)[0])
                    
                


                
           
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
           
       df_sub_data = df_data[date_range[0]:date_range[1]]
       with st.spinner(text="En cours ..."):
            # st.write(mpl_display_ts_multiple_predictions(
            #             df_sub_data, l_pred_col=l_pred_col,
            #             true_y=target, x_label='', y_label="Consumption (KW)",
            #             title="", ax_titles=ax_titles)[1])
            if not st.button('Voir plus de valeurs'):
                st.write(mpl_display_ts_multiple_predictions(
                        df_sub_data, l_pred_col=l_pred_col,
                        true_y=target, x_label='', y_label="Consumption (KW)",
                        title="", ax_titles=ax_titles)[1])
                st.pyplot(mpl_display_ts_multiple_predictions(
                df_sub_data, l_pred_col=l_pred_col,
                true_y=target, x_label='', y_label="Consumption (KW)",
                title="", ax_titles=ax_titles)[0])
            else:
                # st.button("Voir plus de valeurs", on_click=st.write(df_data))
                st.write(df_data)
                st.pyplot(mpl_display_ts_multiple_predictions(
                    df_data, l_pred_col=l_pred_col,
                    true_y=target, x_label='', y_label="Consumption (KW)",
                    title="", ax_titles=ax_titles)[0])
            
    # st.write(type(df_data))
       
      
      


    


            

















    with open('style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    
   

    # Row A
    # st.markdown('### Metrics')
    # col1, col2, col3 = st.columns(3)
    # col1.metric("Temperature", "70 °F", "1.2 °F")
    # col2.metric("Wind", "9 mph", "-8%")
    # col3.metric("Humidity", "86%", "4%")

   

    


