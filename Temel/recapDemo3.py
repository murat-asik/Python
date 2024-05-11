num = int(input("Enter a number: "))
count = True
for x in range(2, num):
    if (num % x) == 0:
        count = False
        break
if count == True:
    print("This number is the prime number.")
else:
    print("This number is not a prime number.")
