import sys

list = [45, 'murat', 0, 3, "6"]

for x in list:
    try:
        print("Number: " + str(x))
        result = 1/int(x)
        print("Result: " + str(result))
    except ValueError:
        print(str(x) + " is not a number !!")
    except ZeroDivisionError:
        print("Error dividing by zero for " + str(x) + " !!")
    except:
        print(str(x)+" Could not calculate !!")
        print("System says : " + str(sys.exc_info()[0]))
    finally:
        print("It's over.")
