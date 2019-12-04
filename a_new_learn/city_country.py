def city_country(city_name, country_name,):
	living = {'City':city_name, 'Country': country_name}
	return living

while True:
	print("\nPlease enter you living in city name: ")
	print("(If you don't want ask, please enter 'q' at any time to quit)")
	ci_name = input("city_name: ")
	if ci_name == 'q':
		break
	co_name = input("country_name: ")
	if co_name == 'q':
		break
	living = city_country(ci_name.title(),co_name.title())
	print(living)



