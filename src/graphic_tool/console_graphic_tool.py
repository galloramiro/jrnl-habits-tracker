class ConsoleGraphicTool:
    # https://www.nerdfonts.com/cheat-sheet
    _blank_check = ""  # 󰄱 
    _completed_check = ""  # 󰡖 󰄯 󰄮 
    _sleep = "  "
    _humor = "  "
    _stress = "  "

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

    def _generate_days_line(self) -> str:
        raise NotImplementedError
