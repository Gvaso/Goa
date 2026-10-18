Name = input("Enter your name: ")
Age = int(input("Enter your age: "))
print (str(Age >= 18) + " " + "You are over 18.")
print (str(Age < 18) + " " + "You are under 18.")
   
     # მომხმარებელს შევაყვანინეთ სახელი და ასაკი, გავიგეთ არის თუ არა მომხმარებელი 18 ზე მეტი წლის

Num1 = float(input("Enter the first number: "))
Num2 = float(input("Enter the second number: "))

print (str(Num1 > Num2) + " " + "The first number is greater than the second number.")
print (str(Num1 < Num2) + " " + "The first number is less than the second number.")
     
print (str(Num1 == Num2) + " " + "The first number is equal to the second number.")
            # მომხმარებელს შევაყვანინეთ ორი რიცხვი, გავიგეთ რომელია მეტია, ნაკლებია თუ ტოლია

user_password = input("Enter your password: ")
user_age = int(input("Enter your age: "))
password = "GoaArisN1!"
# შევაყვანინებთ პაროლს და ასაკს მომხარებელს
print(str(user_age >= 13 and user_password == password))
#გვეტყვის არის თუარა ჭეშმარიტი მითითებული ინფორმაცია მომხმარებლისგან

Product_price = float(input("Enter the product price: "))
user_age = int(input("Enter your age: "))

print (Product_price > 100 and user_age >= 18)
print (Product_price < 100 and user_age < 18)
#and
print (Product_price > 100 or user_age >= 18)
print (Product_price < 100 or user_age < 18)
#or

# შევაყვანინებთ პროდუქტის ფასს და ასაკს მომხარებელს