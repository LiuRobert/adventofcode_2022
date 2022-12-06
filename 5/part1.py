import os

# Modified the data in this one
# Crates is the crates but just the letters on separate lines
# Moves is just the moves without the crates at the top

current_folder = os.path.dirname(os.path.abspath(__file__))
with open(current_folder + "/moves.txt", "r") as f:
    move_lines = f.read().splitlines()

with open(current_folder + "/crates.txt", "r") as f:
    crate_lines = f.read().splitlines()

crates = {}
counter = 0
for line in crate_lines:
    counter += 1
    crates[counter] = [*line]

for line in move_lines:
    words = line.split(" ")
    ammount = int(words[1])
    from_pile = int(words[3])
    to_pile = int(words[5])
    crates[to_pile].extend(reversed(crates[from_pile][-ammount:]))
    crates[from_pile] = crates[from_pile][:-ammount]

tops = ""
for key, values in crates.items():
    tops += values[-1:][0]

print(tops)
