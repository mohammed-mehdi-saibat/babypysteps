from src.utils import load_csv, filter_by_min_score, average_score, summarize

if __name__ == "__main__":
    records = load_csv("data/sample.csv")
    print(f"Total records: {len(records)}")

    passed = filter_by_min_score(records, min_score=10)
    print(f"Admis (score >= 10): {len(passed)}")

    print(f"Resume: {summarize(records)}")