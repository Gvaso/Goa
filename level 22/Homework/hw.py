phone = {
    "model": "iPhone 15",
    "brand": "Apple",
    "price": 2500,
    "color": "Black",
    "memory": "128GB"
}

new_phone = phone.copy()

new_phone["model"] = "iPhone 16"
new_phone["price"] = 3000

print(phone)
print(new_phone)
# ეს პროგრამა ქმნის ტელეფონის ობიექტს და მის ასლში ცვლის ორ მონაცემს

game = {
    "name": "Roblox",
    "genre": "Adventure",
    "developer": "Roblox Corporation",
    "release_year": 2006,
    "platform": "PC"
}

game.update({
    "multiplayer": True,
    "online": True,
    "rating": 9
})

print(game)
#ეს პროგრამა ქმნის საყვარელი თამაშის ობიექტს და update მეთოდით ამატებს ახალ ინფორმაციას

countries = {
    "Georgia": "Tbilisi",
    "Germany": "Berlin",
    "France": "Paris",
    "Italy": "Rome",
    "Spain": "Madrid"
}

for country, capital in countries.items():
    print(country, "-", capital)

print("Georgia capital:", countries["Georgia"])
#ეს პროგრამა ქმნის ქვეყნების და მათი დედაქალაქების ობიექტს და ტერმინალში გამოაქვს მათი სახელები და დედაქალაქები

scores = {
    "Saba": 95,
    "Nika": 75,
    "Giorgi": 88,
    "Luka": 60,
    "Ana": 92
}

for name, score in scores.items():
    if score > 80:
        print(name)

print("Total students:", len(scores))
# ეს პროგრამა ქმნის მოსწავლეების ქულების ობიექტს და გამოაქვს მხოლოდ იმ მოსწავლეების სახელები რომლებმაც 80 ქულაზე მეტი მიიღეს
