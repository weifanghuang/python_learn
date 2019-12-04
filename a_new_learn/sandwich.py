sandwich_orders = ["1","5","2","3","5","8","5"]
print("'5' is sell out")
while '5' in sandwich_orders:
	sandwich_orders.remove('5')
print(sandwich_orders)
finished_sandwiches = []
while sandwich_orders:
	finished_sandwich = sandwich_orders.pop()
	print("I made your tuna sandwich " + finished_sandwich)
	finished_sandwiches.append(finished_sandwich)
print("Today made sandwich: ")
for finished_sandwich in finished_sandwiches:
	print(finished_sandwich)


