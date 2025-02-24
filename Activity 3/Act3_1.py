firstName = input("Enter your First name: ")
lastName = input("Enter your Last name: ")
yourAge = int(input("Enter your age: "))
fullName = firstName + " " + lastName
print(" ")

print("Full name: " + fullName)
print("Sliced Name: " + (fullName[:4]))
print("Greeting Message: Hello, " + (fullName[:4]) + "! Welcome. You are " + str(yourAge) + " years old" )
