import json
#If you previously saved user favorite number,lods it.
#Otherwise, the user is prompted to enter favorite.
filename = 'user_favorite.json'
try:
	with open(filename) as file_object:
		number = json.load(file_object)
except FileNotFoundError:
	number = input("Please enter you favorite number: ")
	with open (filename, 'w') as file_object:
		json.dump(number,file_object)
		print("We like the number " + str(number) + " too!")
else:
	print("I know your favorite number! It's " + str(number) + "!")