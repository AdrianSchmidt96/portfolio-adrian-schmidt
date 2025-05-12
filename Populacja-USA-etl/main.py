import pandas as pd
import requests
import json

url = "https://datausa.io/api/data?drilldowns=Nation&measures=Population"

data = requests.get(url).json()

df = pd.DataFrame(data['data'])


df.head()
df.columns
df = df.sort_values('Year')


df['Population'] = df['Population'].astype(int)
df['Year'] = df['Year'].astype(int)

avg_population = df['Population'].mean()

print("The average population in USA is", round(avg_population))

df['Annual_population_change'] = df['Population'].diff()

max_annual = df['Annual_population_change'].max()

print('Maximum annual is', max_annual)

df.to_excel('outputs/raport.xlsx', index= False)

with open ('data/data_raw.json', 'w') as f:
    json.dump(data,f)
    
with open ('outputs/raport.txt', 'w', encoding='utf-8') as f:
    f.write('Raport populacji USA\n')
    f.write('*****************************\n')
    f.write(f'Średnia populacja: {round(avg_population)}\n')
    f.write(f'Maksymalny roczny przyrost populacji: {round(max_annual)}\n')
    
    
print("Raporty zostały wygenerowane")