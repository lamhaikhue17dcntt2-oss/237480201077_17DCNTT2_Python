def chuoinn(n, arr):
    min = 1000
    x = 0
    for i in range(n):
        s = 0
        for letter in arr[i]:
            s = s + 1
        if s < min:
            min = s
            x = i + 1
    print ('Chuỗi ngắn nhất: chuỗi',x)

arr = []
n = int(input('Nhập số lượng chuỗi: '))
for i in range(n):
    chuoi = str(input(f'chuoi {i + 1}: '))
    arr.append(chuoi)
chuoinn(n, arr)



