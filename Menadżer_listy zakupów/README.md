# Menadżer listy zakupów (aplikacja konsolowa)

To mój pierwszy projekt w Pythonie, zrealizowany w ramach nauki podstaw programowania ;)
Aplikacja umożliwia zarządzanie listą zakupów z podziałem na kategorie i zapis danych do bazy PostgreSQL.

## Funkcje

- Dodawanie nowych produktów do listy z przypisaniem kategorii
- Zapis danych do bazy PostgreSQL (tabela `shopping_list_manager`)
- Wyświetlanie aktualnej listy zakupów
- Edycja istniejących pozycji
- Eksport listy do pliku `lista.txt`


## Wymagania

- Python 3
- PostgreSQL (baza `MLZ`, tabela `shopping_list_manager`)
- Biblioteka `psycopg2`

## Jak uruchomić

Upewnij się, że PostgreSQL działa i masz utworzoną bazę `MLZ` oraz tabelę:

```sql
CREATE TABLE shopping_list_manager (
    id SERIAL PRIMARY KEY,
    name TEXT,
    value TEXT,
    category TEXT
)
python main.py
```

## Uwagi
Projekt został stworzony jako forma nauki – wykorzystuje import modułów, pracę z klasami, podstawy interakcji z bazą danych i zapis do pliku.

## Status
Projekt edukacyjny – ukończony.