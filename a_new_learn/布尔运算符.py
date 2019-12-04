# Check username and PIN
database = [
    ['albert', '1234'],
    ['dilbert', '5678'],
    ['smith', '7766'],
    ['jones', '9999']
]

username = input('User name:')
pin = input("PIN code: ")
if [username, pin] in database:
    print('Access granted')
else:
    print('You name apply for a new ID')

    database.append([username, pin])
    print(database)