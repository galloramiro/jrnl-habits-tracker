import typer

from src.service.service import JrnlHabitTrackerService


def main(name: str):
    print(f"Hello {name}")


if __name__ == "__main__":
    typer.run(main)