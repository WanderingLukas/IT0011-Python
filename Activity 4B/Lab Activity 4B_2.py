currencyData = {}

f = open("currency.csv", "r")
for line in f:
    if  "code,name,rate" in line:
           continue
       
    parts = line.strip().split(',')

    currencyCode = parts[0]
    exchangeRate = float(parts[2])

    currencyData[currencyCode] = exchangeRate

howMuch = int(input("How much dollar do you have? "))
whatCurrency = input("What Currency you want to have? ").upper()


if whatCurrency in currencyData:
    amount = howMuch * currencyData[whatCurrency]
    print("Dollar: " + str(howMuch) + " USD")
    print(whatCurrency + ": " + str(amount))
else:
    print("Currency not found.")
