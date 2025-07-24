import pandas as pd

# Stworzenie funkcji,która odpowiada za wstępne czyszczenie i ujednolicenie kolumn


def clean_column_and_save (df, out_data='../data/clean_data/cleaned_creditcard.csv'):
    '''
    Czyści nazwy kolumn:
    - zamienia wszystkie litery na małe,
    - usuwa białe znaki z początku i końca,
    - zamienia spacje na podkreślenia,
    - zapisuje plik w wybranej lokalizacji
    '''
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_', regex=False)
    
    df.to_csv(out_data)
    print(f'Dane zapisane w:  {out_data}')
    return df