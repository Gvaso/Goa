num = int(input("Enter Your Digit:"))

if num > 0 : 
    print ("Positive")
elif num == 0 :
    print ("Your digit is equal to 0")
else:
    print("Negative")
    # მომხმარებელს შემოყავს რიცხვი და იგებს ის უარყოფითია ,დადებითია თუ ტოლია 0 ის

point = int(input("Enter Your Points:"))

if point > 100 or point < 0:
    print ("Thats Not Even A Point Anymore")

elif point >= 90:
 print("Your point is A")

elif point >=101:
    print("Thats Not Even A Point Anymore")

elif point >=80:
 print ("Your point is B")

elif point >=70:
    print("Your point is C")

elif point >=60:
    print("Your point is D")

else:
    print("Your point is F")
    
   # მომხმარებელს შემოვაყვანინეთ ქულა და გავაგებიეთ მისი შეფასება (A,B,C,D,F) და გავაგებიეთ 0ზე ნაკლები ქულა ან 100ზე მეტი ქულა საერთოდ ქულა არის თუ არა 

secret_num = 15
num1 = int(input("Guess The Digit:"))

while num1 != secret_num :
    print("You Guessed It Wrong")
    num1 = int(input("Guess The Digit:"))

    if num1 == secret_num:
        print("You Guessed The Number")      

        #მომხარებელს შეყავს რიცხვი იქამდე სანამ ის მას არ გამოიცნობს 

digit1 = float(input("Enter Your First Digit:"))     
digit2 = float(input("Enter Your Second Digit:")) 
enter_operator = input("Enter The Operator: + , - , *, / :")

if enter_operator == "+":
 print (digit1 + digit2)

elif enter_operator == "-":
 print (digit1 - digit2)

elif enter_operator == "*":
 print (digit1 * digit2)

else:
 print (digit1 / digit2)
 
 #მომხმარებელმა შემოიყვანა 2 ნებისმიერი ციფრი და ეს ციფრი ოპერატორის დახმარების გაიყო,მიემატა,გამოაკლდა ან კიდე გამრავლდა


 
