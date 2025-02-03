
Num1 = int(input("Please Enter a Number 1#: "))

Num2 = int(input("Please Enter a Number 2#: "))

Num3 = int(input("Please Enter a Number 3#: "))

if (Num1 < Num2) and (Num1 < Num3):
    lowest = Num1
elif (Num2 < Num1) and (Num2 < Num3):
    lowest = Num2
else:
    lowest = Num3
    
if (Num1 > Num2) and (Num1 < Num3):
    middle = Num1
elif (Num1 < Num2) and (Num1 > Num3):
    middle = Num1
elif (Num2 > Num1) and (Num2 < Num3):
    middle = Num2
elif (Num2 < Num1) and (Num2 > Num3):
    middle = Num2
else:
    middle = Num3
  

if (Num1 > Num2) and (Num1 > Num3):
    highest = Num1
elif (Num2 > Num1) and (Num1 > Num3):
    highest = Num2
else:
    highest = Num3
    
print("The highest number is:", highest )
print("The middle number is:", middle )
print("The lowest number is:", lowest )