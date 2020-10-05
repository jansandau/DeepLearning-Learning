import matplotlib.pyplot as plt

x = [[1, 4, 3,9], 
     [3,1,5,2]]

y = ['red' , 'blue', 'blue', 'red']

x1 = x[0]
x2 = x[1]

plt.scatter(x1, x2, color =y)
#plt.show()

w = [1, 3, 6, 9, 7, 4]
print(w)

w_squared = [val**2 for val in w[0 : 4]]

print(w_squared)
