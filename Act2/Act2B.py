aNumber = int(input("Enter a Prime: "))

if aNumber == 0 or aNumber == 1:
    print(aNumber, "is not a prime number")
elif aNumber > 1:
   for i in range(2,aNumber):
       if (aNumber % i) == 0:
           break
   else:
       print(aNumber,"is a prime number")
else:
   print(aNumber,"is not a prime number")