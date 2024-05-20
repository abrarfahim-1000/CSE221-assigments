
def minutes(time): #helper function, to convert the time into minutes
    hours, minutes = time.split(':')
    return int(hours) * 60 + int(minutes)

with open('input4.txt','r') as file:
    with open('output4.txt','w') as file2:
        n=int(file.readline().strip())
        m=n
        departures=[]
        revised=[]
        while n>0:
            new=list(file.readline().split())
            departures.append(new)
            n-=1
        for i in range(len(departures)):
            for j in range(i+1,len(departures)):
                if departures[j]<departures[i]:
                    departures[i],departures[j]=departures[j],departures[i]
        for i in range(len(departures)):
            for j in range(i+1,len(departures)):
                if departures[j][0]==departures[i][0]:
                    if minutes(departures[j][-1]) > minutes(departures[i][-1]):
                        departures[i],departures[j]=departures[j],departures[i]
                        break
        count=0
        for i in departures:
            for j in i:
                file2.write(f'{j} ')
            count+=1
            if count<m:
                file2.write('\n')