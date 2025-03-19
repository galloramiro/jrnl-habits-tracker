from src.client.local_client import LocalClient
from src.data_processor.data_processor import DataProcessor
from src.graphic_tool.console_graphic_tool import ConsoleGraphicTool
from src.repository.csv_repository import CsvRepository


class JrnlHabitTrackerService:

    def __init__(
        self,
        client: LocalClient,
        data_processor: DataProcessor,
        repository: CsvRepository,
        graphic_tool: ConsoleGraphicTool,
    ):
        self._client = client
        self._data_processor = data_processor
        self._repository = repository
        self._graphic_tool = graphic_tool

    def generate_monthly_habits_and_titles_data_by_month(self):
        raise NotImplementedError

    def show_full_habits_and_health_charts(self):
        raise NotImplementedError

    def show_titles_by_day(self):
        raise NotImplementedError

    def show_titles_by_week(self):
        raise NotImplementedError

    def show_titles_by_month(self):
        raise NotImplementedError

    @staticmethod
    def build_local_console_service():
        return JrnlHabitTrackerService(LocalClient(), DataProcessor(), CsvRepository(), ConsoleGraphicTool())
