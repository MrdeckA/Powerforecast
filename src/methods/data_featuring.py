x_selected1=['hour', 'Temperature', 'months']
x_selected2=['hour', 'months', 'general diffuse flows', 'Temperature', 'Humidity']
x_selected3=['months', 'hour', 'Temperature']

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
