import numpy as np 


my_list = np.array([1,2,3], dtype =np.float)
print(my_list)

#shape = dimensionen
my_zero_array = np.zeros(shape=(10), dtype=np.int)

print(my_zero_array)

my_one_array = np.ones(shape=(4,4), dtype=np.int)
print(my_one_array)

my_random_array = np.random.randint(low = 0, high = 11, size = 100)

print(my_random_array)