def greet_user(names):
	"""问候列表的用户"""
	for name in names:
		msg = "Hello, " + name.title() + "!"
		print(msg)

username = ['hannah', 'ty' ,'margot']
greet_user(username)