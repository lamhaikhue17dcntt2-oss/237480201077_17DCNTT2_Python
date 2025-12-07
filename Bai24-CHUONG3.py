n = 0; s = 0; c = 0; l = 0
while (n <= 0):
    n = int(input('Nhap so nguyen duong n: '))
while (n > 0):
    s = n % 10
    if (s % 2 == 0):
        c = c + 1
    if (s % 2 != 0):
        l = l + 1
    n = n // 10
print ('So chan',c)
print ('so le ',l)