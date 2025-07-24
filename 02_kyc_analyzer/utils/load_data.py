import pandas as pd

'''
Stworzenie funkcji, która przekonweruje dane z CSV na DataFrame
'''


def load_data(path):
    '''
    Zachowuje czystość kodu, 
    oraz w przyszłości mogę rozszerzyć funkcję 
    do otwierania plików Excel czy JSON.
    '''
    return pd.read_csv(path)