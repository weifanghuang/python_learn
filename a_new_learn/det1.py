print("........I love kim........")
cars = ["audi","bmw","subaru","toyota"]
print(cars)
temp = input("You like is car")
car = int(temp)
for car in cars:
	if car =="bmw":
		print(car.upper()+ " of made in germany\n".title())
	elif car =="audi" :
		print(car.title() +" of made in germany\n".title())
	else:
		print(car.title() + " of made in japan\n".title())
print("I like car very much\n")
