num = int(input("Enter a number : "))

count = 1

if num < 0:
    print("Negative numbers are not calculated factorial.")
elif num == 0:
    print("Result is 1.")
else:
    for i in range(1, num+1):
        count = count * i
    print("Result : ", count)
