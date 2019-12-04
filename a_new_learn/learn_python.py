pro = 'programming.txt'
with open(pro) as file_object:
	lines = file_object.readlines()

message =''	
for line in lines:
	message += line.rstrip()
	
print(message.replace('love', 'hate'))