from typing import List

from src.data_processor.dto import MonthlyTitleRow, MonthlyHabitsRow


class DataProcessor:
    HEALTH_TAGS = ("@health", "@PositiveHabits")
    POSITIVE_HABITS_TAGS = ("@PositiveHabits", "@NegativeHabits")
    NEGATIVE_HABITS_TAGS = ("@NegativeHabits", "@ConvictConditioning")
    CONVICT_CONDITIONING_TAGS = ("@ConvictConditioning", "@DailyTasks")
    JOURNAL_TAG = ("@journaling", "")

    def generate_monthly_titles_rows(self, jrnl_files_paths: List[str]) -> List[MonthlyTitleRow]:
        raise NotImplementedError

    def generate_monthly_habits_rows(self, jrnl_files_paths: List[str]) -> List[MonthlyHabitsRow]:
        raise NotImplementedError
