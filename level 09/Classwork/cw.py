i = 0
while i < 5:
    print("Saba")
    i += 1
#5 ჯერ დაიპრინტა ჩემი სახელი
total = 0
i = 0

while i < 10:
    total = total + i
    i = i + 1

print(total)
#0-10 ის ჩათვლით გამოითვალა რიცხვთა ჯამი
num = int(input("Enter The Number: "))

i = 0
total = 0

while i <= num:
    total = total + i
    i = i + 2

print(total)
#მომხმარებელს შემოვატანიეთ რიცხვი და 0 დან გამოთვალა მხოლოდ ლუწების ჯამი
saved_password = "1234"
password_input = input("Enter the password: ")

while password_input != saved_password:
    print("Incorrect password. Please try again.")
    password_input = input("Enter the password: ")
    # მომხმარებელს შემოყვანს პაროლი იქამდე სანამ პაროლი სწორი არ იქნება 

age = int(input ("Enter age: "))

if age >= 18:
    print("You are adult ")
else: 
    print("You are not adult")
    # მომხარებელმა შეიყვანა ასაკი და კომპიუტერმა უპასუხა იყო თუ არა ის სრულწლოვანი

num1 = int(input("Enter The Digit:"))
if num1 % 2 == 0:
 print("Your number is even")
else:
    print("Your number is odd")
    #მომხმარებელს შემოვაყვანიეთ რიცხვი და გავიგეთ ლუწია თუ კენტი ეს რიცხვი 


num1 = int(input("Enter Your First Digit: "))
num2 = int(input("Enter Your Second Digit: "))
num3 = int(input("Enter Your Third Digit: "))

if num1 > num2 and num1 > num3:
    print(str(num1) + " is the biggest digit between these three")
elif num2 > num1 and num2 > num3:
    print(str(num2) + " is the biggest digit between these three")
elif num3 > num1 and num3 > num2:
    print(str(num3) + " is the biggest digit between these three")
else:
    print("Two or more numbers are equal, or all three are equal.")
#მომხარებელს შევაყვანიეთ ციფრები და გავაგებიეთ რომელი ციფრი არის ყველაზე დიდი