import kim
from collections import OrderedDict

cities = OrderedDict()

cities ['london'] = {'country' : 'england',
					'population' : 9176530,
					'mayor' : 'Sadiq Khan',
					}
cities['paris'] = {'country' : 'france',
					'population' : 2140526,
					'mayor' : 'Anne Hidalgo',
					}
cities['new_york'] = {'country' : 'united_states',
					'population' : 8398748,
					'mayor' : 'Bill de Blasio',
					}

for city, city_info in cities.items():
	print("\nCity : " + city.title())
	print("Country : " + city_info['country'].title())
	print("Population : " + str(city_info['population']))
	print("Mayor : " + city_info['mayor'].title())
