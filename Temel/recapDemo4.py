students = ["Murat","Umut","Ahmet","Mehmet","Veli"]

fileToAppend = open("students.txt","a")

for student in students:
    fileToAppend.write(student)
    fileToAppend.write("\n")

fileToAppend.close()