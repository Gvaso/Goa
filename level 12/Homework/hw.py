
digit =  [12,34,53,32,10]
enter_digit = int(input("Enter The Digit : "))
if enter_digit in digit:
    print("The number you entered matches one of the numbers.")
else:
    print("It does not match any of them")

print (digit[0])
print (digit[2])

for digits in digit:
    print(digits)
    #მომხმარებელს შემოყავს რიცხვი და პროგრამარა აგებინებს ემთხვევა თუ არა რომელიმე რიცხვს რომელიც List შია მოცემული  და ასევე პროგრამა შლის ყველა არსებულ რიცხვს და გამოსახავს ტერმინალში

student_score = [34,43,67,97,10]   
failed = 0
passed = 0

for score in student_score:
 if score < 50 :
    failed += 1
    print ("Failed:", score)
 else:
        passed += 1
        print("Passed:", score)

print("Total Failed:", failed)
print("Total Passed:", passed)
#ითვლის თუ რამდენი მოსწავლე passed the test and failed the test
digit_1 = []
negative = 0
positive = 0
equal = 0 

for i in range(7):
    digit_2 = int(input("Enter The Digit: "))
    digit_1.append(digit_2)

print(digit_1)

largest = digit_1[0]

for digit in digit_1:
    print(digit)

    if digit < 0:
        negative += 1
    elif digit > 0:
        positive += 1
    else:
        equal += 1

    if digit > largest:
        largest = digit

print("Positive's:", positive)
print("Negative's:", negative)
print("Equal To Zero:", equal)
print("Maximum Number:", largest)
#მომხარებელმა შემოიყვანა  7 ციფრი და გავაებინეთ რომელია პოზიტიური უარყოფითი და 0 ტოლი და გავაგებიეთ რომელია დიდი ციფრი 


movies = ["Avatar", "Titanic", "Interstellar"]

for movie in movies:
    print(movie)

new_movie = input("Enter a new movie: ")
movies.append(new_movie)

print("Updated movie list:", movies)


index = int(input("Enter movie index: "))

if index >= 0 and index < len(movies):
    print("Your movie:", movies[index])
else:
    print("Invalid index!")
#უკვე ლისტში შეყვანილ ფილმებს მომხმარებელს შეეძლუია რომ ჩააამატოს ამ ლისტში კიდე მისი სსურველი ფილმი ინდექსის დახმარებით

