dictionaries = {
    "book" : "kitap",
    "table" : "masa",
    "pencil" : "kalem"
}

dictionaries2 = dict(kitap = "book", masa = "table")
dictionaries["book"] = "okuma kitabı"
del(dictionaries["book"])
print(dictionaries["pencil"])
print(dictionaries)
print(dictionaries2)