my_friends = ['Lucy','Aile','Jim','Lily','Davier','Jack']
print(my_friends)
message ="Can you have dinner with me? "+ my_friends[2]
print(message)
not_attending = 'Jim'
print("Jim can not attending")
my_friends.remove(not_attending)
print("Wecome my new friend Masa")
my_friends.append('Mase')#Jim can not attending masa can attending
my_famlies = ["father","mather","sister"]
my_friends = my_famlies + my_friends
print("my famlies want meet my friends")
print(my_friends)
for friend in my_friends:
	print(friend.title() +" Friday night Can you have dinner in Michelin Restaurant with me?  " + str(len(my_friends) + 1) + " people will together! ")
	print("I will wait for you, " + friend.title()+ ".\n")
for friend in my_friends:
	print("Sorry, "+friend.title() + " the Restaurant cannot accommodate many people at once.so I will two people")

