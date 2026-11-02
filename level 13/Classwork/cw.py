h = int(input("Enter The H : "))
for i in range (h, 0, -1):
    for j in range(1, i + 1):
        print(j, end ="")
        print()
# #მომხმარებელმა შემოიყვანა ციფრი და პროგრამამ დაიწყო ათვლა მაგ : 1,2,3,4,5 | 1,2,3,4
number = int(input("შეიყვანე რიცხვი: "))

for i in range(1, number + 1):
    print(" " * (number - i) * 2, end="")

    for j in range(1, i + 1):
        print(j, end=" ")

    for k in range(i - 1, 0, -1):
        print(k, end=" ")

    print()
#მომხარებელმა შემოიყვანა ციფრი და მიმდებარე ციფრები ჩამოიშლება პირამიდივით
h = int(input("Enter height: "))

for i in range(1, h + 1):
    for j in range(1, i + 1):
        if j == 1 or j == i or i == h:
            print("*", end="")
        else:
            print(" ", end="")
    print()
#მომხმარებელს შემოყავს სიმაღლე და იმ სიმაღლის hollow გამოისახება ეკრანზე ფიფქებით
h = int(input("Enter height: "))

for i in range(1, h + 1):
    for j in range(h - i):
        print(" ", end="")

    for j in range(2 * i - 1):
        print("*", end="")

    print()
#მომხმარებელს შემოვაყვანინეთ ციფრი და მაგ ციფრის მიხედვით დაიბეჭდა (*)ების პირამიდა 
    