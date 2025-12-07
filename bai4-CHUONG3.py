def max(n,arr):
    a = 0
    max = 0
    for i in range(n):
        if arr[i] > a:
            a = arr[i]
            max = i
    print (f"Vị trí phần tử lớn nhất: phần tử thứ {max + 1}")

arr = {}
n = int(input('Nhập số phần tử: '))
for i in range(n):
    phantu = int(input(f"  Phần tử thứ {i+1}: "))
    arr[i] = phantu
max(n,arr)