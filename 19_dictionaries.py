#Dicts

#key: value
noten_klasse_8a = {"armin": 1, "ben": 2, "jan": 1}

note_armin = noten_klasse_8a["armin"]

print("\n")

#mit .items() gibt es den key und schlüssel
for i, note in noten_klasse_8a.items(): 
    print(i , " har eine ", note)


for i in noten_klasse_8a.keys(): 
    print(i)