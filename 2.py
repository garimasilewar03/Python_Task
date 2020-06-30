'''Ask the user to choose the following option first:
If User Enter 1 - Addition 
If User Enter 2 - Subtraction
If User Enter 3 - Division
If USer Enter 4 - Multiplication
If User Enter 5 - Average
Ask the user to enter the 2 numbers in a variable for first and second for the first 4 options mentioned above.
Ask the user to enter two more numbers as first1 and second2 for calculating the average as soon as the user chooses an option 5.
In the end, if the answer of any operation is Negative print a statement saying “Zsa”
'''

first = int(input("Enter first number "))
second = int(input("Enter second number "))
op = int(input("Enter the operator you want to perform on these two numbers, 1=add , 2=sub , 3=div , 4=mult, 5=avg "))

result = 0
if op == 1:
    result = first + second
    print(result)
elif op == 2:
    result = first - second
    print(result)
elif op == 3:
    result = first/second
    print(result)
elif op == 4:
    result = first*second
    print(result)
elif op == 5:
    first1 = int(input("enter third number "))
    second2 = int(input("enter fourth number "))
    result = (first + second + first1 + second2) / 4
    print(result)
    
if result < 0:
    print("zsa")