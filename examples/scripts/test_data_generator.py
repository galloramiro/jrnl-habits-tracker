import os
import random
from datetime import datetime, timedelta

# Note: This code was generated with the assistance of AI.


def generate_timestamp(start_time, end_time, last_time=None):
    if last_time is None:
        random_time = start_time + (end_time - start_time) * random.random()
    else:
        increment = timedelta(minutes=random.randint(1, 15))
        random_time = last_time + increment
        if random_time > end_time:
            random_time = end_time
    return random_time


def get_day_name(date):
    days = ["LUNES", "MARTES", "MIÉRCOLES", "JUEVES", "VIERNES", "SÁBADO", "DOMINGO"]
    day_index = datetime.strptime(date, "%Y-%m-%d").weekday()
    return days[day_index]


def weighted_choice(choices):
    total = sum(weight for choice, weight in choices)
    r = random.uniform(0, total)
    upto = 0
    for choice, weight in choices:
        if upto + weight >= r:
            return choice
        upto += weight
    assert False, "Shouldn't get here"


def generate_data(month, day):
    date = f"2025-{month:02d}-{day:02d}"
    day_name = get_day_name(date)
    start_time = datetime.strptime(f"{date} 20:00:00", "%Y-%m-%d %H:%M:%S")
    end_time = datetime.strptime(f"{date} 23:55:00", "%Y-%m-%d %H:%M:%S")
    last_time = None

    data = f"[{generate_timestamp(start_time, end_time).strftime('%Y-%m-%d %I:%M:%S %p')}] |\n"
    data += f"## {day_name}\n\n"
    data += "@Health\n"
    data += f"Sueño: {weighted_choice([(6, 1), (7, 3), (8, 3), (9, 1)])}\n"
    data += f"Humor: {weighted_choice([(5, 1), (6, 4), (7, 2), (8, 1)])}\n"
    data += f"Estres: {weighted_choice([(1, 5), (2, 3), (3, 1), (4, 1)])}\n\n"

    data += "@PositiveHabits\n"
    for i in range(1, 8):
        value = 0 if random.random() < 0.25 else 1
        data += f"- positive_habit_{i:02d}: {value}\n"
    data += "\n"

    data += "@NegativeHabits\n"
    for i in range(1, 5):
        value = 1 if random.random() < 0.05 else 0
        data += f"- negative_habit_{i:02d}: {value}\n"
    data += "\n"

    data += "@ConvictConditioning\n"
    exercises = [
        "Saludo al Sol",
        "Full Pullups",
        "Unevein Squats",
        "Close Pushups",
        "Straigt Leg Raises",
        "Handstand Pushups",
        "Straignt Bridges",
    ]
    day_exercises = {
        "LUNES": ["Saludo al Sol", "Full Pullups", "Unevein Squats"],
        "MARTES": [],
        "MIÉRCOLES": ["Saludo al Sol", "Close Pushups", "Straigt Leg Raises"],
        "JUEVES": [],
        "VIERNES": ["Saludo al Sol", "Handstand Pushups", "Straignt Bridges"],
        "SÁBADO": [],
        "DOMINGO": [],
    }
    for exercise in exercises:
        if exercise in day_exercises.get(day_name, []):
            if exercise == "Saludo al Sol":
                data += f"- {exercise}: 5\n"
            else:
                data += f"- {exercise}: {random.randint(10, 60)}\n"
        else:
            data += f"- {exercise}: 0\n"
    data += "\n"

    data += "@DailyTasks\n"
    data += "### GENERAL\n"
    num_tasks = random.randint(1, 5)
    for i in range(1, num_tasks + 1):
        data += f"- Task {i:02d}\n"
    data += "\n"

    data += "### MENSAJES\n"
    data += "- Task 01\n\n"

    data += "### TRABAJO\n"
    for i in range(1, 3):
        data += f"- Task {i:02d}\n"
    data += "\n"

    data += "### PSICÓLOGA\n"
    for i in range(1, 3):
        data += f"- Task 0\n"
    data += "\n"

    data += "@Journaling\n\n"

    num_entries = random.randint(5, 10)
    for i in range(1, num_entries + 1):
        last_time = generate_timestamp(start_time, end_time, last_time)
        data += f"[{last_time.strftime('%Y-%m-%d %I:%M:%S %p')}] |\n"
        data += f"### {date} Title {i:02d}\n"
        data += "Lorem ipsum\n\n"

    return data


# Generate data for the specified day and save to file
month = 6
for day in range(1, 31):
    data = generate_data(month, day)
    dir_path = f"./examples/jrnl-dir/2025/{month:02d}"
    os.makedirs(dir_path, exist_ok=True)
    file_path = os.path.join(dir_path, f"{day:02d}.txt")
    with open(file_path, "w") as file:
        file.write(data)
