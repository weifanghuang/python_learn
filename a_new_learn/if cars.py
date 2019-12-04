#只执行一个代码块
print("........I love kim........")
cars = ["audi","bmw","subaru","toyota"]
for car in cars:
	if car =="bmw":
		print(car.upper()+ " of made in germany\n".title())
		break
	elif car =="audi" :
		print(car.title() +" of made in germany\n".title())
	else:
		print(car.title() + " of made in japan\n".title())
print("I like car very much\n")

#voting.py
print("\n........I love kim........")
age = 17
if age >= 18:
	print('You are old enough to votel!')
	print('Have you registered to vote yet?\n')
else:
	print('Sorry, you are too young to vote!')
	print('Please register to vote as sonn as you turn 18 years old!\n')
#amusement.py
print("\n........I love kim........")
age = 68
if age < 4:
	price = 0
elif age < 18 or age >=65:
	price = 5
elif age < 65:
	price = 10
print("Your admission cost $" + str(price)+".\n")
#toppings.py
print("\n........I love kim........")
requested_toppings = ['mushrooms','green peppers','extra cheese']
for requested_topping in requested_toppings:
	if requested_topping == 'green peppers':
		print('Sorry, we are out of green peppers right now.')
	else:
		print('Adding '+ requested_topping + '.' )
print("\nFinished making your pizza!")
#列表为空时
print("\n........I love kim........")
requested_toppings = []
if requested_toppings:
	for requested_topping in requested_toppings:
		print('Adding'+ requested_topping + '.' )
	print("\nFinished making your pizza!")
else:
		print('Are you sure you want a plain pizza?')
#多列表
print("\n........I love kim........")
available_toppings = ['mushrooms','olives','green peppers'
					  'pepperoni','pineapple','extra cheese']
requested_toppings = ['mushrooms','french fries','extra cheese']
for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print('Adding '+ requested_topping + '.' )   
	else:
		print("Sorry we don't have "+ requested_topping + '.')                  
print("\nFinished making your pizza!")
#用户名问候
print("\n........I love kim........")
user_names = ['kim','lily','jack','mark','admin']
if user_names:
	for user_name in user_names:
		if user_name == 'admin':
			print("Hello admin, would you like to see a status report? ")
		else: 
			print("Hello " + user_name.title() + ' thank you for logging in again')
else:
	print('We need to find some users')
#唯一無二のユーザー
print("\n........I love kim........")
current_users = ['kim','Lily','jack','mark','admin']
current_users = [s.lower() for s in current_users]
new_users = ['Kim','lily','Eric','Joe','Alice']
for new_users in new_users:
	if new_users.lower() in current_users:
		print(new_users + ' Username is already in using,Please enter other username')
	else:
		print(new_users +' Username is not being used you can use')
#順番数
print("\n........I love kim........")
ordinal_number = list(range(1,10))
for ordinal_number in ordinal_number:
	if ordinal_number > 3:
		print(str(ordinal_number) + 'th')
	elif ordinal_number == 1:
		print(str(ordinal_number) + 'st')
	elif ordinal_number == 2:
		print(str(ordinal_number) + 'nd')
	else:
		print(str(ordinal_number) + 'rd')
















