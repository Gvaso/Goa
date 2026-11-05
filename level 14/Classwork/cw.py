number = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

total = 0 

for num in number:
    total += num **2

    print("კვადრატის ჯამი:", total)
#პროგრამაში უკვე შეყვანილი ციფრები გარდაიქმა კვადრატებად და ტერმინალში გადმოიცა მათი კვადრატული ჯამი

numbers = [2,5,8,3,10,7,12,4,9,6,15,11,14,13,16,18,20,17,19,21]

even_sum = 0 
odd_sum = 0 

for num in numbers:
    if num % 2 ==0:
        even_sum += num
    else:
        odd_sum += num
print("ლუწი რიცხვების ჯამი:", even_sum)
print("კენტი რიცხევის ჯამი:", odd_sum)
#პროგრამაში უკვე შეყვანილი რიცხვები გადაიყო ლუწი ერთ მხარეს და კენტრი მეორე მხარე შემდეგ პროგრამამ დაჯამა ლუწი რიცხვები და კენტი რიცხვები და შედეგი გამოიღო ტერმინალში

numbers = []
n= int(input("შეიყვანეთ რციხვების რაოდენობა:"))

for i in range(n):
    num= int(input("შეიყვანეთ რიცხვი: "))
    numbers.append(num)

numbers.sort()

print("დაალაგეთ სია:", numbers)

maximum = numbers[0]
minimum = numbers [0]

for num in numbers:
    if num > maximum:
        maximum = num

        if num < minimum:
            minimum = num

print ("მაქსიმალური რიცხვი:", maximum)
print ("მინიმალური რიცხვი:", minimum)
#მომხმარებელს შემოაქვს ციფრების რაოდენობა შემდეგ ეს რაოდენობა for  ციკლის საშვალების ვიგებთ რომელია პატარა და დიდი და ალაგებს ზრდადობის მიხედვით

grades = []

n = int(input("შეიყვანეთ მოსწავლეების რაოდენობა: "))

for i in range(n):
    grade = int(input(f"შეიყვანეთ {i + 1}-ე მოსწავლის ქულა (0-100): "))

    while grade < 0 or grade > 100:
        print("შეცდომა! ქულა უნდა იყოს 0-დან 100-მდე.")
        grade = int(input("შეიყვანეთ ქულა თავიდან: "))

    grades.append(grade)

total = 0
maximum = grades[0]
minimum = grades[0]
passed = 0
failed = 0

for grade in grades:
    total += grade

    if grade > maximum:
        maximum = grade

    if grade < minimum:
        minimum = grade

    if grade > 60:
        passed += 1
    elif grade < 60:
        failed += 1

average = total / n

print("საშუალო ქულა:", average)
print("მაქსიმალური ქულა:", maximum)
print("მინიმალური ქულა:", minimum)
print("ჩააბარა:", passed)
print("ვერ ჩააბარა:", failed)
#მომხმარებელმა შემოიყვანა პროგრამაში მოსწავლეების რაოდენობა და მათი ქულები და პროგრამამ უთხრა მასწავლებელს თუ რამდენმა ჩააბარა და რამდენმა ვეერ ჩააბარა 