import csv
from calendar import weekday, monthrange
from datetime import datetime
from typing import List

from blessed import Terminal


class ConsoleGraphicTool:
    # https://www.nerdfonts.com/cheat-sheet
    _blank_check = "  "  # 󰄱 
    _completed_check = "  "  # 󰡖 󰄯 󰄮 
    _sleep = "  "
    _humor = "  "
    _stress = "  "
    _terminal = Terminal()

    def generate_positive_habits_graph(self, file_path: str) -> str:
        data = self._from_csv_to_list_of_dict(file_path=file_path)
        year = int(data[0]["year"])
        month = int(data[0]["month"])
        days_in_month = self._generate_month_range(month=month, year=year)
        data = self._filter_by_tag(data=data, tag="PositiveHabits")
        descriptions = self._get_unique_descriptions(data=data)
        descriptions_lines = self._generate_lines_for_description(
            data=data, descriptions=descriptions, days_in_month=days_in_month
        )
        days_line = self._generate_days_line(month=month, year=year)
        return descriptions_lines + days_line

    def generate_negative_habits_graph(self) -> str:
        raise NotImplementedError

    def generate_health_graph(self) -> str:
        raise NotImplementedError

    def generate_day_titles_graph(self) -> str:
        raise NotImplementedError

    def generate_week_titles_graph(self) -> str:
        raise NotImplementedError

    def generate_month_titles_graph(self) -> str:
        raise NotImplementedError

    def _generate_days_line(self, month: int, year: int = datetime.now().year) -> str:
        month_days = monthrange(year, month)[1]
        number_days_line = ""
        letters_days_line = ""

        days_letter = {0: "L", 1: "M", 2: "M", 3: "J", 4: "V", 5: "S", 6: "D"}

        for day in range(1, month_days + 1):
            zero_padded_day = str(day).zfill(2)
            number_days_line += f"{zero_padded_day} "
            letter_weekday = days_letter[weekday(year, month, day)]
            letters_days_line += f" {letter_weekday} "

        color_number_days_line = f"{self._terminal.magenta}{number_days_line}"
        color_letters_days_line = f"{self._terminal.magenta}{letters_days_line}"
        complete_color_line = f"{color_number_days_line}\n{color_letters_days_line}"

        return complete_color_line

    @staticmethod
    def _from_csv_to_list_of_dict(file_path: str) -> List[dict]:
        with open(file_path, mode="r", newline="") as file:
            reader = csv.DictReader(file)
            return [row for row in reader]

    @staticmethod
    def _generate_month_range(month: int, year: int) -> List[int]:
        month_days = monthrange(year, month)[1]
        return list(range(1, month_days + 1))

    @staticmethod
    def _filter_by_tag(data: List[dict], tag: str) -> List[dict]:
        return list(filter(lambda row: row["tag"] == tag, data))

    @staticmethod
    def _get_unique_descriptions(data: List[dict]) -> List[str]:
        descriptions = list({row["description"] for row in data})
        descriptions.sort(reverse=True)
        return descriptions

    def _generate_lines_for_description(
        self, data: List[dict], descriptions: List[str], days_in_month: List[int]
    ) -> str:
        final_line = ""
        for description in descriptions:
            description_data = list(filter(lambda row: row["description"] == description, data))
            description_data.sort(key=lambda row: row["day"])
            description_line = ""

            for day in days_in_month:
                day_data = list(filter(lambda row: row["day"] == str(day), description_data))

                if day_data:
                    day_row = day_data[0]
                    day_value = int(day_row.get("value", 0))
                    if day_value == 1:
                        description_line += self._completed_check
                    else:
                        description_line += self._blank_check
                else:
                    description_line += self._blank_check

            description_line = f"{self._terminal.white}{description_line} {self._terminal.magenta}{description}"
            final_line += f"{description_line}\n"
        return final_line
