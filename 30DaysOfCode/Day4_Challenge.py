"""
Task: 
Write a Person class with an instance variable, age, and a constructor that
takes an integer, initialAge, as a parameter. 
The constructor must assign initialAge to age after confirming the argument passed 
as initialAge is not negative; if a negative argument is passed as initialAge, 
the constructor should set age to 0 and print "Age is not valid, setting age to 0.". 

In addition, you must write the following instance methods:

yearPasses() should increase the age instance variable by 1.
amIOld() should perform the following conditional actions:
If age < 13, print "You are young.",
If age >= 14 and < 18, print "You are a teenager.",
Otherwise, print "You are old.".
"""

class Person:
    global age

    def __init__(self,initialAge):
        global age
        if initialAge >= 0:
            age = initialAge
        else:
            age = 0
            print("Age is not valid, setting age to 0.")


    def amIOld(self):
        global age
        if age < 13:
            print("You are young.")
        elif age < 18:
            print("You are a teenager.")
        else:
            print("You are old.")
    
    def yearPasses(self):
        global age
        age += 1
        
t = int(input())
for i in range(0, t):
    age = int(input())         
    p = Person(age)  
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()       
    p.amIOld()
    print("")