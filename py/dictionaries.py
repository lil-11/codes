#using dictionaries in a for loop
player_name = input("Enter player name: ").lower()
goals = {
    "karlson": 20,
    "neville": 30,
    "shenieda": 40
}
for player in goals:
    if player == player_name:
        print(goals[player])
        break
else:
    print("No player found with that name.")