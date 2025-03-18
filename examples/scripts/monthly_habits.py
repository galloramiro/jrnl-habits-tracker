import csv
import logging
import os
import re
import sys

from datetime import datetime
from dataclasses import asdict, dataclass
from typing import List


LOGGER = logging.getLogger("MonthlyHabitsLogger")
logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)


@dataclass
class Row:
    date: str
    year: int
    month: int
    day: int
    week_number: int
    description: str
    value: int
    tag: str


class MonthlyHabits:
    HEALTH_TAGS = ("@Health", "@PositiveHabits")
    POSITIVE_HABITS_TAGS = ("@PositiveHabits", "@NegativeHabits")
    NEGATIVE_HABITS_TAGS = ("@NegativeHabits", "@ConvictConditioning")
    CONVICT_CONDITIONING_TAGS = ("@ConvictConditioning", "@DailyTasks")

    def generate_data_by_month(self, month: str):
        LOGGER.debug(f"Start generating data for month: {month}", extra={"month": month})
        files_path = self._get_list_of_files(month=month)

        monthly_view_data = []

        for file_path in files_path:

            with open(file_path, "r") as journal_day:
                journal_day_text = journal_day.read()

                date = self._get_date_string(text=journal_day_text)

                health_data = self._extract_data_from_tag(
                    start_tag=self.HEALTH_TAGS[0],
                    end_tag=self.HEALTH_TAGS[1],
                    text=journal_day_text,
                )
                monthly_view_data += self._clean_tag_data(text=health_data, date=date)

                positive_habits_data = self._extract_data_from_tag(
                    start_tag=self.POSITIVE_HABITS_TAGS[0],
                    end_tag=self.POSITIVE_HABITS_TAGS[1],
                    text=journal_day_text,
                )
                monthly_view_data += self._clean_tag_data(text=positive_habits_data, date=date)

                negative_habits_data = self._extract_data_from_tag(
                    start_tag=self.NEGATIVE_HABITS_TAGS[0],
                    end_tag=self.NEGATIVE_HABITS_TAGS[1],
                    text=journal_day_text,
                )
                monthly_view_data += self._clean_tag_data(text=negative_habits_data, date=date)

                convict_conditioning_data = self._extract_data_from_tag(
                    start_tag=self.CONVICT_CONDITIONING_TAGS[0],
                    end_tag=self.CONVICT_CONDITIONING_TAGS[1],
                    text=journal_day_text,
                )
                monthly_view_data += self._clean_tag_data(text=convict_conditioning_data, date=date)

        self._save_data_into_a_csv(data=monthly_view_data, path=files_path[0])

    def _get_list_of_files(self, month: str) -> List[str]:
        JRNL_PATH = "./examples/jrnl-dir/"
        month_path = os.path.abspath(f"{JRNL_PATH}2025/{month}")

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

    def _get_date_string(self, text: str) -> str:
        match = re.search(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} [A-Z]{2}", text)

        # match = re.search(r"\d{4}-\d{2}-\d{2}", text)
        return match.group()

    def _get_year_month_day_week_number(self, date: str) -> List[int]:
        LOGGER.debug(f"Parsing datetime data from: {date}", extra={"date": date})
        date = datetime.strptime(date, "%Y-%m-%d %I:%M:%S %p")
        year = date.year
        month = date.month
        day = date.day
        week_number = date.isocalendar().week
        LOGGER.debug(
            "Datetime data sucsessfuly parsed",
            extra={
                "year": year,
                "month": month,
                "day": day,
                "week_number": week_number,
            },
        )
        return year, month, day, week_number

    def _extract_data_from_tag(self, start_tag: str, end_tag: str, text: str) -> str:
        """
        Text would be looking something like this:
            '[2024-07-21 11:37:43 PM] # Day\n@tag_1\ndata_1: 9\ndata_2: 6\ndata_3: 4\n\n@tag_2\n- data_1: 1\n- data_2: (...)'
        """
        LOGGER.debug(
            f"Start extracting data for tag: {start_tag}",
            extra={"start_tag": start_tag, "end_tag": end_tag},
        )
        start_tag_index = text.index(start_tag)
        end_tag_index = text.index(end_tag)
        extracted_data = text[start_tag_index:end_tag_index]
        LOGGER.debug(
            f"For {start_tag} we found this data: {extracted_data}",
            extra={
                "start_tag": start_tag,
                "end_tag": end_tag,
                "extracted_data": extracted_data,
            },
        )
        return extracted_data

    def _clean_tag_data(self, text: str, date: str) -> List[Row]:
        """
        Tag data would be looking something like this:
            '@Health\nSueño: 9\nHumor: 6\nEstres: 4\n\n'
        """
        LOGGER.debug(f"Cleaning data for {date}", extra={"text": text, "date": date})
        clean_data = []
        rows = text.split("\n")
        tag = rows[0].replace("@", "")
        rows_with_valid_data = list(filter(lambda row: row.strip() not in ["", "None"], rows[1:]))

        # TODO: change this, I dont like calling the 3 layers of deepnes on the functions calling functions
        year, month, day, week_number = self._get_year_month_day_week_number(date=date)

        LOGGER.debug(
            f"Rows with vslid data for tag: {tag} and date {date}",
            extra={"tag": tag, "rows_with_valid_data": rows_with_valid_data},
        )
        if not rows_with_valid_data:
            LOGGER.warning(
                f"No valid data found for tag {tag} and date {date}",
                extra={"tag": tag, "date": date, "text": text},
            )
            return [
                Row(
                    date=date,
                    year=year,
                    month=month,
                    day=day,
                    week_number=week_number,
                    description="no_valid_data",
                    value=0,
                    tag=tag,
                )
            ]

        for row in rows_with_valid_data:
            description, value = row.split(":")

            description = description.replace("-", "")
            description = description.strip()
            value = value.strip()

            clean_data.append(
                Row(
                    date=date,
                    year=year,
                    month=month,
                    day=day,
                    week_number=week_number,
                    description=description,
                    value=value,
                    tag=tag,
                )
            )

        LOGGER.debug(
            f"Clean data for tag {tag} and date {date}",
            extra={"tag": tag, "date": date, "clean_data": clean_data},
        )

        return clean_data

    def _save_data_into_a_csv(self, data: List[Row], path: str) -> None:
        file_name_index = path.rfind("/")
        file_path = f"{path[:file_name_index]}/monthly_habits_data.csv"

        with open(file_path, mode="w", newline="") as file:
            writer = csv.writer(file)

            header = asdict(data[0]).keys()
            writer.writerow(header)

            for row in data:
                row_data = asdict(row).values()
                writer.writerow(row_data)


if __name__ == "__main__":
    month_number = sys.argv[1]

    data_generator = MonthlyHabits()
    data_generator.generate_data_by_month(month=month_number)
