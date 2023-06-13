import streamlit as st
from streamlit_option_menu import option_menu
from pathlib import Path
import random
from src import analysis 
import src.forecast as h 



def load_custom_css():
    st.markdown('<link href="style.css" rel="stylesheet">', unsafe_allow_html=True)

# Appeler la fonction pour charger le CSS personnalisé

def get_random_img(img_names: list[str]) -> str:
    return random.choice(img_names)


load_custom_css()
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
            /box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.2);/
            position: relative;
            bottom: 5em;
        }
    </style>
"""




# Affichage de l'image avec les styles CSS
st.markdown(style, unsafe_allow_html=True)
st.markdown(f'<div class="image-container"><img src="{chemin_image}" alt="Ma superbe image"></div>', unsafe_allow_html=True)
# st.write(f'<h3 class="text" >Prévision de la consommation énergétique</h3>', unsafe_allow_html=True)
# pages = {
#     "Home": home,
#     "Upload": data_analysis,
#     "Tasks": predictions,
# }


text = """
L'autosuffisance énergétique demeure un enjeu de taille pour chaque nation.

Notre projet consiste en une prévision instantanée de la consommation énergétique afin d'optimiser les réseaux de distribution et les adopter les meilleurs stratégies de stockage.
                                                                    
Les modèles de ce projet ont été construits sur les données de la ville de Tétouan au Maroc et apposés à trois villes de cotonou dont Calavi, Ganhi et Akpakpa. Les données de consommation sont données en KW pour ces trois zones.



"""

def draw_main_page():
        st.divider()
        st.write(f"<div style='text-align: justify;'>{text}</div>", unsafe_allow_html=True)
        st.divider()

# st.markdown(f'<div class="image-container"><img src="{chemin_image}" alt="Ma superbe image"></div>', unsafe_allow_html=True)
# 2. horizontal menu
selected2 = option_menu(None, ["Accueil", "Etat de Consommation", 'Prévisions'], 
    icons=['house', '', "list-task", 'gear'], 
    menu_icon="cast", default_index=0, orientation="horizontal")
if selected2 == "Accueil":
    # st.image(f"Hosted/ai_face{get_random_img(['', '2', '3', '4', '5', '6', '7', '8'])}.png")
    #st.markdown(f'<div class="image-container"><img src="{chemin_image}" alt="Ma superbe image"></div>', unsafe_allow_html=True)

    draw_main_page()
    

elif selected2 == "Etat de Consommation":
    st.write(f"<h4 style='text-align: justify;'>Habitudes de consommation</h3>", unsafe_allow_html=True)

    analysis.data_analysis_func()

elif selected2 == "Prévisions":
    h.draw_forecast_page()
