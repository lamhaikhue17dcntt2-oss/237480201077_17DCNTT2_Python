def snt(a):
    s = 0
    for i in range(2,a):
        if a % i == 0:
            s = s + 1
    if s == 0:
        print (a,'là số nguyên tố')
    else:
        print (a,'không phải là số nguyên tố')
a = int(input('Nhập a = '))
snt(a)