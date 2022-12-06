import os

current_folder = os.path.dirname(os.path.abspath(__file__))
with open(current_folder + "/input.txt", "r") as f:
    lines = f.read().splitlines()

def not_overlap(first, second):
    return first.get("high") < second.get("low") or first.get("low") > second.get("high")

overlapping = 0
for line in lines:
    split_line = line.split(",")
    first = {"low": int(split_line[0].split("-")[0]), "high": int(split_line[0].split("-")[1])}
    second = {"low": int(split_line[1].split("-")[0]), "high": int(split_line[1].split("-")[1])}
    if not not_overlap(first, second):
        overlapping += 1

print(overlapping)