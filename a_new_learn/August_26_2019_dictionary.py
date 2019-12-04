#认识字典
print("\n........I love kim........")
alien_0 ={'color': 'green', 'points': 5}
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 0
print(alien_0)
#创建字典
print("\n........I love kim........")
alien_0 = { }
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)
print('The alien is ' + alien_0['color'] + '.')
alien_0['color'] = 'yellow' #把颜色下对应的值改变
print('The alien is now ' + alien_0['color'] + '.')
#改变字典中的值alien 位置
print("\n........I love kim........")
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x_position: " + str(alien_0['x_position']))
#向右移动，移动距离由速度决定
if alien_0['speed'] =='slow':
	x_increment = 1
elif alien_0['speed'] =='medium':
	x_increment = 2
else: #速度有慢-中-快三档
	x_increment = 3
#新的x轴位置等于原始位置加移动加移动距离
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x_position: " + str(alien_0['x_position']))
#删除键-值对
print("\n........I love kim........")
alien_0 = {'color': 'red','points': 5}
print(alien_0)
del alien_0['points'] #彻底删除
print(alien_0)
#多对象字典
print("\n........I love kim........")
favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	}
print("Sarah's favorite language is " +
	 favorite_languages['sarah'].title() + 
	 ".")
#联系人
print("\n........I love kim........")
private_informatation = {
	'first_name': 'huang',
	'last_name': 'weifang',
	'age': 23,
	'city': 'obihiro',
	}
print(private_informatation['first_name'])
print(private_informatation['last_name'])
print(private_informatation['age'])
print(private_informatation['city'])
#好きな番号
print("\n........I love kim........")
favorite_numbers = {
	'kim' : ['6', '8', '9'],
	'rose': ['5', '6', '9'],
	}
for name , numbers in favorite_numbers.items():
	print("\n" + name.title() + "'s favorite numbers are :")
	for number in numbers:
		print("\t" + str(number))

#遍历字典中的所有键-值对
print("\n........I love kim........")
user_0 = {
	'username': 'Hweifang',
	'first': 'huang',
	'last' : 'weifang',
	}
print(user_0.items())
for key,value in user_0.items():
	print("\nKey: " + key)
	print("Value: " + value)
#favorite languages
print("\n........I love kim........")
favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	}
for name,language in favorite_languages.items():
	print(name.title() + "'s favorite language is " +
		language.title() + '.')
friends = ['phil','sarah']
for name in sorted(favorite_languages.keys()):#按字母顺序sorted（）遍历字典中的所有键
	print(name.title())
	if name in friends:
		print(' Hi ' + name.title() + 
			', I see your favorite language is ' + favorite_languages[name].title() + '!')
	else:
		print(' Hello ' + name.title() + ' Can I make friend with you!')
#遍历字典中的所有值
print("\n........I love kim........")
favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	}
for language in set(favorite_languages.values()):#set()剔除重复的值 遍历字典中的值
	print(language.title())
# August 27 dictionary 嵌套
print("\n........I love kim........")
python_language = {
	'if':'判断',
	'for':'循環',
	'title':'頭文字大文字',
	'upper':'大文字',
	'lower':'小文字',
	}
for key, value in python_language.items():
	print(key.title() +' : '+value)
#River
print("\n........I love kim........")
river = {'huanghe':'china_shanxi','changjiang':'china_shanghai','nile':'egypt'}
for key, value in river.items():
	print('The ' + key.title() + ' runs through ' + value.title() + '.')
for key in river:
	print(key.title())
for value in river.values():
	print(value.title())
#感謝参加調査
print("\n........I love kim........")
favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	}
my_friends = ['jen','sarah','kim','rose']
for my_friend in my_friends:
	if my_friend in favorite_languages.keys():
		print(my_friend.title() + ' thank you !')
	else: 
		print(my_friend.title() + ' You are not my friend')
#6.4嵌套字典贮存在列表
print("\n........I love kim........")
alien_0 = {'color': 'yellow','points': 5}
alien_1 = {'color': 'red','points': 10}
alien_2 = {'color': 'green','points': 15}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
	print(alien)
