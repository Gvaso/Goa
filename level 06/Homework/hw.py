Num1 = int(input("Enter the first number: "))
Num2 = int(input("Enter the second number: "))

print(Num1 == Num2)
print(Num1 < Num2)
print(Num1 > Num2)
# #მოხმარებელს შემოვაყვანიე რიცხვი და გავაგებიე მეტია თუ არა ნაკლებია თუ ტოლია . 


Grade = int(input("Enter your grade: "))

if Grade > 50:
    print ("More Then 50")
elif Grade < 50:
    print ("Less Then 50")
else:
    print ("Equal To 50")
    #მოხმარებელს შემოვაყვანიე ქულა და გავაგებიე მეტია, ნაკლებია თუ ტოლია 50 ზე.


Product = float(input("Enter the product price: "))
Price = float(input("Enter the price you want to pay: "))

if Price > Product:
    print ("You have paid more than the product price.")
elif Price < Product:
        print ("You have paid less than the product price.")
else:
    print ("You have paid the exact product price.")
 #მოხმარებელს შემოვაყვანიე პროდუქტის ფასი და გავაგებიე მეტია, ნაკლებია თუ ტოლია პროდუქტის ფასზე.
digit = int(input("Enter a digit: "))

if digit % 2 == 0:
    print("The digit can be divided by 2.")
else:
    print("The digit cannot be divided by 2.")
#მოხმარებელმა შეიყვანა მთელი რიცხვი და გაიგო, რიცხვი იყოფა თუ არა 2 ზე 