students = ["Murat", "Engin", "Süleyman"]

students.append("Ahmet")
students[0] = "Veli"
print(students[3])
students.remove("Engin")
print(students)

# list constructor
cities = list(("Ankara", "İstanbul", "İzmir", "Kocaeli"))
print(cities)
print(len(cities))


# other functions

# print(cities.clear())
print("Ankara sayısı : " + str(cities.count("Ankara")))
print("Ankara indexi : " + str(cities.index("Ankara")))
cities.pop(1)
cities.insert(4, "Samsun")
cities.reverse()
print(cities)

cities2 = cities  # pointer
cities2[0] = "Bolu"
print(cities)  # cities veya cities2 bastırdığımızda aynı çıktıyı alırız
# Arrayler referans tiptir ----> bellekteki yere işaret eder

cities.extend(cities2)
cities.sort()
print(cities)
