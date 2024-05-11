tupleList = (2, 4, 6, "Ankara", (2, 3, 4))
list = [2, 4, 6, "Ankara", [3, 4, 5]]

list[0] = 6
# tupleList[0] = 6 #TypeError: 'tuple' object does not support item assigment
# tuple ---> read only veri yapısına sahiptir

# -----> tuple olduğunu belirtmek için virgül kullanılır
tupleValue = ("Murat",)
print(type(tupleValue))

print(tupleList[1:2])
print(list[1:2])

print(tupleList[-2])  # sağdan ikinci demektir
print(list[-2])

print(type(tupleList))
print(type(list))
print(tupleList)
print(list)
print(len(tupleList))
print(len(list))
