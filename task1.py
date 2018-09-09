a = float(input("Введите число:"))
b = input("Во что перевести число - в байты (bytes) или килобайты (kbytes)?")
if b == 'bytes':
    print ("число %s в байтах = " % a, a * 1024)
elif b == 'kbytes':
    print ("число %s в кбайтах = " % a, a / 1024)




