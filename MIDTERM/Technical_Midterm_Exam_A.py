
#This line of code gives a path for the file to the program
file = "numbers.txt"

#This code opens the number.txt and read it line by line start from 1
with open (file) as numtext:
    line_num = 1 
    
    #This block of codes loops through each line in the numbers.txt
    #It also removes any extra spaces from beginning  to the end of the line
    for line in numtext:
        line= line.strip()
        #This code lets it split the line of numbers with commas like
        nums = line.split(',')
        #This line of code sums the integers on each lines and ignores empty spaces
        line_sum = sum(int(num) for num in nums if num.strip() != "")
    
        #This line of code turns the line_sum into an integer and reverses it
        reverse = int(str(line_sum)[::-1])

        #This line of code checks if the line_sum is a palindrome by reversing it and comparing it to "reverse"
        #If it fits with the "reverse" it will say it is a "Palindrome" but if not it will say "Not Palindrome"
        if line_sum == reverse:
            IsOrNotaPalindrome = "Palindrome"
        else:
            IsOrNotaPalindrome = "Not Palindrome"
        #Prints the Line along its number i.e "Line 1 : 10,20,30,40,50" along with its total sum which is 150 and 
        #shows the result of the sum of all numbers on line  and show either it is a Palindrome or not 
        print("Line " + str(line_num) + ": " + line + " (sum " + str(line_sum) + ") - " + IsOrNotaPalindrome)
        
        #If the line_num is below 10 it will continue to increase Line # until it reaches 10 which is the max
        #according to the number.txt 
        if line_num == 10:
            break
        line_num +=1
        

