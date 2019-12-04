def show_magicans(magicians_name):
	"""I will show magiceans name"""
	for magician_name in magicians_name:
		print(magician_name.title())

def make_great(magicians_name,):
	#对原列表进行遍历
	while magicians_name:
		make_great = "the Great " + magicians_name.pop()
		
		Make_great.append(make_great)
	return Make_great
magicians_name = ['jimi','jock', 'alsai']
Make_great =[]

show_magicans(magicians_name)
make_great(magicians_name[:])
print(magicians_name)
print(Make_great)