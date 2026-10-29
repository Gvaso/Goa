num = int(input("Enter a number: "))

count = 0

for i in range(1, 11):
    result = num * i

    if result % 3 == 0:
        print(num, "x" , i, "=" ,result, "| Divisible by 3")
        count += 1
    else:
        print (num, "x" , i, "=" , result, "| Not divisible by 3")

print("Total divisible by 3:", count)
#მომხმარებელმა შემოიყვანა რიცხვი და გადამრავდლა 1 2 3 და ასეშემდეგ და შემდეგ დაუწერა ეს რიცხვი იყოფოდა თუ არა 3 ზე 

balance = 1000

deposits = 0
withdrawals = 0

total_deposited = 0
total_withdrawn = 0

while True:
    print("====== BANK SYSTEM ======")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Transaction Summary")
    print("5. Exit")
    print("=========================")
                                          
    choice = int(input("Choose an option: "))

    if choice == 1:
        print("Current balance:", balance, "GEL")

    elif choice == 2:
        amount = float(input("Enter deposit amount: "))

        if amount > 0:
            balance += amount
            deposits += 1
            total_deposited += amount
            print("Deposit successful!")
        else:
            print("Invalid amount!")

    elif choice == 3:
        amount = float(input("Enter withdrawal amount: "))

        if amount <= 0:
            print("Invalid amount!")
        elif amount > balance:
            print("Not enough money!")
        else:
            balance -= amount
            withdrawals += 1
            total_withdrawn += amount
            print("Withdrawal successful!")

    elif choice == 4:
        print("====== TRANSACTION SUMMARY ======")
        print("Current balance:", balance, "GEL")
        print("Total deposits:", deposits)
        print("Total withdrawals:", withdrawals)
        print("Total money deposited:", total_deposited, "GEL")
        print("Total money withdrawn:", total_withdrawn, "GEL")

    elif choice == 5:
        print("Thank you for using our bank!")
        break

    else:
        print("Invalid option! Choose 1-5.") 
#