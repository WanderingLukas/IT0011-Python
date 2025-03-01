students = []
filename=""

while True:
    print("Main Menu")
    print("1. Open File")
    print("2. Save File")
    print("3. Save as File")
    print("4. Show All Students Record")
    print("5. Show Student Record")
    print("6. Add Record")
    print("7. Edit Record")
    print("8. Delete Record")
    
    option = int(input("Please enter a number only: "))
    
    if option == 1: #Opens a file
        filename = input("Enter the filename to open: ")
        students.clear()  
        try:
            with open(filename + ".txt", 'r') as file:
                for line in file:
                    data = line.strip().split(',')
                    studentID = data[0]
                    firstName = data[1]
                    lastName = data[2]
                    classStanding = float(data[3])
                    examGrade = float(data[4])
                    students.append((studentID, (firstName, lastName), classStanding, examGrade))
            print("File " + filename + " loaded successfully.")
        except FileNotFoundError:
            print("File not found. Starting with an empty student record list.")
            
    elif option ==2: #Save the file
        if not filename:
            filename = input("Enter the filename to save: ")
            
        with open(filename + ".txt", 'w') as f:
                for student in students:
                    studentID, (firstName, lastName), classStanding, examGrade = student
                    f.write(studentID + "," + firstName + "," + lastName + "," + str(classStanding) + "," + str(examGrade) + "\n")
        print("File " + filename +" saved successfully.")
            
    elif option == 3: #Saves the file as another file
        filename = input("Enter the filename to save as: ") 
        with open(filename + ".txt", 'w') as f:
            for student in students:
                studentID, (firstName, lastName), classStanding, examGrade = student
                f.write(studentID + "," + firstName + "," + lastName + "," + str(classStanding) + "," + str(examGrade) + "\n")
            print("File saved successfully as", filename)

    elif option ==4: #Shows all the Student Records
        if not students:
            print("No student records available.")
        else: 
            print("Choose display order:")
            print("1. By Last Name")
            print("2. By Grade (60% Class Standing + 40% Exam)")
            otherOption = input("Enter choice: ")
            
            if otherOption == "1": #Order by Names
                sorted_students = sorted(students, key=lambda x: x[1][1].lower())
            elif otherOption == "2": #Order by Grades
                sorted_students = sorted(students, key=lambda x: (0.6 * x[2] + 0.4 * x[3]), reverse=True)
            else:
                print("Invalid choice. Showing default order.")
                sorted_students = students
            for student in sorted_students:
                studentID, (firstName, lastName), classStanding, examGrade = student
                final_grade = 0.6 * classStanding + 0.4 * examGrade
                print("ID: " + studentID + " | Name: " + firstName + " " + lastName + " | Class Standing: " + str(classStanding) + " | Exam Grade: " + str(examGrade) + " | Final Grade: " + str(round(final_grade, 2)))
    
    
    elif option ==5: #Show Student Record Specified
        student_id = input("Enter Student ID to search: ")
        found = False
        for student in students:
            if student[0] == student_id:
                studentID, (firstName, lastName), classStanding, examGrade = student
                final_grade = 0.6 * classStanding + 0.4 * examGrade
                print("ID: " + studentID + " | Name: " + firstName + " " + lastName + " | Class Standing: " + str(classStanding) + " | Exam Grade: " + str(examGrade) + " | Final Grade: " + str(round(final_grade, 2)))
                found = True
                break
        if not found:
            print("Student not found.")
        
    elif option ==6: #Adds Student Record
        while True:
            studentID = input("Enter Student ID (6-digit number): ")
            
              
            if len(studentID) == 6 and studentID.isdigit():
                break  
            else:
                print("Student ID must be exactly 6 digits. Please try again.")
            
        if any(student[0] == studentID for student in students):
            print("Error: Student ID already exists.")
        else:
            firstName = input("Enter First Name: ")
            lastName = input("Enter Last Name: ")
            classStanding = float(input("Enter Class Standing Grade: "))
            examGrade = float(input("Enter Major Exam Grade: "))
            students.append((studentID, (firstName, lastName), classStanding, examGrade))
            print("Record added successfully.")
       
    elif option ==7: #Edit Student Record
        student_id = input("Enter Student ID to edit: ")
        found = False
    
        for i, student in enumerate(students):
            if student[0] == student_id:
                firstName = input("Enter New First Name: ")
                lastName = input("Enter New Last Name: ")
                classStanding = float(input("Enter New Class Standing Grade: "))
                examGrade = float(input("Enter New Major Exam Grade: "))
                students[i] = (student_id, (firstName, lastName), classStanding, examGrade)
                found = True
                print("Record updated successfully.")
                break

        if not found:
            print("Student ID not found.")
        
    elif option == 8: #Deletes Student Record
        student_id = input("Enter the student ID to delete: ")
        original_count=len(students)
        students[:] = [student for student in students if student[0] != student_id]
        if len(students) == original_count:
            print("Student ID not found.")
        else:
            print("Student record deleted successfully.")
            
            if filename:
                with open(filename + ".txt", 'w') as f:
                    for student in students:
                        studentID, (firstName, lastName), classStanding, examGrade = student
                        f.write(studentID + "," + firstName + "," + lastName + "," + str(classStanding) + "," + str(examGrade) + "\n")
                print("File updated successfully after deletion.")