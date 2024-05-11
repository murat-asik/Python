try:
    number = int(input("Enter a number : "))
except ValueError:
    print("Type mismatch. Please enter number!!")
except ZeroDivisionError:
    print("Denominator cannot be zero!!")
except:
    print("There's a mistake!!")

print("It's over.") 