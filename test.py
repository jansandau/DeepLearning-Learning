print("Hello World")

a = 3 
b = 4 
 

print(a + b)
a = 3
b = 3 

#def = function
def sum(a, b):
    c = a + b
    print(c)

sum(a,b)



def einausgaben (einnhmen, ausgaben): 
    bleite = False 
    if ausgaben > einnhmen:
        bleite = True 
    
    if bleite == True: 
        print("ALARM")
    else : 
        print("Alles gut")
    

einausgaben(100, 199)
