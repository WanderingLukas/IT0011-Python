aNumber = 5

for aNumber1 in range(aNumber):
    for aNumber2 in range (aNumber-aNumber1-1):
        print (" ", end=" ")
    for aNumber2 in range (aNumber1+1) :
        print(aNumber2+1, end=" ")
    print()
    