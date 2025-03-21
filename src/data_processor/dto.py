from dataclasses import dataclass


@dataclass
class MonthlyTitleRow:
    date: str
    title: str
    week_number: int
    weekday_number: int
    month: int
    year: int
    time: str


@dataclass
class MonthlyHabitsRow:
    date: str
    year: int
    month: int
    day: int
    week_number: int
    description: str
    value: int
    tag: str
