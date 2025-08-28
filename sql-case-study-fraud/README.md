# SQL Case Study – Fraud (nocne transakcje)

## O co chodzi?
Prosty case study. Szukam anomalii w danych transakcyjnych – na start skupiłem się na nocnych godzinach (23:00–05:00).  
Idea: klient, który wykonuje dużo transakcji w nocy i dużym wolumenem → potencjalnie podejrzany.

## Jak to zrobiłem?
1. **Ranking klientów nocnych**  
   - `sql/02_rank_night_clients.sql` – liczę ile transakcji i jaki wolumen w nocy ma każdy klient.  
   - Wynik w `data/02_rank_night_clients.csv`.

2. **Szczegóły transakcji dla top klientów**  
   - `sql/04_night_high_volume_report.sql` – wybieram konkretne ID klientów i ściągam wszystkie ich transakcje w nocy (z datą, kwotą, merchant_city itp.).  
   - Wynik w `data/04_night_high_volume_report.csv`.

## Co dalej (będę rozwijał projekt)
- **Wykrywanie nietypowych wzorców (anomalie)**  
  - nocne godziny już mam; dorzucę:
    - rozdrabnianie wpłat/wypłat (seria małych transakcji w krótkim oknie),  
    - „podejrzane” końcówki kwot (np. 999.99 zamiast 1000),  
    - porównanie transakcji klienta do jego historii (WINDOW FUNCTIONS: AVG/STDDEV, LAG, rolling SUM).

- **Analiza cyklu życia transakcji**  
  - miesięczny wolumen per klient, trendy m/m, wykrywanie nagłych skoków/spadków (okna czasowe, percentyle).

- **Optymalizacja zapytań**  
  - porządek w typach danych, indeksy pod kluczowe filtry/joiny,  
  - materialized view + `REFRESH (CONCURRENTLY)` do szybkich raportów,  
  - krótkie uzasadnienia „dlaczego tak”, z `EXPLAIN/EXPLAIN ANALYZE` (na próbce).

## Jak odpalić?
1. Uruchom zapytania z `sql/` w swojej bazie Postgres (kolejność: najpierw `02`, potem `04`).  
2. Wyniki zapiszą się w CSV – przykładowe są już w folderze `data/`.  
3. Możesz podmienić listę ID w `04_night_high_volume_report.sql`, żeby przeanalizować innych klientów.

---

💡 To jest wersja 1.0 – baza pod dalsze analizy fraudowe. Kolejne anomalie i optymalizacje będę dorzucał na bieżąco.