def sayHi(name = "Visitor"):
    print("Hello " + name)

sayHi("Murat")
sayHi()

def sayHi2(name = "Visitor", lastName = "Friend"):
    print("Hello " + name + " " + lastName)

sayHi2()
sayHi2("Murat","Aşık") 

def calculateRightTriangleArea(a,b):
    return a*b/2

area = calculateRightTriangleArea(4,5)

print(area)

calculateRightTriangleArea2 = lambda a,b : a*b/2

print(calculateRightTriangleArea2(48,25))

print(type(calculateRightTriangleArea2))


