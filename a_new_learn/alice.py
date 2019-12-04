def count_words(filename):
	"""Calculate how many words the file contains"""

	try:
		with open(filename) as file_object:
			contents = file_object.read()
	except FileNotFoundError:
		pass
	else:
	#Calculate how many words the file contains
		words = contents.split()
		num_words = len(words)
		print("The file " + filename + " has about " + str(num_words) + " words.")

filenames = ['pidigit.txt','alice.txt', 'guest.txt', 'pi_million_digits.txt']
for filename in filenames:
	count_words(filename)