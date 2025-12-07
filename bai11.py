while 1:
    n=int(input("nhap vao so nguyen n: "))
    if(n<=0):
        print("n phai la so nguyen duong")
    if(n>0): break


if(n%7==0 and n%5==0):
    print("n chia het cho 5 va 7")
else:
    print("n ko chia het cho 5 va 7")