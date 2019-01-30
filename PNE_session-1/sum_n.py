num = int(input( "Please enter an integer: " ))
number =0

if num != 0:
   for i in range(1, num+1):
       number += i
       print(number)
else:
     exit()
