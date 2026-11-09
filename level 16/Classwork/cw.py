def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def divide(a, b):
    return a / b

def multiply(a, b):
    return a * b


print(add(10, 5))
print(subtract(10, 5))
print(divide(10, 5))
print(multiply(10, 5))
#შევქმენით 4 ფუნქცია რომელიც იყენებს მათემატიკურ ყველა ოპერაცია + - * / 

def check_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


def check_odd(number):
    if number % 2 != 0:
        return True
    else:
        return False


print(check_even(10))
print(check_odd(7))
#შექმენით ორი ფუნქცია, რომლებიც შეამოწმებენ გადაცემული რიცხვი ლუწია თუ კენტი და შესაბამის შემთხვევაში დააბრუნებენ True-ს ან False-ს. გამოიყენეთ if და else პირობები, შემდეგ გამოიძახეთ ორივე ფუნქცია და დაბეჭდეთ შედეგები.