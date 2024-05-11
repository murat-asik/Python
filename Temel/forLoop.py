cities = ["Ankara","İstanbul","izmir"]

for city in cities:
    if city == "İstanbul":
        continue #sadece istanbulu yazmaz 
        #break döngüyü tamamen bitirir
    print("Code for " + city + " : " + city[0:3])
    print("*******")


for x in range(2,100,2):
    print(x)