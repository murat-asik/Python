class Math:
    def __init__(self):
        print("It's work.")

    def addition(self, num1, num2):
        return num1 + num2

    def subtraction(self, num1, num2):
        return num1 - num2

    def multiplication(self, num1, num2):
        return num1 * num2

    def division(self, num1, num2):
        return num1 / num2


math = Math()
math2 = Math()

print("Result : " + str(math.addition(2, 78)))
print("Result : " + str(math.subtraction(48, 21)))
print("Result : " + str(math.multiplication(5, 24)))
print("Result : " + str(math.division(49, 6)))

class Person:
    def __init__(self,firstName,lastName,age):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age

person1 = Person("Murat","Aşık",20)
print(person1.firstName,person1.lastName)


class Worker(Person): 
    def __init__(self,salary):
        self.salary = salary

    
class Customer(Person): 
    def __init__(self,creditCardNumber):
        self.creditCardNumber = creditCardNumber

ahmet = Worker()
ahmet.age
        
mehmet = Customer()   
mehmet.creditCardNumber   
























