num = int(input("Enter The Digit: "))
if num > 0:
    print("Your Digit Is Positive")
elif num < 0 : 
    print ("Your Digit Is Negative")
else:
    print("Your Digit Equal To 0")
if num % 2== 0:
        print("Your Digit Is Even")
else:
    print("Your Digit Is Odd")
    #მომხმრაბელს შემოვაყვანინეთ რიცხვი და გავაგებიეთ მისი რიცხვი დადებითი იყო უარყოფითი და ლუწი იყო თუ კენტი

digit = 45
guess_digit = int(input("Enter The Digit:"))
mistakes = 0

while guess_digit != digit:
    mistakes = mistakes + 1

    if guess_digit < digit:
        print("შენი შეყვანილი რიცხვი ნაკლებია საიდუმლო რიცხვზე")
    else:
        print("შენი შეყვანილი რიცხვი მეტია საიდუმლო რიცხვზე")

    guess_digit = int(input("Guess Again: "))

print("გილოცავ! სწორი რიცხვი გამოიცანი!")
print("შეცდომების რაოდენობა:", mistakes)
print("მცდელობების რაოდენობა:", mistakes + 1)
#მომხარებელი შემოიყვანს რიცხვს ის მაქამდე გამოიცნობს სანამ ეს რიცხვი არ იქნება სწორი 

total = 0

while True:
    price = float(input("შეიყვანე პროდუქტის ფასი: "))
    quantity = int(input("შეიყვანე პროდუქტის რაოდენობა: "))

    if price <= 0 or quantity <= 0:
        print("ფასი და რაოდენობა უნდა იყოს დადებითი!")
        continue

    product_total = price * quantity
    total = total + product_total

    print("პროდუქტის ღირებულება:", product_total)

    answer = input("გსურს კიდევ პროდუქტის დამატება? (yes/no): ")

    if answer == "no":
        break

if total >= 200:
    discount = total * 0.15
elif total >= 100:
    discount = total * 0.10
else:
    discount = 0

final_total = total - discount

print("საწყისი თანხა:", total, "ლარი")
print("ფასდაკლება:", discount, "ლარი")
print("საბოლოო გადასახდელი თანხა:", final_total, "ლარი")
# მომხმარებელს შეჰყავს პროდუქტის ფასი და რაოდენობა, პროგრამა ითვლის პროდუქტის ღირებულებას, ამატებს კალათის ჯამურ თანხას და თანხის მიხედვით ითვლის ფასდაკლებასა და საბოლოო გადასახდელ თანხას.

total = 0
tickets_total = 0
discount_total = 0

while True:
    age = int(input("შეიყვანე ასაკი: "))
    tickets = int(input("შეიყვანე ბილეთების რაოდენობა: "))

    if age < 0 or tickets <= 0:
        print("არასწორი მონაცემებია!")
        continue

    if age < 12:
        price = 10
    elif age >= 60:
        price = 12
    else:
        price = 15

    start_price = price * tickets

    if tickets >= 5:
        discount = start_price * 0.20
    elif tickets >= 3:
        discount = start_price * 0.10
    else:
        discount = 0

    final_price = start_price - discount

    total = total + final_price
    tickets_total = tickets_total + tickets
    discount_total = discount_total + discount

    print("შესყიდვის ღირებულება:", final_price, "ლარი")

    answer = input("გსურს კიდევ ბილეთების შეძენა? (yes/no): ")

    if answer == "no":
        break

print("შეძენილი ბილეთების რაოდენობა:", tickets_total)
print("საწყისი ღირებულება:", total + discount_total, "ლარი")
print("მიღებული ფასდაკლება:", discount_total, "ლარი")
print("საბოლოო გადასახდელი თანხა:", total, "ლარი")

# მომხმარებელს შეჰყავს ასაკი და ბილეთების რაოდენობა, პროგრამა ასაკის მიხედვით განსაზღვრავს ბილეთის ფასს, რაოდენობის მიხედვით ითვლის ფასდაკლებას და შეძენის დასრულებისას გამოაქვს ბილეთების საერთო რაოდენობა, საწყისი ღირებულება, ფასდაკლება და საბოლოო თანხა.

balance = 500
transactions = 0

while True:
    print("\n--- BANK MENU ---")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        print("Your balance is:", balance, "GEL")

    elif choice == "2":
        amount = float(input("Enter deposit amount: "))

        if amount > 0:
            balance = balance + amount
            transactions = transactions + 1
            print("Money deposited successfully!")
            print("Updated balance:", balance, "GEL")
        else:
            print("Amount must be positive!")

    elif choice == "3":
        amount = float(input("Enter withdrawal amount: "))

        if amount <= 0:
            print("Amount must be positive!")
        elif amount > balance:
            print("Not enough money!")
        else:
            balance = balance - amount
            transactions = transactions + 1
            print("Money withdrawn successfully!")
            print("Updated balance:", balance, "GEL")

    elif choice == "4":
        print("Successful transactions:", transactions)
        print("Final balance:", balance, "GEL")
        print("Goodbye!")
        break

    else:
        print("Invalid option! Try again.")
# მომხმარებელი საბანკო მენიუდან ირჩევს სასურველ მოქმედებას, პროგრამა აძლევს ბალანსის შემოწმების, თანხის შეტანისა და გამოტანის შესაძლებლობას, ითვლის წარმატებულ ტრანზაქციებს და სისტემიდან გასვლისას აჩვენებს საბოლოო ბალანსსა და ოპერაციების რაოდენობას.