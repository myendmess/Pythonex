from functions import square

for i in range(10):
    print (f"The square of {i} is {square(i)}") #it's goign to be printed 2 times cause of print present in both this file and imported file
    
    #2nd method
    #import funcitons
    #for i in range(10):
    #print (f"The square of {i} is {functions.square(i)}")
    