age = int(input("Enter Your Age:"))
if age < 13:
    print ("Your Child")
elif age >= 13 and age <17:
    print ("Your Teenager")
else:
    print ("Your Adult")
# #     #მომხმარებელს შემოვაყვანინეთ ასაკი და გავაგებინეთ ის Child , Teenger იყო თუ Adult

N = int(input("Enter The Positive Number:"))
for num in range (1, N+1):
    if num % 2 ==0:
        print(num, "Even")
    else:
        print(num, "Odd")
#მომხმარებელს შემოვაყვანინეთ ციფრი და მაგ ციფრის ჩათვლის ვანახეთ მიმდინარე ციფრებ ლუწია და კენტი
correct_password = "python123"
input_password = ""

while input_password != correct_password:
    input_password = input("Please enter correct password: ")

    if input_password == correct_password:
        print("✅ Access granted!")
    else:
        print("❌ Try again!")
#     #მომხმარებელს შემოვაყვანინეთ პაროლი და იქამდე შემოიყვანს სანამ ეს პაროლი სწორი არ იქნება 
##################################

correct_password = "python123"
input_password = ""
mistakes = 0

while input_password != correct_password and mistakes < 3:
    input_password = input("Please enter correct password: ")

    if input_password != correct_password:
        mistakes = mistakes + 1
        print("შეცდომა:", mistakes)

if mistakes == 3:
    print("პაროლი 3-ჯერ არასწორად შეიყვანეთ!")
else:
    print("პაროლი სწორია!")
#მომხარებელმა შემოიყვანა პაროლი და თუ 3 ჯერ არასწორად ჩაწერა გააგდებს და თუ სწორად მაშინ შეუშვებს 
many_student = int(input("How Many Students Are In Class : "))

passed = 0
failed = 0 

for i in range (many_student):
    score = int(input("Enter Student Score: "))

    if score <0 or score >100:
        print("Invalid Score")
    elif score >=90:
        print("Grade: A")
        passed = passed + 1
    elif score >=80:
        print ("Grade :B")
        passed = passed + 1
    elif score >=70:
        print ("Grade :C")
        passed = passed + 1
    elif score >=60:
          print ("Grade :D")
          passed = passed + 1
    else:
        print ("Grade: F")
        failed = failed + 1

print("Total Passed:",passed)
print("Total Failed:", failed)
#მომხმარებელს შემოვავანიეთ სტუდენტების რაოდენობა ნიშნები ამთი და ვინ გადავიდა და ვინ ვერ მოახერხა გადასვლა 
balance = 500.0 
while True:
    enter_amount = float(input("Enter The Amount You Want To Withdraw :"))

    if enter_amount ==0:
        print ("ATM Session Ended.")
        break
    elif enter_amount <0:
        print("Invalid Amount!")
    else:
        balance = balance - enter_amount
        print("Withdrawal Successful")
        print("Remaining Balance:", balance, "₾")
        #მომხარებელმა მიუთითა რამდენის გამოტანა უნდა ბალანსიდან და ის გამოიტანს მისივე ანგარიშიდან 