def coin_change(coins,target):
    step=[float('inf')]*(target+1)
    step[0]=0
    for i in range(1,target+1):
        for coin in coins:
            if i-coin>=0:
                step[i]=min(step[i],step[i-coin]+1)
    return step[target]

with open ('input4_2.txt','r') as fin:
    with open('output4_2.txt','w') as fout:
        coin,target=list(map(int,fin.readline().split()))
        coins=[int(x) for x in fin.readline().split()]
        fout.write(str(coin_change(coins,target)))