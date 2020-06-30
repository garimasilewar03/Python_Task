'''Write a program that accepts a string as an input from the user and calculates the number of digits and letters.
     Expected output: consul12
     Letters 6
     Digits 2
'''
input_str = input("Enter a string having letters and digits ")
letters = 0
digits = 0
for i in input_str:
    if i.isdigit():
        digits = digits + 1
    elif i.isalpha():
        letters = letters+1
print(digits, "Digits")
print(letters, "Letters")
