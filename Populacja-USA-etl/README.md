# Projekt: Analiza populacji USA (ETL z użyciem API)

Projekt zrealizowany w ramach mojego planu rozwoju zawodowego – skupionego na analizie danych i automatyzacji z wykorzystaniem Pythona.  
Celem było wykonanie kompletnego mini-procesu ETL: pobranie danych z otwartego API, ich przekształcenie oraz wygenerowanie prostego raportu.

Projekt ma charakter edukacyjny, ale oparty jest o realne dane, strukturę plików i logikę pracy zbliżoną do tej, z którą spotykam się w środowisku korporacyjnym.

## Zakres projektu

- Pobranie danych z API (datausa.io)
- Przekształcenie danych JSON do DataFrame
- Obliczenie średniej populacji i zmian rocznych
- Zapis danych do raportów: Excel i tekstowy

## Technologie

- Python 3
- Pandas
- Requests

## Jak uruchomić:

```bash
pip install pandas requests openpyxl
python main.py
```
Raport zostanie zapisany w folderze outputs/, a dane źródłowe w folderze data/.

## Status
Projekt ukończony.

W kolejnych projektach planuję rozszerzyć proces ETL o integrację z bazami danych oraz wizualizacje.