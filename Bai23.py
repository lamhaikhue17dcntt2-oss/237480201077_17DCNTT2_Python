n = 0; s = 0
while (n <= 0):
    n = int(input('Nhap so nguyen duong n: '))
while (n > 0):
    s = s + 1
    n = n // 10
print (s)