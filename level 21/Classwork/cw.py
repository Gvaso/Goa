#  შექმენით ფუნქციოა სახელად multiply რომელსაც გადაეცემა ერთი პარამეტრი სახელად operation ეს multiply ფუნქცია აბრუნებს 2 * operation(5, 10)

# შემდეგ შექმენით რომელიმე მათემატიკური ფუნქცია add, subtract, divide რომელსაც გადაეცემა 2 პარამეტრი num1, num2

# როდესაც შექმნით ფუნქციას გამოიძახეთ multiply და გადაეცით მეორე ფუნქცია მნიშვნელობად

# საბოლოოდ დაბეჭდეთ multiply ფუნქციიდან დაბრუნებული მნიშნელობა
def multiply(operation):
    return 2 * operation(5, 10)

def add(num1, num2):
    return num1 + num2

result = multiply(add)
print(result)
