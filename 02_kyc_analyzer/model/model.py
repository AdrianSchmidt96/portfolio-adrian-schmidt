import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score
from sklearn.preprocessing import OrdinalEncoder
from sklearn.metrics import confusion_matrix



df = pd.read_csv('data/clean_data/after_eda/ready_to_kyc.csv')
df['iban_country'] = df['nr_rachunku'].str[:2]

x = df[['dane_kontrahenta', 'iban_country', 'kwota_transakcji_(waluta_rachunku)']]
y = df['red_flag']

encoder = OrdinalEncoder()
x.loc[:,['dane_kontrahenta', 'iban_country']] = encoder.fit_transform(x[['dane_kontrahenta', 'iban_country']])

x_train, x_test, y_train, y_test = train_test_split(x,y, test_size= 0.2, random_state=42)

model = RandomForestClassifier()
model.fit(x_train,y_train)

y_pred= model.predict(x_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("Precision:", precision_score(y_test, y_pred))
print("Recall:", recall_score(y_test, y_pred))

print(confusion_matrix(y_test, y_pred))