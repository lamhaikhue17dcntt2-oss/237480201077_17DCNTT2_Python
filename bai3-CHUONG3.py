def ArmStrong(a):
    z = 0; dem = 1; n = a; s = 0;b = a
    while z == 0:
        if int(n/10) > 0:
            dem = dem + 1
        elif n == 0 :
            break
        n = n / 10

    for i in range(dem):
       x = 0
       x = int(a % 10)
       c = x
       for j in range(dem - 1):
           c = c * x
       s = s + c
       c = 0
       a = a / 10
    if b == s:
        print (b,'là số Armstrong')
    else :
        print (b,'không là số Armstrong')

a = int(input('Nhập a = '))
ArmStrong(a)