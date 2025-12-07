n=int(input("nhap vao so nguyen: "))
t=n
s=0
while(n>0):
    s=s+n%10
    n=n//10

print("tong cac chu so cua ",t,"= ",s)
