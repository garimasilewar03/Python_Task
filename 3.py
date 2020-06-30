age = int(input("enter a positive number "))
if age >=11:
    print("You are eligible to see the football match")
    if age <=20 or age >=60:
        print("TIcket price is $12")
    else:
        print("Ticket price is $20")
else:
    print("You are not eligible to buy the ticket")