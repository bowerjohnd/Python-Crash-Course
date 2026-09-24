players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])

print(players[1:4])

print(players[:4])

print(players[2:])

print("-")
print(players)
print(players[-3:])

print("-")

step_slice = list(range(101))
print(step_slice)
print(step_slice[::10])         # slice by 10s: 0, 10, 20, 30, 40, 50...

print("-")

print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())
