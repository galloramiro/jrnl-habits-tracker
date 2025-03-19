from dataclasses import dataclass


class MonthlyTitleRow(dataclass):
    date: str
    title: str
    week_number: int
    weekday_number: int
    month: int
    year: int
    time: str


class MonthlyHabitsRow(dataclass):
    date: str
    year: int
    month: int
    day: int
    week_number: int
    description: str
    value: int
    tag: str
