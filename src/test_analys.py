import pandas as pd
from pandas_profiling import ProfileReport
def profile():
    df = pd.read_csv("https://raw.githubusercontent.com/MrdeckA/Powerforecast/main/Tetuan%20City%20power%20consumption.csv")
    profile = ProfileReport(df) 
    return profile















# def uploaded_file():
#     st.write("Choose a file")

#     st.sidebar.header('Dashboard `version 2`')

#     st.sidebar.subheader('Heat map parameter')
#     time_hist_color = st.sidebar.selectbox('Color by', ('temp_min', 'temp_max')) 

#     st.sidebar.subheader('Donut chart parameter')
#     donut_theta = st.sidebar.selectbox('Select data', ('q2', 'q3'))

#     st.sidebar.subheader('Line chart parameters')
#     plot_data = st.sidebar.multiselect('Select data', ['temp_min', 'temp_max'], ['temp_min', 'temp_max'])
#     plot_height = st.sidebar.slider('Specify plot height', 200, 500, 250)

#     # Row A
#     st.markdown('### Metrics')
#     col1, col2, col3 = st.columns(3)
#     col1.metric("Temperature", "70 °F", "1.2 °F")
#     col2.metric("Wind", "9 mph", "-8%")
#     col3.metric("Humidity", "86%", "4%")

#     # Row B
#     # seattle_weather = pd.read_csv('https://raw.githubusercontent.com/MrdeckA/Powerforecast/main/Tetuan%20City%20power%20consumption.csv')
#     seattle_weather = pd.read_csv('https://raw.githubusercontent.com/tvst/plost/master/data/seattle-weather.csv', parse_dates=['date'])
#     stocks = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/stocks_toy.csv')

#     c1, c2 = st.columns((7,3))
#     with c1:
#         st.markdown('### Heatmap')
#         plost.time_hist(
#         data=seattle_weather,
#         date='date',
#         x_unit='week',
#         y_unit='day',
#         color=time_hist_color,
#         aggregate='median',
#         legend=None,
#         height=345,
#         use_container_width=True)
#     with c2:
#         st.markdown('### Donut chart')
#         plost.donut_chart(
#             data=stocks,
#             theta=donut_theta,
#             color='company',
#             legend='bottom', 
#             use_container_width=True)

#     # Row C
#     st.markdown('### Line chart')
#     st.line_chart(seattle_weather, x = 'date', y = plot_data, height = plot_height)


