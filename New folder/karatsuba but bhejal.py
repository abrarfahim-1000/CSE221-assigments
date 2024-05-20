def modified_kr(int1, int2):
    if(int1 < 100 or int2 < 100):
        return int1*int2
    h = max(len(str(int1)), len(str(int2)))//3
    a = int1//10**(2*h)
    temp = int1%10**(2*h) 
    b = temp//10**h
    c = temp%10**h

    d =  int2//10**(2*h)
    temp = int2%10**(2*h)
    e = temp//10**h
    f = temp%10**h

    ad = modified_kr(a, d)
    be = modified_kr(b, e)
    cf = modified_kr(c, f)

    ae_plus_bd = modified_kr((a+b), (d+e)) - ad - be 
    bf_plus_ce = modified_kr((b+c), (f+e)) - be - cf 

    af_plus_be_plus_cd = modified_kr((a+b+c),(d+e+c)) - ae_plus_bd - bf_plus_ce - ad - cf

    return ad*10**(4*h) + (ae_plus_bd)*10**(3*h) + (af_plus_be_plus_cd)*10**(2*h) + (bf_plus_ce)*10**(h) + cf

print(modified_kr(1200112,300112))
print(1200112* 300112)
print(modified_kr(1920,1080))