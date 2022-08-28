print("Welcome to the tip calculator!!")
bill = int(input("What was the total bill?: "))
tip  = int(input("How much tip Options >>> 10%, 12%, 15%?: "))
ppl  = int(input("How many people to split the bill?: "))

print(
    (bill/ppl) * (tip/100)+1)

