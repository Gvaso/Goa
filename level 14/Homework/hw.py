num = int(input("შეიყვანე დადებითი რიცხვი: "))

count = 0
total = 0
even = 0
odd = 0

while num > 0:
    digit = num % 10

    count += 1
    total += digit

    if digit % 2 == 0:
        even += 1
    else:
        odd += 1

    num = num // 10

print("ციფრების რაოდენობა:", count)
print("ციფრების ჯამი:", total)
print("ლუწი ციფრები:", even)
print("კენტი ციფრები:", odd)

if total % 2 == 0:
    print("ციფრების ჯამი ლუწია")
else:
    print("ციფრების ჯამი კენტია")
#მომხმარებელს შემოყავს რიცხვი და პროგრამა გაგების ციფრების რაოდენობას, ჯამს, ლუწია თუ კენტი

numbers = []

for i in range(15):
    num = int(input("შეიყვანე რიცხვი: "))
    numbers.append(num)

biggest = numbers[0]
smallest = numbers[0]

positive = 0
negative = 0
zero = 0
total = 0

for num in numbers:
    if num > biggest:
        biggest = num

    if num < smallest:
        smallest = num

    if num > 0:
        positive += 1
    elif num < 0:
        negative += 1
    else:
        zero += 1

    total += num

average = total / 15

print("ყველაზე დიდი:", biggest)
print("ყველაზე პატარა:", smallest)
print("დადებითი რიცხვები:", positive)
print("უარყოფითი რიცხვები:", negative)
print("ნულები:", zero)
print("საშუალო არითმეტიკული:", average)

if average > 0:
    print("საშუალო დადებითია")
elif average < 0:
    print("საშუალო უარყოფითია")
else:
    print("საშუალო ნულის ტოლია")
# მომხმარებელს შემოაქვს 15 სხვადასხვა რიცხვი პროგრამა პოულობს მათ შორის ყველაზე დიდ და ყველაზე პატარა რიცხვს ითვლის დადებითი უარყოფითი და ნულის ტოლი რიცხვების რაოდენობას ასევე გამოთვლის საშუალო არითმეტიკულს და ადგენს საშუალო დადებითია უარყოფითი თუ ნულის ტოლი

secret = 37

for i in range(7):
    guess = int(input("გამოიცანი საიდუმლო რიცხვი: "))

    if guess == secret:
        print("გილოცავ! სწორად გამოიცანი!")
        break

    elif guess < secret:
        print("საიდუმლო რიცხვი უფრო დიდია")

    else:
        print("საიდუმლო რიცხვი უფრო პატარაა")

else:
    print("თამაში დასრულდა!")
    print("სწორი პასუხი იყო:", secret)
# პროგრამაში წინასწარ განსაზღვრულია საიდუმლო რიცხვი 37 მომხმარებელს აქვს 7 მცდელობა მის გამოსაცნობად ყოველი მცდელობის შემდეგ პროგრამა ეუბნება საიდუმლო რიცხვი უფრო დიდია თუ პატარა სწორი პასუხის შემთხვევაში თამაში ჩერდება და გამოაქვს წარმატების შეტყობინება ხოლო 7 მცდელობის ამოწურვისას აჩვენებს სწორ პასუხს

start = int(input("შეიყვანე საწყისი რიცხვი: "))
end = int(input("შეიყვანე საბოლოო რიცხვი: "))

fizz = 0
buzz = 0
fizzbuzz = 0

for i in range(start, end + 1):

    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
        fizzbuzz += 1

    elif i % 3 == 0:
        print("Fizz")
        fizz += 1

    elif i % 5 == 0:
        print("Buzz")
        buzz += 1

    else:
        print(i)

print("Fizz რაოდენობა:", fizz)
print("Buzz რაოდენობა:", buzz)
print("FizzBuzz რაოდენობა:", fizzbuzz)
# მომხმარებელს შემოაქვს საწყისი და საბოლოო რიცხვები პროგრამა ამ დიაპაზონში ამოწმებს ყველა მთელ რიცხვს თუ რიცხვი იყოფა 3-ზე და 5-ზე გამოაქვს FizzBuzz თუ მხოლოდ 3-ზე იყოფა გამოაქვს Fizz თუ მხოლოდ 5-ზე იყოფა გამოაქვს Buzz სხვა შემთხვევაში გამოაქვს თვითონ რიცხვი და ბოლოს ითვლის თითოეული მათგანის რაოდენობას