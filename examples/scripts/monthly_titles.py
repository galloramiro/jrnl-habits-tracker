import csv
import logging
import os
import re
import sys

from datetime import datetime

from dataclasses import asdict, dataclass
from typing import List


LOGGER = logging.getLogger("MonthlyTitlesLogger")
logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)


@dataclass
class Row:
    date: str
    title: str
    week_number: int
    weekday_number: int
    month: int
    year: int
    time: str


class MonthlyTitles:
    JOURNAL_TAG = "@Journaling"

    def generate_data_by_month(self, month: str) -> None:
        LOGGER.debug(f"Start generating data for month: {month}", extra={"month": month})
        files_path = self._get_list_of_files(month=month)

        monthly_data = []

        for file_path in files_path:
            with open(file_path, "r") as journal_day:
                base_day_text = journal_day.read()
                date = self._get_date_string(text=base_day_text)
                year, month, week_number, weekday_number, time = (
                    self._get_year_month_week_number_weekday_number_and_time(date=date)
                )
                journal_day_text = self._filter_journal_text(text=base_day_text)
                titles = self._get_and_clean_titles(text=journal_day_text)
                # dates = self._get_titles_dates(text=journal_day_text)
                # TODO: fix date data, because im using the first entry for all the titles, and that's wrong.
                for title in titles:
                    monthly_data.append(Row(date, title, week_number, weekday_number, month, year, time))

        self._save_data_into_a_csv(data=monthly_data, path=files_path[0])

    def _get_list_of_files(self, month: str) -> List[str]:
        JRNL_PATH = os.environ.get("JRNL_PATH")
        month_path = os.path.abspath(f"{JRNL_PATH}2024/{month}")

        files = []

        for file in os.listdir(month_path):
            if file.endswith(".txt"):
                files.append(os.path.join(month_path, file))

        files.sort()

        number_of_files = len(files)
        LOGGER.debug(
            f"We find {number_of_files} files in the following path: {month_path}",
            extra={"month_path": month_path, "number_of_files": number_of_files},
        )
        return files

    def _filter_journal_text(self, text) -> str:
        journal_tag_index = text.index(self.JOURNAL_TAG)
        return text[journal_tag_index:]

    def _get_date_string(self, text: str) -> str:
        match = re.search(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} [A-Z]{2}", text)
        if match:
            return match.group(0)
        else:
            return

    def _get_year_month_week_number_weekday_number_and_time(self, date: str) -> List[int]:
        LOGGER.debug(f"Parsing datetime data from: {date}", extra={"date": date})
        date = datetime.strptime(date, "%Y-%m-%d %I:%M:%S %p")
        year = date.year
        month = date.month
        week_number = date.isocalendar().week
        weekday_number = date.isocalendar().weekday
        time = date.time().strftime("%H:%M:%S")
        LOGGER.debug(
            "Datetime data sucsessfuly parsed",
            extra={
                "year": year,
                "month": month,
                "week_number": week_number,
                "weekday_number": weekday_number,
                "time": time,
            },
        )
        return year, month, week_number, weekday_number, time

    def _get_and_clean_titles(self, text: str) -> List[str]:
        LOGGER.debug("Cleaning titles", extra={"text": text})
        regex_str = re.compile("### (.*)")
        titles = re.findall(regex_str, text)
        LOGGER.debug("Titles cleaned", extra={"titles": titles})
        return titles

    def _save_data_into_a_csv(self, data: List[Row], path: str) -> None:
        file_name_index = path.rfind("/")
        file_path = f"{path[:file_name_index]}/monthly_titles_data.csv"
        LOGGER.debug(
            f"Start saving data on: {file_path}",
            extra={"file_path": file_path, "rows_len": len(data)},
        )
        with open(file_path, mode="w", newline="") as file:
            writer = csv.writer(file)

            header = asdict(data[0]).keys()
            writer.writerow(header)

            for row in data:
                row_data = asdict(row).values()
                writer.writerow(row_data)
        LOGGER.debug("Process finished sucsessfuly")


if __name__ == "__main__":
    month_number = sys.argv[1]

    data_generator = MonthlyTitles()
    data_generator.generate_data_by_month(month=month_number)
