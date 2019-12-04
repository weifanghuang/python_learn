import kim

print("Give me two number, and I will add them")
print("Enter 'q' to quit")

while True:
	first_number = input("\nfirst number: ")
	if first_number == 'q':
		break
	second_number = input("\nsecond number :")
	if second_number == 'q':
		break
	try:
		answer = int(first_number) + int(second_number)
	except ValueError:
		print("Please enter number")
	else:
		print(answer)
