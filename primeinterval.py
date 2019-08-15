num=int(input());
if num > 1:
   # check for factors
   for i in range(3,n):
       if (n % i) == 0:
           print(n,"is not a prime number")
           print(i,"times",n//i,"is",n)
           break
   else:
       print(n,"is a prime number")
       

else:
   print(n,"is not a prime number")
