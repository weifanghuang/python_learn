my_foods = ['pizza','natto','ramen','yakitori','fried rice','fried noodles']
kim_foods = my_foods[ : ]

my_foods.append('carrot')
kim_foods.append('cabbage')

print("my favorite foods are:")
print(my_foods)

print("\nkim favorites foods are:")
print(kim_foods)

print("The first three items in the list are:")
print(my_foods[ :3])

print('The items from the middle of the list are:')
print(my_foods[2:5])

print('The last three items in the list are')
print(kim_foods[-3: ])


#Buffet Menu
Buffet_Menu = ('natto','ramen','yakitori','fried rice','fried noodles')
for food in Buffet_Menu:
	print(food)
New_Menu = ('mabo tofu','gyoza')
Buffet_New_Menu = Buffet_Menu + New_Menu
print(Buffet_New_Menu)
for new_food in Buffet_New_Menu:
	print(new_food)