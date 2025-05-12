# Kantor walutowy – pobieranie kursów z API NBP

Projekt napisany w Pythonie jako ćwiczenie nauki pracy z API, obsługi danych z JSON i podstawowych obliczeń finansowych.  
Aplikacja działa w terminalu i pozwala użytkownikowi wymieniać waluty na podstawie aktualnych kursów z API NBP.

## Funkcje

- Pobranie aktualnych kursów walut z API NBP (https://api.nbp.pl)
- Lista dostępnych walut z kodami walut
- Obsługa wymiany między:
  - PLN → waluta obca
  - waluta obca → PLN
  - waluta obca → waluta obca
- Sprawdzenie poprawności kodów walut i kwot
- Prosty interfejs tekstowy w konsoli

## Wymagania

- Python 3
- Biblioteka `requests`


## Jak uruchomić

1. Upewnij się, że masz zainstalowaną bibliotekę `requests`.
2. Uruchom plik `main.py`:

## Status
Projekt edukacyjny – ukończony