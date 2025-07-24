import pandas as pd

def remove_nan_columns(df):
    '''
    Usuwa  kolumny zawierajace w całości wartości NaN
    '''
     
    
    
    return df.dropna(axis= 1, how='all', inplace = True)