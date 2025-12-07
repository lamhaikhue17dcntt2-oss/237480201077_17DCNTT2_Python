def sosanh(n, arr, k):
    a = 0
    for i in range(n):
        if arr[i] == k:
            a = 1
            return i + 1
    if a == 0:
        return -1


arr = []
k = int(input('Nhập k = '))
n = int(input('Nhập số phần tử: '))
for i in range(n):
    phantu = int(input(f"  Phần tử thứ {i+1}: "))
    arr.append(phantu)
if sosanh(n,arr,k) > -1:
    print ('Phan tử đầu tiên có giá tri = k: phần tử thứ',sosanh(n,arr,k))
else :
    print ('Không có phần tử nào bằng k')