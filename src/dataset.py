from src.utils import load_csv

class Dataset:
    def __init__(self, name: str):
        self.name = name
        self._records: list[dict] = [] 

    def load(self, records: list[dict]) -> None:
        self._records.extend(records)

    @property
    def row_count(self) -> int:
        return len(self._records)

    @property
    def columns(self) -> list[str]:
        if self._records:
            return list(self._records[0])
        return []

    def summary(self) -> dict:
        return {
            "Dataset's name": self.name,
            "Total rows": self.row_count,
            "Total columns": self.columns
        }

    def __repr__(self) -> str:
        return f"Dataset(name={self.name!r}, rows={self.row_count})"

class CsvDataset(Dataset):
    def __init__(self, name: str):
        super().__init__(name)

    def load_from_csv(self, path: str) -> None:
        records = load_csv(path)
        self.load(records)

    def filter_by_column(self, column: str, min_value: float) -> list[dict]:
        return [record for record in self._records if float(record[column]) >= min_value]

class FilteredDataset(CsvDataset):
    def top_n(self, column: str, n: int) -> list[dict]:
        sorted_records = sorted(self._records, key=lambda record: float(record[column]), reverse=True)
        return sorted_records[:n]