from time import sleep                            #importing modules from time  
                                                  #importing modules from threading
from threading import *



class ONE(Thread):                                 #creating a class name ONE with class builtin function and inheriting the Thread function to the class by Thread keyword                                 
    
    def run(self):                                 #creating a function named run with the self keyword   

        for i in range(5):                         #within the function under a class we are initializing a for loop that prints HELLO WORLD 
            print("HELLO WORLD")
            sleep(1)                               # sleep function to used to make a time difference of 1 sec after the output and after another output


class TWO(Thread):
    def run(self):
        for i in range(5):
            print("HELLO WORLD 1")
            sleep(1)                                


o1=ONE()
o2=TWO()

o1.start()

sleep(0.3)                                          #This sleep function creates a time difference of 0.3 ms between two instances with sleep of 1ms
o2.start()

o1.join()                                           #This function 'join' used to makes the main thread to run at last 
o2.join()

print("BYE")                                        #Main function 
