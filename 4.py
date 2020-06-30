'''If a user enters a negative number just break the loop and print “It’s Over”
If a user enters a positive number just continue in the loop and print “Good Going”
'''
age = int(input("enter a positive number "))
if age < 0:
    print("its over")
    break
else:
    print("you have enteredd a positive number")
