
x=int(input("Введите число,требующее первода в иную сс "))
y=int(input("Введите желаемую СС" ))
if y==2:
    b = ''
    while x > 0:
        b = str(x % 2) + b
        x = x // 2
    print(b)
else:
    b = ''
    while x > 0:
        b = str(x % 8) + b
        x = x // 8
    print(b)
