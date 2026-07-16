# Tests Manuels - utils.py

| Fonction                | Entree (Donnees de test)             | Resultat attendu        | Statut |
| :---------------------- | :----------------------------------- | :---------------------- | :----- |
| `average_score()`       | `[]` (Liste vide)                    | `0.0`                   | OK     |
| `average_score()`       | `[{"score": "10"}, {"score": "20"}]` | `15.0`                  | OK     |
| `filter_by_min_score()` | sample.csv, `min_score=10`           | 9 lignes retournees     | OK     |
| `filter_by_min_score()` | sample.csv, `min_score=20`           | 0 lignes retournees     | OK     |
| `summarize()`           | `[]` (Liste vide)                    | dict avec que des 0     | OK     |
| `summarize()`           | sample.csv                           | count: 10, max: 19.0... | OK     |
