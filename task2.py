sum = input("Введите натуральное число:")
a = 1
b = 1
for i in sum:
    if i in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            a += int(i)
            if int(b)>0:
                b *= int(i)
print ("Сумма:", a)
print ("Произведение:", b)


