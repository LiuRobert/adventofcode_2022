import os

def translate(my_move):
    if my_move == 'X':
        return 'A'
    elif my_move == 'Y':
        return 'B'
    elif my_move == 'Z':
        return 'C'

current_folder = os.path.dirname(os.path.abspath(__file__))
with open(current_folder + "/input.txt", "r") as f:
    lines = f.read().splitlines()

# Rock = A
# Paper = B
# Scissors = C

total_points = 0
for line in lines:
    points = 0
    opponent_move = line.split(" ")[0]
    my_move = translate(line.split(" ")[1])
    if my_move == 'A':
        points += 1
    elif my_move == 'B':
        points += 2
    elif my_move == 'C':
        points += 3
    if opponent_move == my_move:
        points += 3
    elif my_move == 'A' and opponent_move == 'C' or my_move == 'B' and opponent_move == 'A' or my_move == 'C' and opponent_move == 'B':
        points += 6
    total_points += points

print(total_points)