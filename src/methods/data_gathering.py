import pandas as pd

def importation_of_dataset(path_):
    data_consumption=pd.read_csv(path_,index_col=0,parse_dates=['DateTime'])