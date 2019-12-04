from Car import Car
from electric_car import ElectricCar 
from Restaurant import Restaurant
from User import Admin

my_beetle = Car('volkswagen','beetle',2019)
print("\n" + my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster',2020)
print("\n" + my_tesla.get_descriptive_name())

my_restaurant = Restaurant("pizza hut", "pizza")
my_restaurant.describe_restaurant()


eric = Admin('eric', 'matthes', 'e_matthes', '29', 'alaska')
eric.describe_user()
eric.greet_user()
eric.privileges.show_privieges()