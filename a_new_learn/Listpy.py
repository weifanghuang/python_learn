bicycles = ['trek','connondale','redline','specialtzend']
print(bicycles)
print(bicycles[0])
print(bicycles[0].upper())
print(bicycles[-1].upper())
message = "My first bicycle was a " + bicycles[-1].upper() +"."
print(message)
my_friends = ['Lucy','Aile','Jim','Lily','Davier','Jack']
message = "Hello " + my_friends[0]+"!"
print(message)
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
motorcycles[2] = 'nissan'
print(motorcycles)
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
motorcycles.append('nissan')
print(motorcycles[-1].upper())
car = []
car.append('nissan')
car.append('honda')
car.append('toyota')
car.append('mitsubishi')
car.append('sizuki')
print(car)
car.insert(0,'yamaha')
print(car[0].upper())
print(car)
Cheapest_car = car.pop(3)
print(car)
print(Cheapest_car.upper())
message = "Cheapest car was a " + Cheapest_car.upper()+"!"
print(message)
car = []
car.append('nissan')
car.append('honda')
car.append('toyota')
car.append('mitsubishi')
car.append('sizuki')
print(car)
car.insert(0,'yamaha')
print(car)
Too_expensive ='mitsubishi'
car.remove(Too_expensive)
print(car)
print("\nThe " + Too_expensive.title() +" car is too expensive for me")