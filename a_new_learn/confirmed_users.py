#创建一个待验证用户的列表
unconfirmed_users = ['kim','rose','jenny']
#一个用于储存已验证用户的列表
confirmed_users =[ ]

#验证用户
while unconfirmed_users:
	current_user = unconfirmed_users.pop()#认证的用户元素等于从未认证用户中删除的元素

	print("verifying user: " + current_user.title()) #删除的元素就是正在认证的元素
	confirmed_users.append(current_user) #从未认证用户中删除的元素添加认证的用户元素

#显示所有验证的用户
print("\n The following users have been confirmed: ")
for confirmed_user in confirmed_users:
	print(confirmed_user.title())