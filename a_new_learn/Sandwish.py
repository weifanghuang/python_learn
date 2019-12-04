def make_sandwish(*toppings):
	"""sandwish topping"""
	print("\nmaking a sandwish with the following toppings: ")
	for topping in toppings:
		print("\t" +topping.title())

make_sandwish("lettuce", "tomato", "cucumber")
make_sandwish("lettuce", "tomato", "green peppers")
make_sandwish('egg', 'cucumber', 'onion')