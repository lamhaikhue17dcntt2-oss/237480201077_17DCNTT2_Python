def tb(a, arr):
    s = 0
    for i in range(a):
        s = s + arr[i]
    s = s / a
    return s

arr = []
a = int(input('Nhập a: '))
n = int(input('Nhập số phần tử: '))
for i in range(n):
    phantu = int(input(f"Nhập pt thứ {i+1}: "))
    arr.append(phantu)
print ('Trung bình cua',a,'phần tử đầu tiên:',float(tb(a, arr)))