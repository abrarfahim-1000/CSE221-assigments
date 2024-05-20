def karatsuba(x, y):
    if x < 10 or y < 10:
        return x*y

    n=max(len(str(x)), len(str(y)))
    m=n//2
    p=10**m

    xf=x//p
    xl=x%p 

    yf=y//p
    yl=y%p

    first=karatsuba(xf,yf)
    last=karatsuba(xl,yl)
    mid1=karatsuba(xf+xl,yf+yl)-first-last

    return first*(10**(2*m))+mid1*(10**m)+last

print(karatsuba(1920,1080))