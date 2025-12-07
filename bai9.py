st=int(input("nhap so tien: "))
sttam=st
to50=to20=to10=to5=to2=to1=0
if(st>=50000):
    to50=st//50000
    st=st-(50000*to50)

if(st>=20000):
    to20=st//20000
    st=st-(20000*to20)

if(st>=10000):
    to10=st//10000
    st=st-(10000*to10)

if(st>=5000):
    to5=st//5000
    st=st-(5000*to5)

if(st>=2000):
    to2=st//2000
    st=st-(2000*to2)

if(st>=1000):
    to1=st//1000
    st=st-(1000*to1)

print(" co ",to50," to 50000",
      " co ",to20," to 20000",
      " co ", to10," to 10000",
      " co ",to5," to 5000",
      " co ",to2," 2000",
      " co ",to1," to 1000")
      
 




