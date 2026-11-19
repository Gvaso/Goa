# მოიყვანეთ შემდეგი ფუნქციების გამოყენების  2-2 მაგალითი: sum, min, max და sorted, ასევე აღწერეთ თითოეული მათგანი დეტალურად.
prices = (15, 25, 10, 50)
total = sum(prices)
print(total)  # prices ში შეყვანილი ციფრები ჯამდება და გამოდის პასუხი 100 
###
scores = [10, 20, 30]
final_score = sum(scores, 100)
print(final_score)  # scores შეყვანილი არის ციფრები და sum ის მეშვეობით ვამატებთ ერთმანეთზე და 100 ემატება რადგან მოცემული არის ფრჩხილებში 
###
temperatures = (18, 12, 24, 9, 15)
lowest = min(temperatures)
print(lowest)  # არსებული ტემპერატურებიდან min ფუნქცია გამოგვიტანს ყველაზე მინიმალურს ანუ 9ს 
###
balances = (-15.5, 0, 42.0, -3.2)
lowest_balance = min(balances)
print(lowest_balance)  #  ბალანსშია მითითებული არის თანხა და ყველაზე დაბალ თანხას გამოიყვანს ანუ -15.5 ს 
###
points = [45, 89, 12, 99, 67]
highest = max(points)
print(highest)  # points ში არის მოცემული ქულები და max ფუნქციის დახმარებით გვანახებს ყველაზე დიდ ქულას ანუ 99ს 
###
temperatures = (-12.5, -3.0, -8.4, -1.2)
warmest = max(temperatures)
print(warmest)  # ტემპერატურაში არის მოცემული გრადუსები და ისევ max  ფუნქცის დახმარებით გავიგებთ თუ რომელი არის ყველაზე მაღალი ამ შემთხვევაში -1.2 არის მაღალი ტემპერატურა 
###
unsorted_tuple = (42, 7, 19, 1, 88)
sorted_list = sorted(unsorted_tuple)
print(sorted_list)  # მოცემულია ციფრები tuple ში და sorted ფუნქციის დახმარებით დალაგდება [1, 7, 19, 42, 88]
###
ratings = (3.5, 4.9, 2.1, 5.0)
top_ratings = sorted(ratings, reverse=True)
print(top_ratings)  # მოცემული არის რეიტინგი და sorted ფუნქცის დახმარებით დალაგდება მაგრამ სწორად არა რადგან reverse გვაქვს მოცემული ამ შეთხვევაში მაღლიდან დაბლა დალაგდება [5.0, 4.9, 3.5, 2.1]
###
mixed_tuple = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)

total_sum = 0

for number in mixed_tuple:
    total_sum += number

print("რიცხვების ჯამი:", total_sum)  # ქმნის tuple-ს 0-დან 20-მდე რიცხვებით for ციკლით კრებს მათ ჯამს და ბეჭდავს შედეგს ანუ შედეგი გამოვა 210
###
my_tuple = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)

temp_list = list(my_tuple)

temp_list.append("Saba Gvaso")


my_tuple = tuple(temp_list)

print(my_tuple) # ქმნის tuple-ს გადააქცევს list-ად ამატებს "Saba GVASO"-ს, შემდეგ ისევ tuple-ად აქცევს და ბეჭდავს პასუხს : (10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 'Saba Gvaso')

