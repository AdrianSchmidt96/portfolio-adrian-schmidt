# Projekt: KYC Transaction Analyzer

## Cel projektu

Banki zmuszone są do stałego monitoringu klientów i ich transakcji pod kątem zgodności z ich profilem ekonomicznym. Narzędzie, które stworzę wspierać będzie zespoły AML/KYC, wskazując, które transakcje warto przeanalizować dokładniej.

## Analizowane dane są stworzonyme przez AI na pdosstawie realnego szblonu jednego z banków.

## Struktura folderów

02_kyc_analyzer/
├── data/             # Dane wejściowe i oczyszczone
│   ├── raw_data/     # Surowe pliki .csv
│   └── clean_data/   # Dane po wstępnym czyszczeniu
├── notebooks/        # Główna analiza i eksploracja danych
├── output/           # Wykresy, raporty, gotowe dane
├── utils/            # Funkcje pomocnicze: czyszczenie, ładowanie danych


## Schemat pracy

- Surowe dane trzymam w lokalizacji `data/raw_data/`.
- Oczyszczone dane zapisuję w lokalizacji `data/clean_data/`.
- Fukjce wpierające pracę oraz pomagające utrzymać czystość i przejrzystość kodu np. ładowanie danych trzymam w lokalizacji `utils/`.
- Analiza oraz wykresy znajdują się wyłącznie w `notebooks/`.
- Nazwy kolumn powinny być ujednolicone: małe litery, bez spacji, z podkreślnikami.

## Kryteria red flg

- Transakcje powyżej 10.000 
- Zakupy nieruchomości, sprzedaży nieruchomości
- Bukmacherzy, casyna itd

README będzie rozwijane oraz uzupełniane w trakcie postępu prac. 