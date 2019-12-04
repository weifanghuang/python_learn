# A simple database

# A dictionary that uses a people's name as a key, and everyone uses a dictionary. The dictionary contains the keys
# 'phone' and 'adar', which are associated whit phone numbers and addresses, respectively

people ={
    'Alice':{
        'phone':'2345',
        'addr': 'Foo drive 23'
    },
    'Beth':{
        'phone':'12345',
        'addr':'Bar street 42'
    },
    'Cecil':{
        'phone':'2998',
        'addr':'baz avenue 90'
    }
}

# Phone number and addresses labels
labels = {
    'phone':'phone number',
    'addr':'address'
}

name = input('Name: ')

# Want phone number or address
request = input('Phone number(p) or address(a)?')

# use the key
if request =='p':
    key = 'phone'
if request =='a':
    key = 'addr'

# print information
if name in people:
    print("{}'s {} is {}.".format(name, labels[key],people[name][key]))
else:
    print('Not found')
