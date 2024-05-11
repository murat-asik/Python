setA = {1, 2, 3, 4, 5}
setB = {1, 3, 4, 6, 7, 8}

print(setA | setB)
print(setA.union(setB))
print(setB.union(setA))

"""
set union

orijinal kümedeki tüm öğeleri ve belirtilen kümelerden 
tüm öğeleri içeren bir küme döndürür. Virgülle ayırarak 
istediğiniz sayıda küme belirtebilirsiniz. Bir öğe birden 
fazla kümede mevcutsa, sonuç bu öğenin yalnızca bir görünümünü içerir

"""

print(setA & setB)
print(setA.intersection(setB))
print(setB.intersection(setA))

"""
set intersection

İntersection () yöntemi, tüm kümeler için ortak olan öğeleri içeren yeni bir küme döndürür

"""

print(setA - setB)
print(setA.difference(setB))
print(setB.difference(setA))

"""
set difference

Difference () yöntemi, iki kümenin ayar farkını döndürür

"""

print(setA ^ setB)
print(setA.symmetric_difference(setB))
print(setB.symmetric_difference(setA))

"""
set symmetric_difference

Python symmetric_difference () yöntemi, iki kümenin simetrik
farkını döndürür. İki A ve B kümesinin simetrik farkı, A veya B'de 
bulunan, ancak kesişme noktasında olmayan elemanlar kümesidir.

"""
