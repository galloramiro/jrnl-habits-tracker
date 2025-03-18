import logging
import os
import sys

import pandas as pd
from uniplot import plot


LOGGER = logging.getLogger("MonthlyViewsLogger")
logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)

# TODO: create enum or config file with habits names


class MonthlyViews:
    # https://www.nerdfonts.com/cheat-sheet
    _blank_check = "" # 󰄱 
    _completed_check = "" # 󰡖 󰄯 󰄮 

    def show_all_graphs(self, month: str):
        self._generate_health_view(month=month)
        self._generate_days_line()
        self._generate_view_by_habit_and_month(habit="PositiveHabits", month=month)
        self._generate_days_line()
        self._generate_view_by_habit_and_month(habit="NegativeHabits", month= month)

    def _generate_view_by_habit_and_month(self, habit: str, month: str):
        dataframe = self._get_dataframe(month=month)
        dataframe = self._filter_dataframe_by_tag(dataframe=dataframe, tag=habit)
        descriptions = list(dataframe["description"].unique())

        for description in descriptions:
            description_dataframe = dataframe[dataframe["description"] == description]
            self._generate_habits_line(dataframe=description_dataframe)

    def _generate_health_view(self, month: str):
        dataframe = self._get_dataframe(month=month)
        dataframe = self._filter_dataframe_by_tag(dataframe=dataframe, tag="Health")        
        values = list(dataframe["value"].unique())
        values.sort(reverse=True)
    
        if 0 in values:
            cero_index = values.index(0.0)
            values.pop(cero_index)

        symbols = {
            "Sueño": "  ",
            "Humor": "  ",
            "Estres": "  ",
        } 
        print(f"\nSueño: {symbols['Sueño']}    Humor: {symbols['Humor']}    Estres: {symbols['Estres']}\n")
        
        for value in values:
            value_dataframe = dataframe[dataframe["value"] == value]
            self._generate_health_line(dataframe=value_dataframe)

    def _get_dataframe(self, month: str) -> pd.DataFrame:
        JRNL_PATH = "./examples/jrnl-dir/"
        FILE_NAME = "monthly_habits_data.csv"
        month_file_path = os.path.abspath(f"{JRNL_PATH}2025/{month}/{FILE_NAME}")
        dataframe = pd.read_csv(month_file_path)
        return dataframe

    def _filter_dataframe_by_tag(self, dataframe: pd.DataFrame, tag: str) -> pd.DataFrame:
        return dataframe[dataframe["tag"] == tag]

    def _remove_rows_with_0_on_value(self, dataframe: pd.DataFrame) -> pd.DataFrame:
        return dataframe[dataframe["value"] != 0.0]

    def _generate_habits_line(self, dataframe: pd.DataFrame) -> str:
        # TODO: make this more inteligent and check the numbers of days for the month
        description_line = ""
        for day in range(1, 32):
            record = dataframe[dataframe["day"] == day]
            if record.empty:
                description_line += f" {self._blank_check} "
            elif record.iloc[0]["value"] == 0.0:
                description_line += f" {self._blank_check} "
            else:
                description_line += f" {self._completed_check} "

        description = str(dataframe.iloc[0]["description"])
        description_line += f" {description}"
        print(description_line)
        return description_line

    def _generate_health_line(self, dataframe: pd.DataFrame) -> str:
        # TODO: make this more inteligent and check the numbers of days for the month
        symbols = {
            "Sueño": "  ",
            "Humor": "  ",
            "Estres": "  ",
        } 
        value_line = ""
        for day in range(1, 32):
            record = dataframe[dataframe["day"] == day]
            if record.empty:
                value_line += f" {self._blank_check} "
            elif record.iloc[0]["value"] == 0.0:
                value_line += f" {self._blank_check} "
            else:
                value_line += symbols[record.iloc[0]["description"]]

        value = str(dataframe.iloc[0]["value"])
        value_line += f" {value}"
        print(value_line)
        return value_line

    def _generate_days_line(self):
        # TODO: make this more inteligent and check the numbers of days for the month
        days_line = ""
        for day in range(1, 32):
            if len(str(day)) == 1:
                days_line += f" 0{day}"
            else:
                days_line += f" {day}"
        print(f"\n{days_line}\n")


if __name__ == "__main__":
    print("Hello!\nEnter the month that you wanna see ")
    month_number = input()
    if len(month_number) == 1:
        month_number = f"0{month_number}"

    graphs = MonthlyViews()
    graphs.show_all_graphs(month=month_number)
