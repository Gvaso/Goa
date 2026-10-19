number = int(input("Enter a number: "))
sum = 0 

for i in range(number + 1):
    sum = sum + i
print(sum)
#შევაყვანინეთ რიცხვი და გამოთვალეთ 0 დან მოცემულ რიცხვამდე რიცხვების ჯამი

number = int(input("Enter a number: "))
total = 0

for i in range(0, number + 1, 2):
    total += i

print(total) 
#შევაყვანინეთ რიცხვი და გამოთვალეთ 0 დან მოცემულ რიცხვამდე ლუწი რიცხვების ჯამი