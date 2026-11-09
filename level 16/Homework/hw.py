# def check_number(number):
#     if number > 0:
#         return "Positive"
#     elif number < 0:
#         return "Negative"
#     else:
#         return "Zero"



# user_input = float(input("შეიყვანეთ რიცხვი: "))


# print(check_number(user_input))
#მომხმარებელს შემოყავს რიცხვი და შემდეგ უბრუნებს პროგრამა პასუხს ეს რიცხვი დადებითია თუ უარყოფითი ან ნულის ტოლი 

def calculate_sum(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


print(calculate_sum(5))  
#მითითებულ რიცხვს 5 დაემატება 1+2+3+4+5=15 თუ მიუთითებენ 6 იქნება 1+2+3+4+5+6 = 21
def calculator(num1, num2, operation):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        if num2 == 0:
            return "Cannot divide by zero"
        return num1 / num2
    else:
        return "Invalid Operation"


print(calculator(10, 5, "+"))   # დაბეჭდავს 15
print(calculator(10, 0, "/"))   # დაბეჭდავს "Cannot divide by zero"
print(calculator(10, 5, "-"))   # დაბეჭდავს 5
print(calculator(10, 5, "*"))   # დაბეჭდავს 50 
#მითითებულ ციფრს print ში 10,5 1 გადამატებს 2 გაყოფს 3 გამოაკლებს 4 გადამრავლებს
def password_checker(password):
    has_letter = any(char.isalpha() for char in password)
    has_digit = any(char.isdigit() for char in password)
    
    if len(password) > 8 and has_letter and has_digit:
        return True
    return False


print(password_checker("myPassword1"))  # True (სიგრძე > 8, შეიცავს ასოს და ციფრს)
print(password_checker("pass1"))        # False (სიგრძე არ არის 8-ზე მეტი)
print(password_checker("123456789"))    # False (არ შეიცავს ასოს)
#ამოწმებს პაროლს: პაროლის სიგრძე 8 სიმბოლოზე მეტია, პაროლში არის მინიმუმ 1 ასო,პაროლში არის მინიმუმ 1 რიცხვი.