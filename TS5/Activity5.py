def main_main ():
    print("[D] - Divide")
    print("[E] - Exponentiation")
    print("[R] - Remainder")
    print("[F] - Summation")
    while True:
        choose = input("Enter a letter (D,E,R and F only): ").upper()
        if choose not in ['D','E','R','F' ]:
            print("Please choose D, E, R, or F only.")
        else:
            print("You chose: " + choose)
            break
        
    num1 = int(input("Enter the 1st Number: "))
    num2 = int(input("Enter the 2nt Number: "))     
        
    if choose == 'D':
        result = divide(num1, num2)
        if result is not None:
            print("Result:", result)
        else:
            print("Denominator cannot be zero")
            
    elif choose == 'E':
        result = exponentiation(num1, num2)
        print("Result:", result)
        
    elif choose == "R":
        result = remainder(num1, num2)
        if result is not None:
            print("Result:", result)
        else:
             print("Denominator cannot be zero")
    elif choose == "F":
        result = summation(num1, num2)
        if result is not None:
            print("Result:", result)
        else:
            print("Second number must be greater than the first number")
 
        
def divide(x, y):
  if y != 0:
    return x / y
  else:
    return None

def exponentiation(x, y):
  return x ** y

def remainder(x, y):
  if y != 0:
    return x % y
  else:
    return None

def summation(x, y):
  if y > x:
    return sum(range(x, y+1))
  else:
    return None                 

main_main()