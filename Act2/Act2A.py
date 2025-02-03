First_Term = int(input("Enter First term Number: "))
Second_Term = int(input("Enter Second term Number: "))

if First_Term < 0:
   print("")
else:
   total = 0
   for num in range (First_Term, Second_Term + 1):
      total += num 
  
print("The sum is", total)
   