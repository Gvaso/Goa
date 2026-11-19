fruits = {"ვაშლი", "ბანანი", "მსხალი", "ატამი", "საზამთრო", "მარწყვი"}

new_fruit = input("შეიყვანე ახალი ხილი: ")

fruits.add(new_fruit)

print(fruits)
#პროგრამა ქმნის 6 ხილის Set-ს მომხმარებელს შეაყვანინებს ახალ ხილს ამატებს მას Set-ში და ბეჭდავს განახლებულ შედეგს

students = {"საბა", "გიორგი", "ნიკა", "ლუკა", "დავითი"}

name = input("შეიყვანე მოსწავლის სახელი: ")

if name in students:
    print("მოსწავლე არსებობს Set-ში")
else:
    print("მოსწავლე არ არსებობს Set-ში")
#პროგრამა ქმნის 5 მოსწავლის Set-ს მომხმარებელს შეაყვანინებს სახელს და ამოწმებს არსებობს თუ არა ეს მოსწავლე Set-ში


numbers = {10, 20, 30, 40, 50, 60, 70}

number = int(input("შეიყვანე რიცხვი: "))

if number in numbers:
    print("რიცხვი არსებობს Set-ში")
    numbers.remove(number)
else:
    print("რიცხვი არ არსებობს Set-ში")

print("განახლებული Set:", numbers)
#პროგრამა ქმნის 7 რიცხვის Set-ს მომხმარებელს შეაყვანინებს რიცხვს ამოწმებს მის არსებობას და თუ არსებობს შლის მას Set-იდან

animals = {"ძაღლი", "კატა", "ლომი", "ვეფხვი", "დათვი", "მგელი"}

print("ცხოველების რაოდენობა:", len(animals))

new_animal = input("შეიყვანე ახალი ცხოველი: ")

animals.add(new_animal)

print("განახლებული Set:", animals)
print("ახალი რაოდენობა:", len(animals))
#პროგრამა ქმნის 6 ცხოველის Set-ს ითვლის მათ რაოდენობას ამატებს ახალ ცხოველს და ბეჭდავს განახლებულ Set-ს და მის რაოდენობას

colors = {"წითელი", "ლურჯი", "მწვანე", "ყვითელი", "შავი"}

color1 = input("შეიყვანე პირველი ფერი: ")
color2 = input("შეიყვანე მეორე ფერი: ")

print(color1, color1 in colors)
print(color2, color2 in colors)
#პროგრამა ქმნის 5 ფერის Set-ს მომხმარებელს შეაყვანინებს ორ ფერს და ამოწმებს ორივე ფერის არსებობას Set-ში

# Define a function that removes duplicates from an array of non negative numbers and returns it as a result.

# The order of the sequence has to stay the same.
def distinct(seq):
    result = []
    for num in seq:
        if num not in result:
            result.append(num)
    return result

# You will be given an array a and a value x. All you need to do is check whether the provided array contains the value.

# a can contain numbers or strings. x can be either.

# Return true if the array contains the value, false if not.
def check(seq, elem):
    return elem in seq

# Can you find the needle in the haystack?

# Write a function findNeedle() that takes an array full of junk but containing one "needle"

# After your function finds the needle it should return a message (as a string) that says:

# "found the needle at position " plus the index it found the needle, so:
def find_needle(haystack):
    return "found the needle at position " + str(haystack.index("needle"))

# Write a function that takes an array of numbers and returns the sum of the numbers. The numbers can be negative. If the array is empty, return 0.

# Examples
# Input: [1, 5.2, 4, 0, -1]
# Output: 9.2

# Input: [-2.398]
# Output: -2.398

# Input: []
# Output: 0
def sum_array(a):
    total = 0
    for num in a:
        total += num
    return total