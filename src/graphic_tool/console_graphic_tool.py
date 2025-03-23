from calendar import weekday, monthrange
from datetime import datetime
from blessings import Terminal


class ConsoleGraphicTool:
    # https://www.nerdfonts.com/cheat-sheet
    _blank_check = ""  # 󰄱 
    _completed_check = ""  # 󰡖 󰄯 󰄮 
    _sleep = "  "
    _humor = "  "
    _stress = "  "
    _terminal = Terminal()

    def generate_positive_habits_graph(self) -> str:
        raise NotImplementedError

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
            letters_days_line += f"{letter_weekday}  "

        color_number_days_line = f"{self._terminal.magenta}{number_days_line}"
        color_letters_days_line = f"{self._terminal.magenta}{letters_days_line}"
        complete_color_line = f"{color_number_days_line}\n{color_letters_days_line}"

        return complete_color_line
