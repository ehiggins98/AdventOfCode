n_players = 430
last_marble = 7158800
circle = [0]
current_player = 0
current_index = 0
scores = [0] * n_players

for marble in range(1, last_marble+1):
    current_player = (current_player) % n_players + 1
    if marble % 23 == 0:
        scores[current_player-1] += marble
        temp = current_index - 7 if current_index >= 7 else current_index - 7 + len(circle)
        scores[current_player-1] += circle[temp]
        current_index = temp % len(circle)
        del circle[temp]
    else:
        current_index += 2
        if current_index > len(circle): current_index = 1

        circle.insert(current_index, marble)
print(max(scores))
