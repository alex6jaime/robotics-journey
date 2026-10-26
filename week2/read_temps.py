import csv
from pathlib import Path

file = Path(__file__).parent / "temperature.csv"

try:
    temperatures = []
        
    with open(file, "r", newline="") as f:
        reader = csv.DictReader(f)

        for row in reader:
            temperatures.append(float(row["temp_c"]))

    if not temperatures:
        raise ValueError("No temperature data found.")

    average_temp = sum(temperatures) / len(temperatures)

    print(f"Average temperature: {average_temp:.2f} °C")

except FileNotFoundError:
    print(f"File {file} not found.")

except (ValueError, KeyError) as error:
    print(f"Error reading temperatures: {error}")