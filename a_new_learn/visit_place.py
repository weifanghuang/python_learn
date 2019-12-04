visit_places = { }
active = True
while active:
	user = input("\n what your name? ")
	place = input(" where are you want go? ")
	visit_places[user] = place
	live = input("Are you like live in home? (yes / no)")
	if live == 'yes':
		active = False
print("\n ---Results---")
for user, place in visit_places.items():
	print(user + " want go to " + place + ".")