# it have 30 aliens
print("\n........I love kim........")
alines = [ ]
for aline_number in range(0,30):
	new_alien = {'color': 'green','points': 5, 'speed':'slow'}
	aliens.append(new_alien)
for alien in aliens[0:6]:
	if alien['color'] == 'green':
		alien['color'] = 'yellow'
		alien['speed'] = 'medium'
		alien['points'] = 10
	elif alien['color'] == 'red':
		alien['color'] = 'purple'
		alien['speed'] = 'fast'
		alien['points'] = 25
for alien in aliens[0:8]:#显示前8个
	print(alien)
print('...')
#显示创建了多少👽
print("Total number of aliens: " + str(len(aliens)))
#在字典中储存列表
print("\n........I love kim........")
pizza = {
	'crust': 'thick',
	'toppings': ['mushrooms','extra cheese'],
	}
#概述所点的披萨
print("You ordered a " + pizza['crust'] + "-crust pizza" +
	"with the following toppings:")
for topping in pizza['toppings']:
	print("\t" + topping)
#一个人喜欢多种计算机语言
print("\n........I love kim........")
favorite_languages = {
	'jen': ['python','c'],
	'sarah': ['c'],
	'edward': ['ruby','jave'],
	'phil': ['python','haskell'],
	}
for name,languages in favorite_languages.items():
	if len(languages) > 1:
		print(" \n " + name.title() + "'s favorite language are : " )
		for language in languages:
			print(" \t " + language.title())
	else:
		print(name.title() + "'s favorite language is " +
		language.title() + '.')
#在字典中存储字典
#many_users.py
print("\n........I love kim........")
users = {
	'aeinstein' : {
	'first': 'albert',
	'last': 'einstein',
	'location': 'princeton',
	},
	'mcurie' : {
	'first': 'marie',
	'last':'curie',
	'location': 'paris',
	},
}
for usersname, user_info in users.items():
	print('\nUesrname: ' + usersname.title())
	full_name = user_info['first'] + " " + user_info['last']
	location = user_info['location']
	print("\tFull name: " + full_name.title())
	print("\tLocation: " + location.title())
#练习6-7
print("\n........I love kim........")
people_0 = {
	'first_name': 'huang',
	'last_name': 'weifang',
	'age': 23,
	'city': 'obihiro',
	}
people_1 = {
	'first_name': 'huang',
	'last_name': 'weihui',
	'age': 21,
	'city': "xi'an",
	}
people_2 = {
	'first_name': 'huang',
	'last_name': 'defu',
	'age': 55,
	'city':'hanzhong',
	}
peoples = [people_0,people_1,people_2]
for people in peoples:
	print(people)
#练习6-8
print("\n........I love kim........")
pig = {'owner' : 'joe','breed' : 'guinea_pig'}
dog = {'owner' : 'mark','breed' : 'huntaway'}
cat = {'owner' : 'rose','breed' : 'persian_cat'}
pets = [pig, dog, cat]
for pet in pets:
	print(pet)
#练习6-9
print("\n........I love kim........")
favorite_places = {
	'lulu' : ["xi'an","hanzhong","hokkaidao"],
	'kim' : ['london','new_york','paris'],
	'rose' : ['new_zealand','australia','italy'],
	}
for name, places in favorite_places.items():
	print("\n" + name.title() + "'s favorite_places are:")
	for place in places:
		print("\t" + place.title())
#练习6-11 city
print("\n........I love kim........")
cities = {
	'london' : {
	'country' : 'england',
	'population' : 9176530,
	'mayor' : 'Sadiq_Khan',
	},
	'paris' : {
	'country' : 'france',
	'population' : 2140526,
	'mayor' : 'Anne Hidalgo',
	},
	'new_york' : {
	'country' : 'united_states',
	'population' : 8398748,
	'mayor' : 'Bill de Blasio',
	},
}
for city, city_info in cities.items():
	print("\nCity : " + city.title())
	print("Country : " + city_info['country'])
	print("Population : " + str(city_info['population']))
	print("Mayor : " + city_info['mayor'])
#完成しました、お疲れ様です、これからもっともっと頑張りましょう