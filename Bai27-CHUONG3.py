m = 0; a = 0; n = 1
while (m <= 1):
    m = float(input('Nhap so nguyen duong m: '))
while (a == 0):
    s = 0
    for i in range(1,n+1):
        s = s + (1/i)
    if (s >= m):
        break
    else :
        n = n + 1
print ('Ket qua n =',n)