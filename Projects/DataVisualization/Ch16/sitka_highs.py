from pathlib import Path
import csv

import matplotlib.pyplot as plt

# csv file names are not correct (from book examples download)
path = Path('csv_weather_data/sitka_weather_2021_full.csv')     # July 2021
lines = path.read_text(encoding='utf-8').splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# Show headers index and string
for index, column_header in enumerate(header_row):
    print(index, column_header)

# Extract high tempertures
highs = []
for row in reader:
    high = row[4]
    highs.append(high)

print(len(highs))

# Plot the high temperatures.
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(highs, color='red')

# Format plot
ax.set_title("Daily High Temperatures, July 2021", fontsize=24)
ax.set_xlabel('', fontsize=16)
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()
