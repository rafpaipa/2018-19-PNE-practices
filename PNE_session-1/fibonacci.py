n = int(input( "Please enter an integer: " ))

n1 = 0
n2 = 1
count = 0


if n == 1:
   print(n1)
else:
   print("Fibonacci sequence for ",n,"terms:")
   while count < n:
       print(n1,end=' , ')
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1