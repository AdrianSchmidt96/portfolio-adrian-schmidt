#Analiza danych sprzedażowych

Poprzez analizę danych sprzedażowych, chcę ustalić:
- którzy klienci przynaszą największe zyski,
- które produkty sprzedają się najlepiej,
- w których krajach jest najlpesza sprzedaż oraz przychody,
- czy pora roku ma znaczenie w przypadku sprzedaży. 

Całość realizowana jest w Pythonie z użyciem notatnika Jupyter oraz bibliotek: Pandas, Matplotlib, Seaborn czy Datetime.

Dane pochodzą z Kaggle - sales_data_sample.csv - http://kaggle.com/datasets/kyanyoga/sample-sales-data

Dziś (16.06.2025) wykonałem:
- wczytanie oraz ekploracja danych,
- oczyszczenie oraz sformatowanie dat,
- dodanie kolumn miesiąc, kwartał, rok i przychód,
- analizę klientów: sumę przychodów, liczbę zamówień, ich udział w sprzedaży oraz klasyczną regułę 80/20,
- wizualizację TOP 5 klientów