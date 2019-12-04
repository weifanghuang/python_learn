# myDictionary = {"key": "value", "key1": "value}

myPhone = {"Iphone x": 1000, "Sumsung s9": 900}

print(myPhone)

Iphone_Price = myPhone["Iphone x"]
print("Iphone price: " + str(Iphone_Price))
# change key values
myPhone["Iphone x"] = 500
print(myPhone)

myPhone.clear()
print(myPhone)
