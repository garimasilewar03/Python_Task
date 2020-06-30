# If a number is divisible by 3 it should print “Consultadd” as a string
x = input("enter a number ")
if int(x) % 3 == 0:
    print("Consultadd")

# If a number is divisible by 5 it should print “c” as a string
y = input("enter a number ")
if int(y) % 5 == 0:
    print("c")

# If a number is divisible by both 3 and 5 its should print “Consultadd Python Training” as a string.
z = input("enter a number ")
if ((int(z) % 3 == 0) and (int(z) % 5 == 0)):
    print("Consultadd Python Training")
