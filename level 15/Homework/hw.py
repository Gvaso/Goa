products = ["Apple", "Milk", "Water", "Meat","Cheese"]

product = input("Enter THe Product You Want To Add: ")

products.append(product)

print(products)
#უკვე შედგენილ პროდუქტების სიაში მომხმარებელი შეძლებს დამატებას ნებისმიერი პროდუქტის რაც მას სურს

teachers = ["Teona", "Ana", "Avtandili", "Gela", "Mate"]
teachers.sort()

print(teachers)
#შეყვანილი მასწავლებლების სიაში sort() დახმაერბით მასწავლებლების სახელები ანბანის მიხედვით დაიბეჭდება 

animals = ["Dog", "Cat", "Monkey", "Lion", "Tiger", "Leopard"]

animal_remove = input("Enter The Animal Kind You Want Remove: ")

animals.remove(animal_remove)

print (animals)
#პროგრამაში უკვე შეყვანილი ცხოველების ჯიშები და მომხმარებელს შეუძლია ნებისმიერი ჯიშის ამოშლა ამ სიიდან

digits = [13, 43, 62, 4, 2]
digits.pop(4)
digits.insert(4, 23)
digits.reverse()
print(digits)
#digits ლისტიდან ამოვაგდეს 4 ინდექსი ანუ 2 იანი შემდეგ ჩავანაცვლეთ 23 ით და ბოლოს შევაბრუნეთ reverse() ფუნქციით მთლიანი განლაგება