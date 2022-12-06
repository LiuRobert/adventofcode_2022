import os

current_folder = os.path.dirname(os.path.abspath(__file__))
with open(current_folder + "/input.txt", "r") as f:
    text = f.readlines()


summed_values = []
current_value = 0
for line in text:
    line = line.strip()
    if line:
        current_value += int(line)
    else:
        summed_values.append(current_value)
        current_value = 0

summed_values.sort()

print(sum(summed_values[len(summed_values) - 3:]))