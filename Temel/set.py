studentsSet = {"Murat", "Umut", "Emre", "Enes", "Bedo"}
# sstudentsSet2 = set("","","","") #Bir başka set tanımlama yöntemi
# set veri yapısında index olmadığı için çıktı sırası değişiklik gösterir
print(studentsSet)

for student in studentsSet:
    print(student)

# print("murat" in studentsSet) #----> False dönecektir çünkü büyük-küçük harf duyarlılığı vardır
print("Murat" in studentsSet)

if "Murat" in studentsSet:
    print("İs on the list.")

studentsSet.add("Ali")
print(studentsSet)

# update -----> bir datayı değil var olan bir seti update eder
studentsSet.update(["Mert", "Ahmet", "Ayşe"])
print(studentsSet)

print(len(studentsSet))

studentsSet.remove("Ayşe")
print(len(studentsSet))

x = studentsSet.pop()  # pop sondaki elemanı silme komutu olamasına rağmen set veri yapısında index olmadığı için random bir elemanı siler
print(len(studentsSet))
print(studentsSet)

studentsSet.clear()  # clear ----> setteki tüm elemanları temizler
print(len(studentsSet))
print(studentsSet)
