print("Welcome to Calculator")

num1 = float(input("Enter first number ="))
num2 = float(input("Enter second number ="))

print("Print 1 for addition = \n Print 2 for subtraction = \n Press 3 for multiplication =\n Press 4 for division =")
choice = int(input("Choose number between 1-4 ="))

if choice == 1:
    print (num1 + num2)
elif choice == 2:
    print(num1 - num2)
elif choice == 3:
    print(num1 * num2)
elif choice == 4:
    print(num1 / num2)
else :
    print("Invalid input")