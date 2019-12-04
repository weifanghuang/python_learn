def make_pizza(size,*toppings):
	#*让python创建一个名为toppongs的空元组，将收到的值全部装到元组中
	"""打印顾客需要的所有配料"""
	print("\nMaking a " + size + " pizza with the following toppings:")
	for topping in toppings:
		print("-" + topping)

