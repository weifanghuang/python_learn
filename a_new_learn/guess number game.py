import random
times = 3 #程序运行3次
number = random.randint(1,10) #取1到10的随机数
print("........I love kim........")  #我的名字
guess = 0
print("May guess what number is in my mind now:")
while (guess != number) and (times > 0):
     temp = input()
     while not temp.isdigit():
         temp = input("sorry enterde is incorrect,please enter an integer")
     guess = int(temp)
     times = times - 1
     if guess == number:
        print("Congratulations, you are my Ms Right")
        print("Give me five")
     else:
        if guess > number:
            print("Sorry the number you entered is too large")
        else:
            print("Sorry the number you entered is too small")
        if times > 0:
            print("Please try again:")
        else:
            print("Chance is running out")
print("Game over")
