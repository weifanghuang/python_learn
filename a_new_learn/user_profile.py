from profile_function import build_profile

first = input("Please enter your first name: ")
last = input("Please enter your last name: ")

user_info ={}
#设置一个标志，判断用户是否愿意输入信息
message =input("May I know more about your? " + 
		"\n(If you want to quit, please enter 'q'): ")
if message != "q":
	active = True
	while active:
		age = input("May I know your age? " + 
			"\n(If you want to quit, please enter 'q'): ")
		if age =='q':
			break
		else:
			user_info[age] = age
		hobby = input("May I know your hobby? " + 
			"\n(If you want to quit, please enter 'q'): ")
		if hobby =='q':
			break
		else:
			user_info[hobby] = hobby
		other = input("Any other you want tell me? (yes/no)")
		if other =='no':
			active = False

	


user_profile = build_profile(first,last,**user_info)
print(user_profile)