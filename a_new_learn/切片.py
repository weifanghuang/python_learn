players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[2:4])
print(players[:3])
print(players[1:])
print(players[-3:])
print("Here are the first three players in my team")
for player in players[:3]:
    print(player.title())
apple = [2, 4, 1, 5, 8]
apple.sort()
print(apple)
print(sorted(apple, reverse=True))

print(players * 3)
