#Plot 

import matplotlib.pyplot as plt 

umsatz  = [10000, 35000, 45000, 650000, 1000000, 1020000 ]

plt.plot([1,2,3,4,5,6], umsatz, color="blue")

#Plot Beschriftung
plt.xlabel("Monat")
plt.ylabel("Umsatz")
plt.title("Umsatz 2020")
plt.show()

