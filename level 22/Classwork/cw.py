# ეს პროგრამა ქმნის person ობიექტს რომელშიც ინახავს ადამიანის შესახებ 5 სხვადასხვა ინფორმაციას შემდეგ ტერმინალში გამოაქვს მთლიანი ობიექტი მისი ყველა გასაღები ყველა მნიშვნელობა და ყველა გასაღები შესაბამის მნიშვნელობასთან ერთად

person = {
    "name": "Saba",
    "age": 16,
    "city": "Poti",
    "hobby": "Programming",
    "favorite_language": "English"
}

print(person)
print(person.keys())
print(person.values())
print(person.items())


# ეს პროგრამა ქმნის book ობიექტს რომელშიც ინახავს წიგნის შესახებ 5 სხვადასხვა ინფორმაციას შემდეგ ცვლის ორ კუთვნილებას ამატებს ორ ახალ კუთვნილებას შლის ერთ კუთვნილებას და ბოლოს ტერმინალში გამოაქვს განახლებული ობიექტი

book = {
    "name": "Harry Potter",
    "author": "J.K. Rowling",
    "pages": 350,
    "year": 1997,
    "genre": "Fantasy"
}

book["name"] = "The Hobbit"
book["pages"] = 400

book["publisher"] = "George Allen & Unwin"
book["language"] = "English"

del book["year"]

print(book)