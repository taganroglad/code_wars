def ooo(x, y, z):

    numbers = [x, y, z]
    for i in numbers:
        i +=10
        print(i)
    return x, y, z
print(ooo(1, 3, 5))