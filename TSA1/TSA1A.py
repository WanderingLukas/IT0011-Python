characters1 = input("Enter a String: ")

vowel = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z",
"B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "X", "Y", "Z"]
numberVowels = 0 
numberConsonants = 0
numberSpaces = 0
numberOther = 0

for char in characters1:
    if char in vowel:
        numberVowels += 1
    elif char in consonants: 
        numberConsonants +=1  
    elif char == ' ':
        numberSpaces +=1
    else :
        numberOther  +=1
    
print("Input string: ", characters1)
print ("Number of Vowels: ", numberVowels) 
print ("Number of Consonants: ", numberConsonants) 
print ("Number of Spaces: ", numberSpaces) 
print ("Number of Others: ", numberOther) 