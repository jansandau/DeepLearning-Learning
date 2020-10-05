
my_list = []

for i in range(10): 
    my_list.append(i)

print(my_list)

#list comprehension

myList2 = [i for i in range(10)]

print(myList2)

#multi dim list 
M = [[1, 2], 
[3, 4]]

print(M)

M2 = [[i+j for j in range(3)] for i in range(3)]

print(M2)