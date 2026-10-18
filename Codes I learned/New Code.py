Num1 = 25
Num2 = 5
print(Num1 + Num2)
print(Num1 - Num2)
print(Num1 * Num2)
print(Num1 / Num2)
print(Num1 // Num2)
print(Num1 % Num2)

# Calculator thing 

print(type(30))

#integer - in - (5,10 ,20 ,30 ,50
#float (5.4 , 10.3 , -6.1)
#string (Text)

#------------------------------------- 1  input /output
user_name = input ("Enter Your Name : ")
user_age = input ("Enter Your Age:")

print ("User Name is" + user_name )
print ("User Age Is" + user_age )
#--------------------------------------2 
user_name = input ("Enter Your Name : ")
user_surname = input ("Enter Your Fullname :")
user_age = input ("Enter Your Age : ")

print ("Hello" + user_name )
print ("User SurName Is " + user_surname )
print ("User Fullname Is " + user_name + user_surname)
print ("User's Age Is" + user_age)
#------------------------------------------3 
product = input("Enter Product Name :")
product_price = float(input("Enter The Product Price:"))
product_many = float(input("Enter How Many :"))
# დასამატებელია print ში str 
print("Your Product Is:"+ " "+ product)
print("Your Product's Price Is:" + " " + str(product_price))
print("You Have :"+" " + product + " " + str(product_many))
print("Your FUll Price Is " + " "+ str(product_price * product_many))
#--------------------------------------------------------------------
#--------------------------------------------------------------------
product = input("Enter Product Name :")
product_price = float(input("Enter The Product Price:"))
product_many = float(input("Enter How Many :"))
#მომხარებელმა შეიყვანა პროდუქტის სახელი , ფასი , რაოდენობა და გადამრავლდა ფასი რაოდენობაზე და გამოვიდა შედეგი
print("Your Product Is:"+ " "+ product)
print("Your Product's Price Is:" + " " + str(product_price))
print("You Have :"+" " + product + " " + str(product_many))
print("Your FUll Price Is " + " "+ str(product_price * product_many))
# # #----------------------------------------------------------------
name = input("Enter Your Name:")
Point = int(input("Enter Your Point's In Math :"))
Point2 = int(input("Enter Your Point's In English :"))
Point3 = int(input("Enter Your Point's In History : "))
print("Your Full Grade Is : " + " " + str(Point + Point2 +Point3))
Average_Points = int(input("Enter The Total Points : "))

print("Your Name Is :" + " " + name)
print("Your Math Grade Is :" + " " + str(Point))
print("Your English Grade Is :" + " " + str(Point2))
print("Your History Grade Is :" + " " + str(Point3))
print("Your Avarage Grade Is :" + " "+ str(Average_Points //3))
#-----------------------------------------------------------------------------------