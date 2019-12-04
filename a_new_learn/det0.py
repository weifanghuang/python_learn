print("\n........I love kim........")
temp = input('Please enter your years: ')
age = int(temp)
if age < 2:
	print('You are a baby')
elif age < 4 and age >=2:
	print('You are learning to walk')
elif age < 13 and age >= 4:
	print('You are a child')
elif age < 20 and age >= 13:
	print('You are a teenager')
elif age <65 and age >= 20:
	print('You are a adult')
elif age >=65:
	print('You are a old man')
