import pandas as pd

def red_flag_analyzer(df,out_data='../data/clean_data/after_eda/ready_to_kyc.csv'):
    
    
    df['red_flag'] = df.apply(lambda row: role(row), axis = 1)
    
    
    
    return df.to_csv(out_data)


hrc = [
    "AF",  # Afghanistan
    "DZ",  # Algeria
    "AO",  # Angola
    "BF",  # Burkina Faso
    "CM",  # Cameroon
    "CI",  # Côte d'Ivoire
    "CD",  # Democratic Republic of Congo
    "HT",  # Haiti
    "LB",  # Lebanon
    "ML",  # Mali
    "MC",  # Monaco
    "MZ",  # Mozambique
    "IR",  # Iran
]

bukmachers = [
    'STS.pl',
    'Fortuna',
    'LV BET',
    'Betclic',
    'Totolotek',
    'Superbet',
    'Betfan',
    'Etoto',
    'forBET',
    'Totalbet',
    'Fuksiarz',
    'PokerStars',
    'Unibet',
    'Bet365',
    'Bwin',
    '1XBET',
    'William Hill',
    '888sport',
    'PZBuk',
    'EnergyBet'
]

def role (row):
    
    if row['dane_kontrahenta'] in bukmachers:
        return 1
    elif row['dane_kontrahenta'] == 'ATM ING' and row['kwota_transakcji_(waluta_rachunku)'] > 5000:
        return 1
    elif row['nr_rachunku'][:2] in hrc:
        return 1
    elif row['kwota_transakcji_(waluta_rachunku)'] > 10000:
        return 1
    elif row['kwota_transakcji_(waluta_rachunku)'] < -10000:
        return 1
    else:
        return 0