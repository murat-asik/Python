num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the secaond number: "))
num3 = int(input("Enter the third number: "))
 
if (num1 > num2) & (num1 > num3):
    enBuyuk = num1
elif (num2 > num1) & (num2 > num3):
    enBuyuk = num2
else:
    enBuyuk = num3

print("The biggest number is :",enBuyuk)