import os

current_folder = os.path.dirname(os.path.abspath(__file__))
with open(current_folder + "/input.txt", "r") as f:
    text = f.read().strip()

def check(text, start_index, end_index):
    if start_index == end_index:
        return True
    char = text[start_index]
    for i in range(start_index + 1, end_index):
        if char == text[i]:
            return False
    return check(text, start_index + 1, end_index)


marker_index = None
for i in range(4, len(text)):
    if check(text, i - 4, i):
        marker_index = i
        break

print(marker_index)