###Schleifen für Listen###

zahlen = [1, 2, 3, 4, 5, 6]

for i in zahlen:
    print(i)

print("\n")

#len = length
for i in range(len(zahlen)):
    print(zahlen[i])

#zip function
noten = [1,2,3,4]
fächer = ["Informatik", "Mathe", "Deutsch", "Franz"]

for note, fach in zip(noten, fächer): 
    print(note , ": " , fach)

print("\n")

#enumerate
präferenzen =  ["Informatik", "Mathe", "Deutsch", "Franz"]

for index, fach in enumerate(präferenzen):
    print(index , " : ", fach)



