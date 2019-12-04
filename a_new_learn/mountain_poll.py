responses = { }
polling_active = True

while polling_active:
	name = input("\n What is your name? ")
	response = input("Which mountain would you like to climb someday? ")
	mountain = input("What the mountain's name? ")

	responses[name] = [response , mountain]

	repeat = input("Would you like to let another person respond? (yes / no) ")
	if repeat =='no':
		polling_active = False

print("\n ---Poll Results---")
for name, response in responses.items():
	print(name + " Would like to climb " + str(response) + ".")
print(responses)