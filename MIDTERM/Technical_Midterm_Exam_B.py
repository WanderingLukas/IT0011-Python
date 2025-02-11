#This codes stores the months 
month_list = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

#This code lets the user input the date
putIndate = input("Enter the Date (mm/dd/yyyy): ")

#This code splits the date by month, day and year by seperating them using "/"
month, day, year = putIndate.split("/")

#This code lets it access the month list  by using the input month 
#It also including minus 1 as index always starts with 0
current_month = month_list[int(month)-1]

#It removes the 0 on the inputed day by turning it into an interger and then back to a string
day = str(int(day))

#This code prints the date in more human readable terms
print(current_month, "" + day + " " + year)
