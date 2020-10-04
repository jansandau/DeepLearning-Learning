#function in anderer datei (ähnlich zu Libs)
# import all wäre mit * 
# Alt 1 import  MyModule

#import spezifische function 
# import MyModule as mm
from MyModule import getMax
my_list1  = [-23, 1, -3 , 10 , -101 , -10 , 23]

#call function from other file
getMax(my_list1)