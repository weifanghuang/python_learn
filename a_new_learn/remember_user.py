import json

def get_stored_username():
	"""If you previously saved username,lods it."""
	filename = 'username.json'
	try:
		with open (filename) as file_object:
			username =json.load(file_object)
	except FileNotFoundError:
		return None
	else:
		return username

def get_new_username():
	"""The user is prompted to enter a username."""
	username = input("What is your name? ")
	filename = 'username.json'
	with open(filename, 'w') as file_object:
		json.dump(username,file_object)
	return username
def greet_user():
	"""Otherwise, the user is prompted to enter a username."""
	username = get_stored_username()
	name = input("Are you " + username.title() + "?(yes/no)")
	if name == 'yes':
		print("Welcome back, " + username.title() + "!")
	else:
		username = get_new_username()
		print("We will remember you when you come back, " + username.title() + "!")
		

greet_user()