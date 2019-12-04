def make_car(brand, type, **other):
	car ={}
	car['brand'] = brand
	car['type'] = type
	for key, value in other.items():
		car[key] = value
	return car

car = make_car('subaru','outback',
				color = 'green',
				speen = '230km',)
print(car)