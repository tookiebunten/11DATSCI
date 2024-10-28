"""Consider three separate states – tired, hungry, thirsty. 
A table is provided, below. It is a mapping between 
states to an associated action.  
 
Create a function that takes three arguments, which 
are the states, and returns the corresponding action. 

ired |hungry |thirsty |action 
False |False |False |“do nothing” 
False |False |True |“drink” 
False |True |False |“eat” 
False |True |True |“drink and eat” 
True |False |False |“sleep” 
True |False |True |“drink in bed” 
True |True |False |“eat in bed” 
True |True |True |“eat and drink in bed” 

"""
