with open ('input1a.txt','r') as file:
   with open ('output1a.txt','w') as file2:
      time=int(next(file))
      count=0
      for line in file:
         if int(line)%2==0:
            file2.write(f'{line.strip()} is an even number')
            count+=1
         else:
            file2.write(f'{line.strip()} is an odd number')
            count+=1
         if count<time:
            file2.write('\n')