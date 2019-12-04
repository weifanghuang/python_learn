def hello(name):
    return "Hello " + name + "!"


print(hello("world"))
print(hello("kim"))


def fibs(num):
    result = [0, 1]
    for i in range(num - 2):
        result.append(result[-2] + result[-1])
    return result


num = int(input('How many Fibonacci numbers do you want?'))
fibs(num)
