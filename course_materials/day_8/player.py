import numpy as np
import sounddevice as sd
import sys
import time
import csv

files = ["anscombes_I.csv", "anscombes_II.csv", "anscombes_III.csv", "anscombes_IV.csv"]


def map_range(value, fromLow, fromHigh, toLow, toHigh):
    # Ensure the input value is within the current range
    value = max(fromLow, min(fromHigh, value))

    # Map the value to the target range
    mapped_value = (value - fromLow) * (toHigh - toLow) / (fromHigh - fromLow) + toLow

    return mapped_value


def play_tone(frequency, duration_sec):
    sample_rate = 44100  # You can adjust the sample rate as needed

    t = np.linspace(0, duration_sec, int(sample_rate * duration_sec), endpoint=False)
    tone = 0.5 * np.sin(2 * np.pi * frequency * t)

    sd.play(tone, sample_rate)
    sd.wait()


for index, filename in enumerate(files):
    # opening the CSV file
    with open(filename, mode="r") as file:
        # reading the CSV file
        csvFile = csv.reader(file)

        # Setting contents to a list
        xs = []
        ys = []
        lines = []
        i = 0
        for line in csvFile:
            lines.append(line)
            if i > 0:
                xs.append(float(line[1]))
                ys.append(float(line[2]))
            i += 1
        for k in range(1, len(xs)):
            tone = map_range(xs[k], 1, 20, 280, 900)
            duration = map_range(ys[k], 1, 20, 0.2, 2)
            play_tone(tone, duration / 2)
        time.sleep(1)
        print("next")
