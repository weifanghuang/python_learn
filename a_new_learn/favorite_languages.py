import kim
from collections import OrderedDict

favorite_languages = OrderedDict()

favorite_languages['jen'] = ['python','c']
favorite_languages['sarah'] = ['c']
favorite_languages['edward'] = ['ruby','jave']
favorite_languages['phil'] = ['python','haskell'],

for name,languages in favorite_languages.items():
	if len(languages) > 1:
		print("\n" + name.title() + "'s favorite language are : " )
		for language in languages:
			print(" \t " + language.title())
	else:
		print(name.title() + "'s favorite language is " +
		language.title() + '.')

