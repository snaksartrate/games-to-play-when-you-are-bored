counter = [0, 0, 0]
valid_inputs = (0, 1, 2, 3)
index_of = {'r' : 0, 'p' : 1, 's' : 2, 'q' : 3, 'c' : 4}
move = ('p', 's', 'r')
score = 0
score_chart = ((0, 1, -1), (-1, 0, 1), (1, -1, 0)) # do score += score_chart[computer_move][player_move]
# positive score means human is winning, negative score means computer is winning

print("valid inputs are r, p, s and q")
while True:
    print(f"score = {score}")
    player_move = 'x'
    while player_move not in valid_inputs:
        player_move = index_of[input("your turn: ")]
        if (player_move == 4):
            print(f"counter = {counter}")
    if (player_move == 3):
        break
    computer_move = 'p'
    if counter[1] >= counter[0] and counter[1] >= counter[2]:
        computer_move = 's'
    elif counter[2] >= counter[0] and counter[2] >= counter[1]:
        computer_move = 'r'
    print(f"computer played \'{computer_move}\'")
    score += score_chart[index_of[computer_move]][player_move]
    counter[player_move] += 1
