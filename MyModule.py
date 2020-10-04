#functions 

my_list = [-2, 1, -3 , 10 , -100 , -10 , 23]

#function to geht min from the list. list is a parameter
def getMax(list):
    result = 0
    for i in range(1, len(list)):
        if list[i] < result:
            result = list[i]
    
    print(result)

#call function

