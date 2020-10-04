#import numpy 
import numpy as np 

zahlen = [100, 23, 4, 5 , 6, 8]

#cast zahlen (normnal array) to np array
zahlen_np_array = np.array(zahlen, int)

print(zahlen_np_array)

maxZahlen = np.max(zahlen_np_array)

print("Maximum: ", maxZahlen)