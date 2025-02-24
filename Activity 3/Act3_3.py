firstName = input("Enter your First name: ")
lastName = input("Enter your Last name: ")
yourAge = int(input("Enter your age: "))
contactNumber = int(input("Enter your Contact Number: "))
course = input("Enter Course: ")

student_information = "Last Name: " + lastName + "\n" + "First Name: " + firstName + "\n" + "Age: " + str(yourAge) + "\n" + "Contact Number: " + str(contactNumber) + "\n" + "Course: " + course + "\n"

f=open("students.txt","a")
f.write(student_information)
f.close()
print("Student Information has been saved to 'students.txt")
