print("\n........I love kim........")
favorite_numbers = {
	'kim': ['6', '8', '9'],
	'rose': ['5', '6', '9'],
	}
for name, numbers in favorite_numbers.items():
	print("\n" + name.title() + "'s favorite numbers are :")
	for number in numbers:
		print("\t" + str(number))
