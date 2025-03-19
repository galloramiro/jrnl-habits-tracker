from typing import List

from src.config import JRNL_DIR


class LocalClient:
    _JRNL_DIR = JRNL_DIR

    def get_file_paths_by_month(self, month: int) -> List[str]:
        raise NotImplementedError

    def get_jrnl_files_path_by_month(self, month: int) -> List[str]:
        raise NotImplementedError

    def get_monthly_habits_by_month(self, month: int) -> List[str]:
        raise NotImplementedError

    def get_monthly_habits_files_paths_by_year(self, month: int) -> List[str]:
        raise NotImplementedError

    def get_monthly_titles_by_month(self, month: int) -> List[str]:
        raise NotImplementedError

    def get_monthly_titles_files_paths_by_year(self, month: int) -> List[str]:
        raise NotImplementedError
