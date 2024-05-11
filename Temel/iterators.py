cities = ["Ankara","İstanbul","Samsun"]

my_iterator = iter(cities)

print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))

for city in cities:
    print(city)