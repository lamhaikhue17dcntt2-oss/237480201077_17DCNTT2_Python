n = 0; s = 0
while (n <= 0):
    n = int(input('Nhap so nguyen duong n: '))
for i in range(1,n):
    k = 0; s = 0
    for j in range(1,i+1):
        s = s + j
        k = i
    if (s >= n):
        break
print ('So K lon nhat nho hon n:',k - 1)
   