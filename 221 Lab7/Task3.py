def counting_stairs(n, fib=None):
    if not fib:
        fib=[None]*(n+1)
    if n<=1:
        return 1
    if fib[n]:
        return fib[n]
    fib[n]=counting_stairs(n-1, fib)+counting_stairs(n-2, fib)
    return fib[n]
    
with open ('input3_4.txt','r') as fin:
    with open('output3_4.txt','w') as fout:
        fout.write(f'{counting_stairs(list(map(int,fin.readline().split())).pop())}')