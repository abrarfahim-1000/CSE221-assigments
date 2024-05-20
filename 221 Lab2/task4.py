with open('input4.txt','r') as file:
    with open('output4.txt','w') as file2:
        people=[]
        tasklist=[]
        checklist=[]
        count=0
        tasklistrev=[]
        task,man=list(map(int,file.readline().split()))
        for line in file:
            tasklist.append(list(map(int,line.split())))
        for i in tasklist:
            tasklistrev.append(i)
        for i in range(len(tasklist)):
            for j in range(i+1,len(tasklist)):
                if tasklist[i][0]+tasklist[i][1]>tasklist[j][0]+tasklist[j][1]:
                    tasklist[i],tasklist[j]=tasklist[j],tasklist[i]
        for i in range(len(tasklistrev)):
            for j in range(i+1,len(tasklistrev)):
                if tasklistrev[i][0]>tasklistrev[j][0]:
                    tasklistrev[i],tasklistrev[j]=tasklistrev[j],tasklistrev[i]
        for tsk in range(man):
            people.append(tasklistrev[tsk])
            count+=1
            checklist.append(tasklistrev[tsk])
        for elem in tasklist:
            if elem not in checklist:
                start,end=elem
                for l in range(len(people)):
                    if start>=people[l][1]:
                        people[l]=elem
                        count+=1
                        checklist.append(tasklistrev[tsk])
                        break
        file2.write(str(count))