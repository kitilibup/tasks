x1 = float(input("Введите минимум x: "))
x2 = float(input("Введите максимум x: "))
step = float(input("Введите шаг: "))
while x1<=x2:
    y=-1.24 * x1**2 + x1
    x1+=step
    print ("шаг %s:" % x1, y)











