import math

def sc(n):
    if n % 2 == 0:
        print (n,'Là số chẵn')
    else:
        print (n,'Không là số chẵn')

def shh(n):
    s = 0
    for i in range(1,n):
        if n % i == 0:
            s += i 
    return s

def snt(n):
    s = 0
    for i in range(2,n):
        if n % i == 0:
            s = 1
    return s

def scp(n):
    s = 0
    can = int(math.sqrt(n))
    if  can * can != n:
        s = 1
    return s

def ucln(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

def bcnn(a, b):
    return int((a * b) / ucln(a, b))

def sntcn(a, b):
    if ucln(a,b) == 1:
        print (f'{a},{b} là nguyên tố cùng nhau')

s = 0; 
print ('==============================================')
print ('1. Kiểm tra số chẵn')
print ('2. Kiểm tra số hoàn hảo')
print ('3. Kiểm tra số chính phương')
print ('4. Kiểm tra số chính phương')
print ('5. Tìm UCLN của 2 số')
print ('6. TÌm BCNN của 2 số')
print ('7. Kiểm tra 2 số có là nguyên tố cùng nhau')
print ('0. Thoát')
print ('==============================================')
while s == 0:
    yc = int(input('Nhập yêu cầu: '))
    if yc > 0 and yc < 5 :
        n = int(input('Nhập n = '))
        if yc == 1:
            sc(n)
        elif yc == 2:
            if n == shh(n):
                print (n,'Là số hoàn hảo')
            else:
                print (n,'Không là số hoàn hảo')
        elif yc == 3:
            if scp(n) == 0:
                print (n,'Là số chính phương')
            else:
                print (n,'Không là số chính phương')
        elif yc == 4:
            if snt(n) == 0:
                print (n,'Là số nguyên tố')
            else:
                print (n,'Không là số nguyên tố') 
    elif yc > 4 and yc < 8:
        a = int(input('Nhập a = '))
        b = int(input('Nhập b = '))
        if yc == 5:
            print (f'UCLN của {a} và {b} là: {ucln(a, b)}')
        if yc == 6:
            print (f'BCNN của {a} và {b} là: {bcnn(a, b)}')
        if yc == 7:
            sntcn(a, b)
    elif yc == 0:
        break