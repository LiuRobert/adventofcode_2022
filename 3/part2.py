import os

current_folder = os.path.dirname(os.path.abspath(__file__))
with open(current_folder + "/input.txt", "r") as f:
    lines = f.read().splitlines()

def to_priority(c):
    if ord(c) > 90:
        return ord(c) - 96
    else:
        return ord(c) - 38

counter = 0
priorities = 0
last_two_lines = []
for line in lines:
    counter += 1
    if counter % 3 != 0:
        last_two_lines.append(line)
    else:
        for c in line:
            if c in last_two_lines[0] and c in last_two_lines[1]:
                priorities += to_priority(c)
                break
        last_two_lines = []

print(priorities)