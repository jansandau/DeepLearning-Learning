### Datentypen in Python ###
# Variablen erstellen

name = 'Jan'
alter = 23

print( name + ' ' + str(alter))

#Function with Parameters
def newUser(name, adresse, alter):
    newName = name
    newAdresse = adresse
    newAlter = alter

    altgenug = False

    #if Statement 
    if alter > 18: 
        altgenug = True
        altersFreigabe(altgenug)

    print("Name: " , newName)


def altersFreigabe(checkValue):

    if checkValue == True: 
        print("Alt genug")

newUser("Jan", "", 23)

print(10 %  2)