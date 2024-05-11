file = open("customers.txt","r",encoding="UTF-8")
print(file.read())
file.close()

fileToAppend = open("students.txt","w")
fileToAppend.write("\n")
fileToAppend.write("Metin")
fileToAppend.close()


import os

if os.path.exists("students.txt"):
    os.remove("students.txt")
else:
    print("No file")

os.rmdir("empty")
