temp = input("please enter a year:")
while not temp.isdigit():
    temp = input("sorry, you input is incorrect,please enter an integer:")
year = int(temp)
if year/40 == int(year/400):
    print(tmpe + 'is leap year')
else:
    if(year/4 == int(year/4)) and (year/100 != int(year/100)):
        print(temp + 'is leap year')
    else:
        print(temp + 'is not leap year')
            
             
