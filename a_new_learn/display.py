def display_message(author,title = 'python'):
	print("\nI am learning in " + title.title() + ' by '+ author.title() + '!')

display_message('kim')

def make_shirt(size = 'XL',pattern ='I love python'):
	print("\nMy size is " + size +' and I want  make a shirt with ' + pattern + ' pattern!')
make_shirt()
make_shirt("L")
make_shirt(pattern = 'China')
def describe_city(city,Country = "China"):
	print("\n" + city.title() + " is in " + Country.title())
describe_city('london','england')
describe_city('Beijing')
describe_city("Shanghai")
describe_city('paris','france')