import os

current_folder = os.path.dirname(os.path.abspath(__file__))
with open(current_folder + "/input.txt", "r") as f:
    text = f.readlines()


largest_value = 0
current_value = 0
for line in text:
    line = line.strip()
    if line:
        current_value += int(line)
    else:
        if current_value > largest_value:
            largest_value = current_value
        current_value = 0

print(largest_value)
