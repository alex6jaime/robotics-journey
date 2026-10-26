from pathlib import Path
import logging


#---------Understanding file paths and directories---------
print(Path.cwd())    # Current working directory
print(Path.home())   # Your Ubuntu home directory

file = Path("week2") / "data.csv"

print(file.name)      # data.csv
print(file.suffix)    # .csv
print(file.parent)    # week2
print(file.exists())  # True if the file exists

#-----Reading and writing files-----

file = Path(__file__).parent / "motor_log.txt"

# Create or overwrite a file
#with open(file, "w", encoding="utf-8") as f:
#    f.write("Motor 1: 100 RPM\n")

# Add another reading
#with open(file, "a", encoding="utf-8") as f:
#    f.write("Motor 2: 150 RPM\n")

# Read the contents
with open(file, "r", encoding="utf-8") as f:
    data = f.read()

print(data)

#--------------Creating folders and listing files--------------
folder = Path(__file__).parent / "sensor_data"

#folder.mkdir(exist_ok=True)

#(folder / "reading1.txt").write_text("Temperature: 25")
#(folder / "reading2.txt").write_text("Temperature: 27")

for file in folder.glob("*.txt"):
    print(file.name)

#------------Understanding exceptions and assertions------------

def calculate_speed(distance, time):
    if time <= 0:
        raise ValueError("Time must be positive")

    return distance / time


try:
    speed = calculate_speed(10, 0)
    print(speed)

except ValueError as error:
    print("Calculation failed:", error)

#----------

def counts_to_degrees(counts, counts_per_rev):
    return counts / counts_per_rev * 360


angle = counts_to_degrees(330, 1320)

assert angle == 90, "Encoder calculation is incorrect"

print("Test passed!")

#-----------Understanding logging-----------

logging.basicConfig(
    level=logging.DEBUG,
    format="%(levelname)s: %(message)s"
)

motor_speed = 75

logging.debug(f"Motor speed = {motor_speed}")
logging.info("Motor started")

if motor_speed > 70:
    logging.warning("Motor speed is high")