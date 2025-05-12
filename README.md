# Portfolio projektów w Pythonie – Adrian Schmidt

To repozytorium zawiera wybrane projekty stworzone w ramach mojego rozwoju zawodowego i nauki języka Python.  
Każdy projekt powstał jako praktyczne ćwiczenie umiejętności – od prostych aplikacji konsolowych, przez pracę z API, aż po przetwarzanie danych i automatyzację.

Repozytorium jest stale rozwijane – pojawiają się tutaj zarówno samodzielne aplikacje, jak i fragmenty większych systemów.

## Aktualne projekty

### 1. Menadżer listy zakupów
Aplikacja konsolowa umożliwiająca tworzenie, edytowanie i zapisywanie listy zakupów z podziałem na kategorie. Dane przechowywane są w bazie PostgreSQL.

- Technologie: Python, PostgreSQL, psycopg2
- Zakres: klasy, SQL, struktura katalogów, eksport do pliku
- Lokalizacja: [`menadzer-listy-zakupow`](./menadzer-listy-zakupow)

### 2. Konwerter walut z API NBP
Konsolowy kantor walutowy pobierający aktualne kursy z API NBP. Obsługuje wymiany między różnymi walutami oraz podstawową walidację danych wejściowych.

- Technologie: Python, API NBP, requests
- Zakres: obsługa API, klasy, logika przeliczeń
- Lokalizacja: [`konwerter-walut`](./konwerter-walut)

### 3. ETL – analiza populacji USA
Projekt ETL pobierający dane z publicznego API, przetwarzający je w Pandas i zapisujący raporty do Excela i pliku tekstowego.

- Technologie: Python, requests, Pandas, Excel
- Zakres: struktura ETL, analiza danych, eksport
- Lokalizacja: [`etl-populacja-usa`](./etl-populacja-usa)

## Technologie

- Python 3.x
- Pandas
- Requests
- PostgreSQL
- Praca z API (NBP, DataUSA)
- Aplikacje CLI

## Status repozytorium

Repozytorium w pełni gotowe do prezentacji w procesie rekrutacyjnym.  
Będę je regularnie aktualizować o kolejne projekty związane z analizą danych, automatyzacją i budową aplikacji Pythonowych.
