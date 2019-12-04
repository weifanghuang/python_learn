filename = 'pi_million_digits.txt'

with open(filename) as file_object:
	lines =file_object.readlines()

pi_string = ''
for line in lines:
	pi_string += line.strip()

birthday = input("Enter your birthday, in the from mmddyy: ")
if birthday in pi_string:
	print("Your birthday appears in the first million_digits of pi!")
else:
	print("Your birthday does not appear in the first million digits of pi.")