# Lit un CSV simple et retourne une liste de dictionnaires. Utiliser uniquement le module csv (pas pandas pour l'instant).
import csv
from pathlib import Path

def load_csv(path: str | Path) -> list[dict]:
    with open(path, mode="r", newline="") as f:
        return list(csv.DictReader(f))

# Retourne les enregistrements dont score >= min_score.
def filter_by_min_score(records: list[dict], min_score: float) -> list[dict]:
    return [record for record in records if float(record["score"]) >= min_score]

# Calcule la moyenne du champ 'score'. Retourne 0.0 si liste vide.
def average_score(records: list[dict]) -> float:
    if not records:
        return 0.0
    return sum(float(record["score"]) for record in records) / len(records) 

# Retourne {'count': n, 'avg_score': x, 'max_score': y, 'min_score': z}
def summarize(records: list[dict]) -> dict:
    if not records:
        return {'count': 0, 'avg_score': 0.0, 'max_score': 0.0, 'min_score': 0.0}
    scores = [float(record["score"]) for record in records]

    return {
        'count': len(records),
        'avg_score': average_score(records),
        'max_score': max(scores),
        'min_score': min(scores)
    }




    
    