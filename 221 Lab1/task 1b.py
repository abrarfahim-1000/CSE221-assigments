with open ('input1b.txt','r') as file:
  with open ('output1b.txt','w') as file2:
    time=int(next(file))
    c=0
    for line in file:
      array=line.split()
      if array[2]=='+':
        file2.write(f'The result of {array[1]} {array[2]} {array[3]} is {int(array[1])+int(array[3])}')
        c+=1
      elif array[2]=='/':
        file2.write(f'The result of {array[1]} {array[2]} {array[3]} is {int(array[1])/int(array[3])}')
        c+=1
      elif array[2]=='*':
        file2.write(f'The result of {array[1]} {array[2]} {array[3]} is {int(array[1])*int(array[3])}')
        c+=1
      elif array[2]=='-':
        file2.write(f'The result of {array[1]} {array[2]} {array[3]} is {int(array[1])-int(array[3])}')
        c+=1
      if c<time:
        file2.write('\n')