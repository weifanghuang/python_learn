import kim
def count_words(filename):
	"""Open the file"""

	try:
		with open(filename) as file_object:
			contens = file_object.read()
	except FileNotFoundError:
		pass
	else:
		print("\n" + filename + contens.title())


filenames = ['cats_name.txt', 'dog_name.txt']
for filename in filenames:
	count_words(filename)