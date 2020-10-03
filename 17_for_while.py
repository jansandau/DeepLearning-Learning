###For und While###

zahlen = [1,2,3,4,5,6]
for i in range(5):

    print(i)

print("\n")

for y in zahlen:
    print(y)

print("\n")

#Start, Stop, Step
for x in range(1, 10, 2):
    print (x)

print("\n")


#while
ich_bin_pleite = False
kontostand = 10 

while ich_bin_pleite == False: 
    print("Nicht pleite ", kontostand)
    kontostand -= 1

    if(kontostand <= 0): 
        ich_bin_pleite = True
        print("PLEITE: ", kontostand)
