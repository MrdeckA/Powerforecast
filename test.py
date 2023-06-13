import streamlit as st
from streamlit_option_menu import option_menu
from pathlib import Path
import random
from src import analysis,forecast




def get_random_img(img_names: list[str]) -> str:
    return random.choice(img_names)



# Chemin vers l'image que tu veux afficher
chemin_image = "https://raw.githubusercontent.com/MrdeckA/Powerforecast/main/%5Bremoval.ai%5D_tmp-6485f96db5931_WAI3XY.png"

# Affichage de l'image
# st.image(chemin_image, width=300)




style = """
    <style>
        .image-container {
            display: flex;
            justify-content: center;
            align-items: center;
        }
        
        .image-container img {
            max-width: 60%;
            max-height: 50%;
            border-radius: 10px;
            /*box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.2);*/
            position: relative;
            bottom: 2em;
        }
    </style>
"""




# Affichage de l'image avec les styles CSS
st.markdown(style, unsafe_allow_html=True)
st.markdown(f'<div class="image-container"><img src="{chemin_image}" alt="Ma superbe image"></div>', unsafe_allow_html=True)

# pages = {
#     "Home": home,
#     "Upload": data_analysis,
#     "Tasks": predictions,
# }


text = """
La prédiction de la consommation énergétique est un réel enjeu pour les gestionnaires de réseau.

Nous proposons de faire une prévision instantanée de la consommation énergétique afin d'adopter la meilleure stratégie de stockage et de distribution.
                                                                    
Les modèles de ce projet ont été construits sur les données de la ville de Tétouan au Maroc. Les données de consommation sont données en KW pour 3 zones différentes: Zone 1, Zone 2 et Zone 3.
Tétouan est une ville du Maroc avec une population de 380 000 habitants, occupant une superficie de 11 570 km². La ville est située dans la partie nord du pays et fait face à la mer Méditerranée.
Le climat est particulièrement chaud et humide pendant l'été.

Le mix énergétique du Maroc est constitué d'un mélange d'énergie fossiles et renouvelables. 
Une bonne prédiction de la consommation permet au gestionnaire de réseau d'adapter sa stratégie de stockage.
"""

def draw_main_page():
        st.divider()
        st.write(f"<div style='text-align: justify;'>{text}</div>", unsafe_allow_html=True)
        st.divider()


# 2. horizontal menu
selected2 = option_menu(None, ['Prédictions'], 
    icons=['house', '', "list-task", 'gear'], 
    menu_icon="cast", default_index=0, orientation="horizontal")
if selected2 == "Home":
    st.image(f"Hosted/ai_face{get_random_img(['', '2', '3', '4', '5', '6', '7', '8'])}.png")
    draw_main_page()

elif selected2 == "Analyses":
    analysis.data_analysis_func()

elif selected2 == "Prédictions":
    forecast.draw_forecast_page()


# elif selected2 == "Prédictions":
#     forecast.draw_forecast_page()
    


# 4. Manual Item Selection


# if st.session_state.get('switch_button', False):
#     st.session_state['menu_option'] = (st.session_state.get('menu_option',0) + 1) % 4
#     manual_select = st.session_state['menu_option']
# else:
#     manual_select = None
    
# selected4 = option_menu(None, ["Home", "Upload", "Tasks", 'Settings'], 
#     icons=['house', 'cloud-upload', "list-task", 'gear'], 
#     orientation="horizontal", manual_select=manual_select, key='menu_4')
# st.button(f"Move to Next {st.session_state.get('menu_option',1)}", key='switch_button')
# selected4

# 5. Add on_change callback
# def on_change(key):
#     selection = st.session_state[key]
#     st.write(f"Selection changed to {selection}")
    
# selected5 = option_menu(None, ["Home", "Upload", "Tasks", 'Settings'],
#                         icons=['house', 'cloud-upload', "list-task", 'gear'],
#                         on_change=on_change, key='menu_5', orientation="horizontal")
# selected5


