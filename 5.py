# Write a program in Python which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200.
# print(*[i for i in range(2000, 3201) if not(i%7) and i%5])

for i in range(2000,3201):
    if i % 7 == 0 and i % 5!=0:
        print(i)
