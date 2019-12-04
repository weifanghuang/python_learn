import kim
filename = 'guest.txt'
with open(filename,'w') as file_object:
	active = True
	while active:
		name = input(
			"Enter you name:"
			"\n(if you wantn't tell please enter 'quit')")
		if name == 'quit':
			active = False
		else:
			like_language = input(
			"Can you tell me what programming language do you like : "
			"\n(if you wantn't tell please enter 'quit')")
			if like_language == 'quit':
				active = False
			else:
				print("Holle " + name.title() + " welcome to my python world")
				print("I also like " + like_language.title() + " language!")

				file_object.write(name.title() +
					" like the " +
					like_language.title() +
					 " programming language!\n")
