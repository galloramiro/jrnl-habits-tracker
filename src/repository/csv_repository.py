import csv
import os
from dataclasses import asdict
from typing import List

from src.config import LOGGER, JRNL_DIR
from src.data_processor.dto import MonthlyTitleRow, MonthlyHabitsRow


class CsvRepositoryError(Exception):
    """Raised when we find errors"""

    def __init__(self, path: str, description: str):
        self.description = description
        self.path = path
        self.message = f"Error when {description} in path: {path}"
        super().__init__(self.message)


class CsvRepository:
    _JRNL_DIR = JRNL_DIR

    def save_monthly_habits_rows(self, rows: List[MonthlyHabitsRow]) -> str:
        raise NotImplementedError

    def save_monthly_titles_rows(self, rows: List[MonthlyTitleRow]) -> str:
        file_name = "monthly_titles_data.csv"
        year = rows[0].year
        month = rows[0].month
        file_path = os.path.abspath(f"{self._JRNL_DIR}/{year}/{month}/{file_name}")

        LOGGER.info(
            f"Start saving data on: {file_path}",
            extra={"file_path": file_path, "rows_len": len(rows)},
        )

        headers = asdict(rows[0]).keys()
        self._save_rows(headers=headers, rows=rows, file_path=file_path)
        return file_path

    @staticmethod
    def _save_rows(headers: List[str], rows: List[MonthlyTitleRow | MonthlyHabitsRow], file_path: str) -> str:
        try:
            with open(file_path, mode="w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(headers)
                for row in rows:
                    row_data = asdict(row).values()
                    writer.writerow(row_data)
            LOGGER.info("Process finished successfully", extra={"file_path": file_path})
        except Exception as exc:
            raise CsvRepositoryError(path=file_path, description="_save_rows") from exc
        return file_path
