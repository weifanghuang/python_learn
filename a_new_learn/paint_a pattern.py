import turtle

turtle.reset()
turtle.pencolor('white')
lens = 190 * 2
kuan = 100 * 2


# 画矩形
def kk(a, b):
    for n in range(1, 5):
        if n % 2 == 0:
            turtle.forward(b / 13)  # 列长
            turtle.right(90)
        else:
            turtle.forward(a / 2)  # 行长
            turtle.right(90)


# 红白条纹绘制函数
def rednw(a, b):
    f = 0
    for k in range(1, 14):
        if k < 8:
            turtle.up()
            turtle.goto(0, -b / 13 * f)
            turtle.down()
            f = f + 1
            # 循环填充颜色-条件语句
            if k % 2 != 0:
                turtle.fillcolor("red")
                turtle.begin_fill()
                # 画小条纹
                kk(a, b)
                turtle.end_fill()
            else:
                kk(a, b)
        else:
            turtle.up()
            turtle.goto(-a / 2, -b / 13 * f)
            turtle.down()
            f = f + 1
            if k % 2 != 0:
                turtle.fillcolor("red")
                turtle.begin_fill()
                # 画小条纹
                kk(a * 2, b)
                turtle.end_fill()
            else:
                kk(a, b)


# 星星的框架 并填充蓝色
def kkb(a, b):
    turtle.up()
    turtle.goto(-a / 2, 0)
    turtle.down()
    turtle.fillcolor("blue")
    turtle.begin_fill()
    for n in range(1, 5):
        if n % 2 == 0:
            turtle.forward(b / 13 * 7)
            turtle.right(90)
        else:
            turtle.forward(a / 2)
            turtle.right(90)
    turtle.end_fill()


# 画星星
def star(a):
    turtle.fillcolor("white")
    turtle.begin_fill()
    for n in range(1, 6):
        turtle.forward(a / 33)
        turtle.right(144)
    turtle.end_fill()


# 第一类 每行六颗星
def lin1star(a, b):
    c1 = -2
    x = a / 23
    for j in range(1, 6):
        c1 = c1 + 2
        b1 = 1
        for i in range(1, 7):
            turtle.up()
            turtle.goto(-x * b1, -9 + c1 * 2 * (-b / 36))
            turtle.down()
            b1 = b1 + 2
            # 绘制五角星
            star(a)


def lin2star(a, b):
    c2 = -1
    x = a / 23
    for j in range(1, 5):
        c2 = c2 + 2
        b2 = 2
        for i in range(1, 6):
            turtle.up()
            turtle.goto(-x * b2, -9 + c2 * 2 * (-b / 36))
            turtle.down()
            b2 = b2 + 2
            # triangle
            star(a)


def USAflag(a, b):
    rednw(a, b)
    kkb(a, b)
    lin1star(a, b)
    lin2star(a, b)
    turtle.up()
    turtle.goto(lens / 2 + 4, 0)
    turtle.down()
    turtle.pencolor('black')
    turtle.write("USA FLAG")


# 调用USAflag（）开始画图
USAflag(lens, kuan)
