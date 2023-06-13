x_selected1=['hour', 'Temperature', 'months']
x_selected2=['hour', 'months', 'general diffuse flows', 'Temperature', 'Humidity']
x_selected3=['months', 'hour', 'Temperature']

def sanity(path_):
    """The purpose is to be sure that the dataset is clean and the and that the data schema is the same as the one we use as a basis"""
    if((path_.isna().sum()).sum()>0):
        path_.dropna(inplace=True)

def importation_of_dataset(path_):
    import pandas as pd
    data_consumption=pd.read_csv(path_,index_col=0,parse_dates=['DateTime'])
    return data_consumption

def box_plot(data_consumption, col):
    import seaborn as sn
    import matplotlib.pyplot as plt 
    sn.boxplot(data_consumption[col])
    # sn.plot(data_consumption[col])
    # plt.title('{}'.format(col))
    
def histplot_(col,data_consumption):
    import seaborn as sn
    sn.histplot(data_consumption[col],kde=True)
    
def skew_kurt(col,data_consumption):
    print("The skewness of {} is {} :".format(col,data_consumption[col].skew()))
    #print("The kurtosis ofis {} :".format(kurtosis(data_consumption)))
    
def plot_series(columns_,data_consumption):
    data_consumption[columns_].plot(subplots=True, figsize=(30, 30))        

    
def boxplot_year(df,x_="months",y_="Zone 1 Power Consumption"):
    import matplotlib.pyplot as plt 
    import seaborn as sn

    plt.figure(figsize=(10,3))
    # sn.boxplot(data=df,x=x_,y=y_)
    # sn.histplot(data=df,x=x_,y=y_)
    sn.lineplot(data=df,x=x_,y=y_)
    # plt.plot(data=df,x=x_,y=y_)
    plt.show()

def boxplot_month(df,x_="hour",y_="Zone 1 Power Consumption"):
    import matplotlib.pyplot as plt 
    import seaborn as sn

    plt.figure(figsize=(7,3))
    # sn.boxplot(data=df,x=x_,y=y_)
    # sn.histplot(data=df,x=x_,y=y_)
    sn.lineplot(data=df,x=x_,y=y_)
    # plt.plot(data=df,x=x_,y=y_)
    plt.show()
    
def boxplot_min(df,x_="hour",y_="Zone 1 Power Consumption"):
    import matplotlib.pyplot as plt 
    import seaborn as sn
    plt.figure(figsize=(10,3))
    sn.lineplot(data=df,x=x_,y=y_)
    # sn.boxplot(data=df,x=x_,y=y_)
    plt.show()

    
def compute_var(df,col,y_="Zone 1 Power Consumption"):
    import matplotlib.pyplot as plt 
    import seaborn as sn
    sn.histplot(x=df[col],y=df[y_])
    return plt.show()


    
def compute_adfuller(time_series,df):
    from statsmodels.tsa.stattools import adfuller
    stationarized=df[time_series]
    total_order = 0
    if adfuller(df[time_series])[1] > 0.05:
        #difference if the adfuller test p-value is greater than 0.05- test de stationnarite
        diff = (stationarized - stationarized.shift(1)).dropna()    
        stationarized, order = stationarize(diff) # stationarize the difference
        total_order = order + 1
    else :
        print("serie stationnaire")
    return stationarized, total_order



def plot_acf_pacf(ts, fig = None):
    import matplotlib.pyplot as plt 
    # import seaborn as sn
    fig = plt.figure(figsize=(20, 10))
    sub1 = fig.add_subplot(121)
    #sm.graphics.tsa.plot_acf(ts, ax=sub1,lag=12)
    plot_acf(ts, ax=sub1) # plot acf
    plt.title('ACF')
    
    sub2 = fig.add_subplot(122)
    plot_pacf(ts, ax=sub2, method='ywm') # plot pacf
    plt.title('PACF')
        
        
def decomposition_(ts):
    decomposition = seasonal_decompose(ts.loc["2017-01", "Zone 1 Power Consumption"], period=6*24)
    fig=decomposition.plot()
    fig.set_size_inches((15, 6))
    
def importances_var(name_of_model,features_):
    # Importance des variables
    plt.figure(figsize=(25,25))
    features_important=pd.Series(name_of_model.feature_importances_, index=features_.columns).sort_values(ascending=False)
    sn.barplot(x=features_important.index, y=features_important)
    plt.xlabel("Variables")
    plt.ylabel("score of importance")
    plt.title("Importance of feature")
    plt.show()
    return features_important



def add_month_or_hour(dataset):
    dataset['months']=dataset.index.map(lambda x: x.month)
    dataset['hour']=dataset.index.map(lambda x: x.hour)
    return dataset

def selection_of_var(dataset,zone=1):
    dataset=add_month_or_hour(dataset)
    if zone==1:
        dataset=pd.concat([dataset[x_selected1],dataset["Zone 1 Power Consumption"]],axis=1)
    if zone==2:
        dataset=pd.concat([dataset[x_selected2],dataset["Zone 2 Power Consumption"]],axis=1)
    if zone==3:
        dataset=pd.concat([dataset[x_selected3],dataset["Zone 3 Power Consumption"]],axis=1)
    return dataset



def for_standardisation(dataset):
    scaler=MinMaxScaler()
    return pd.DataFrame(scaler.fit_transform(dataset),columns=dataset.columns)



def separation_of_dataset(dataset,label_name="Zone 1 Power Consumption",test_size=0.2):
    features=dataset.drop(label_name,axis=1)
    label=dataset[label_name]
    x_train,x_test,y_train,y_test=train_test_split(features,label,test_size=0.2,shuffle=False)
    return x_train,x_test,y_train,y_test



    