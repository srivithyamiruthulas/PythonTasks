leaderboard = [("Player1", 500), ("Player2", 450), ("Player1", 600)]

players = [p for p, s in leaderboard]
is_valid = len(players) == len(set(players))

sorted_leaderboard = sorted(leaderboard, key=lambda x: x[1], reverse=True)

print(is_valid)
print(sorted_leaderboard)
