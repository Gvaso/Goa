fruits = ("Apple", "Banana", "Orange", "Kiwi", "Mango", "Strawberry")

print(fruits[0])
print(fruits[2])
print(fruits[-1])

print(len(fruits))
#პროგრამა ქმნის ხილის Tuple-ს რომელშიც მოთავსებულია 6 სხვადასხვა ხილი ბეჭდავს პირველ მესამე და ბოლო ხილს და len ფუნქციის გამოყენებით ითვლის Tuple-ის სრულ სიგრძეს

students = ("Saba", "Nika", "Giorgi", "Luka", "David")

name = input("Enter student name: ")

if name in students:
    print("Student found!")
else:
    print("Student not found!")
#პროგრამა ქმნის მოსწავლეების Tuple-ს მომხმარებელს შეაყვანინებს მოსწავლის სახელს და in ოპერატორის გამოყენებით ამოწმებს არის თუ არა შეყვანილი სახელი Tuple-ში და გამოაქვს შესაბამისი შედეგი

numbers = (10, 20, 30, 20, 40, 20, 50, 60)

print(numbers.count(20))
print(numbers.index(20))
#პროგრამა ქმნის რიცხვების Tuple-ს count მეთოდის გამოყენებით ითვლის რამდენჯერ მეორდება კონკრეტული რიცხვი ხოლო index მეთოდით პოულობს ამ რიცხვის პირველ გამოჩენის ინდექსს
cities = ("Tbilisi", "Batumi", "Kutaisi", "Zugdidi", "Poti", "Rustavi")

print(cities[:3])

print(cities[-3:])

print(cities)
#პროგრამა ქმნის ქალაქების Tuple-ს და Slicing-ის გამოყენებით ბეჭდავს პირველ სამ და ბოლო სამ ქალაქს საბოლოოდ კი გამოაქვს მთლიანი Tuple