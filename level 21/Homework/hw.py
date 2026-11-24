# ეს პროგრამა ქმნის my_map() ფუნქციას რომელიც სიის თითოეულ რიცხვზე იყენებს გადაცემულ ფუნქციას ამოწმებს რიცხვების 2-ზე გამრავლებასა და კვადრატში აყვანას

def my_map(numbers, func):
    new_list = []

    for num in numbers:
        new_list.append(func(num))

    return new_list


def multiply(num):
    return num * 2


def square(num):
    return num ** 2


numbers = [2, 4, 6, 8, 10]

print(my_map(numbers, multiply))
print(my_map(numbers, square))
# ეს პროგრამა ქმნის my_filter() ფუნქციას რომელიც სიიდან არჩევს მხოლოდ იმ რიცხვებს რომლებიც მოცემულ პირობას აკმაყოფილებს ტოვებს ლუწ და 10-ზე მეტ რიცხვებს

def my_filter(numbers, func):
    new_list = []

    for num in numbers:
        if func(num):
            new_list.append(num)

    return new_list


def even(num):
    return num % 2 == 0


def greater(num):
    return num > 10


numbers = [2, 5, 8, 12, 15, 20]

print(my_filter(numbers, even))
print(my_filter(numbers, greater))
# ეს პროგრამა Lambda ფუნქციის გამოყენებით მომხმარებლის მიერ შეყვანილ ორ რიცხვს კრებს და ბეჭდავს მათ ჯამს

add = lambda a, b: a + b

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print(add(num1, num2))
# ეს პროგრამა Lambda ფუნქციის გამოყენებით ითვლის სიაში არსებული თითოეული სიტყვის სიმბოლოების რაოდენობას და ბეჭდავს შედეგს

word_length = lambda word: len(word)

words = ["Apple", "Banana", "Python", "Computer", "School"]

for word in words:
    print(word, word_length(word))
# ეს პროგრამა მომხმარებელს სთხოვს 5 რიცხვის შეყვანას და Lambda ფუნქციის გამოყენებით ბეჭდავს თითოეული რიცხვის კვადრატს

square = lambda num: num ** 2

for i in range(5):
    num = int(input("Enter a number: "))
    print(square(num))
# ეს პროგრამა მომხმარებელს სთხოვს ორი რიცხვის შეყვანას და Lambda ფუნქციის გამოყენებით პოულობს და ბეჭდავს მათ შორის დიდ რიცხვს

bigger = lambda a, b: a if a > b else b

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print(bigger(num1, num2))
# ეს პროგრამა Lambda ფუნქციის გამოყენებით პოულობს და ბეჭდავს სიაში არსებული თითოეული სიტყვის პირველ სიმბოლოს

first_letter = lambda word: word[0]

words = ["Apple", "Banana", "Python", "School", "Computer"]

for word in words:
    print(first_letter(word))