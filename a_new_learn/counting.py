current_number = input("please enter your favorite number: ")
current_number = int(current_number)
while current_number <= 10:
	current_number += 1
	if current_number % 2 ==0:
		continue

	print(current_number)