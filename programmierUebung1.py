import numpy as np 
import matplotlib.pyplot as plt

#function for e für die übergebene liste 
def aList (list):
    result = []

    for val in list:
        result.append(np.exp(val))
    
    return result


zahlen = [1,2,3, 4]

#retrun wert speichern
ergebnis = aList(zahlen)

plt.plot(ergebnis, color="green")
plt.show()
