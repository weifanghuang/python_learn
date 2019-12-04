prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "
active = True#message = " "#首次循环可检查message！=‘quit’
while active:#message != 'quit':#当message不等于quit是运行while 循环
	message = input(prompt)
	if message == 'quit' or message =="Q":#当message不等于quit时才输出message 
		active = False
	else:
		print(message)
