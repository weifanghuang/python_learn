toppings = "\nPlease enter your ordered pizza topping."
toppings +="\n(Enter'quit' when you are finished "
active = True
while active:
	topping = input(toppings)
	
	if topping == 'quit':
		print("\nFinished making your pizza!")
		break
	else:
		print("Adding " + topping + ".")