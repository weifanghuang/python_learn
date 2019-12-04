def build_profile(first, last, **user_info):
	"""创建一个字典，其中包含我们知道的用户信息"""
	profile = {}
	#创建一个空字典用于存储用户信息
	profile['first_name'] = first
	profile['last_name'] = last
	#遍历字典user_info的所有键值对，
	#注意items（）不能忘记
	for key, value in user_info.items():
		#将所有键值对加入profile{}的字典中
		profile[key] = value
	return profile
	
