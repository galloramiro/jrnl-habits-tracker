from typing import List

from src.data_processor.dto import MonthlyTitleRow, MonthlyHabitsRow


class CsvRepository:
    def save_monthly_habits_rows(self, rows: List[MonthlyHabitsRow]) -> str:
        raise NotImplementedError

    def save_monthly_titles_rows(self, rows: List[MonthlyTitleRow]) -> str:
        raise NotImplementedError
