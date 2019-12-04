import json

number = input("Please enter you favorite number: ")

filename = 'number.json'
with open(filename, 'w') as file_object:
	json.dump(number, file_object)
	print("We like the number " + str(number) + " too!")