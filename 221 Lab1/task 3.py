def selection(array1,array2):
    for i in range(len(array1)):
        idx=i
        for j in range(i+1,len(array1)):
            if array1[j]>array1[idx]: 
                idx=j
            elif (array1[j]==array1[idx] and array2[j]<array2[idx]):
                idx=j
        array1[i],array1[idx]=array1[idx],array1[i]
        array2[i],array2[idx]=array2[idx],array2[i]
# Here I have chosen selection sort so I can ensure there is a minimum amount of swaps
# line 9 and line 10 indicate that I have only swaped once per outer loop iteration in both lists.

with open('input3.txt','r') as file:
    n=int(file.readline().strip())
    id=list(map(int,file.readline().split()))
    number=list(map(int,file.readline().split()))
selection(number,id)
count=0
with open('output3.txt','w') as file2:
    for student_id, marks in zip(id,number):
        file2.write(f'ID:{student_id} Marks:{marks}')
        count+=1
        if count<n:
            file2.write('\n')
        