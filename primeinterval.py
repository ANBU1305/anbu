num=int(input());
if num > 1:
   # check for factors
   for i in range(3,n):
       if (n % i) == 0:
           print(n,"is not a prime number")
           print(i,"times",n//i,"is",n)
           break
   else:
       if((n%2)==0){
          print(n);
        }
       

else:
   print(n);
