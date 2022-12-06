import os

current_folder = os.path.dirname(os.path.abspath(__file__))
with open(current_folder + "/input.txt", "r") as f:
    lines = f.read().splitlines()

priorities = 0
for line in lines:
    first_compartment = line[:int(len(line)/2)]
    second_compartment = line[int(len(line)/2):]
    duplicates = []
    for c in first_compartment:
        if c in second_compartment and not c in duplicates:
            duplicates.append(c)
    for c in duplicates:
        if ord(c) > 90:
            priorities += ord(c) - 96
        else:
            priorities += ord(c) - 38

print(priorities)
print(3 % 3)