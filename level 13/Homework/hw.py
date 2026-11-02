number = 123675312354
digit = 2

count = 0

while number > 0:
    last_digit = number % 10

    if last_digit == digit:
        count += 1

    number //= 10

print(count)
# 1) პროგრამა ითვლის რამდენჯერ გვხვდება მითითებული ერთი ციფრი დიდ რიცხვში.
number = 360
divisor = 2

while number > 1:
    if number % divisor == 0:
        print(divisor, end=" ")
        number //= divisor
    else:
        divisor += 1
# 2) პროგრამა მოცემულ რიცხვს შლის მარტივ მამრავლებად და ბეჭდავს მათ ზრდადობით.

limit = 100

a = 0
b = 1

while a < limit:
    print(a, end=" ")

    a, b = b, a + b
# 3) პროგრამა ბეჭდავს ფიბონაჩის მიმდევრობის ყველა რიცხვს რომელიც მითითებულ ზღვარზე ნაკლებია.

numbers = [4, 17, 2, 9, 31, 6]

largest = numbers[0]
smallest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

    if num < smallest:
        smallest = num

print("უდიდესი:", largest)
print("უმცირესი:", smallest)
# 4) პროგრამა მასივში პოულობს ყველაზე დიდ და ყველაზე პატარა რიცხვს და ბეჭდავს მათ.

numbers = [1, 2, 3, 4, 5]

left = 0
right = len(numbers) - 1

while left < right:
    numbers[left], numbers[right] = numbers[right], numbers[left]

    left += 1
    right -= 1

print(numbers)
# 5) პროგრამა აბრუნებს მასივის ელემენტებს საპირისპირო თანმიმდევრობით ისე რომ ახალ მასივს არ ქმნის.