"""
- The difference between arguments and parameters
- Positional and keyword arguments
- Default arguments
- Variable-length arguments(*args and **kwargs)
- Container unpacking into function arguments
- Local vs global arguments
- Parameters passing (by value or by reference)
"""

#Parameters are the variables defined in a parenthesis when defining a function and arguments are the values paased for this parameters when calling a function


#Variable length arguments(*args, **kwargs)
def fool(a, b, *args, **kwargs):
    print(a,b)
    for arg in args:
        print(arg)
    for key, value in kwargs.items():
        print(key, value)

fool(1, 2, 3, 4, 5, six=6, seven=7)

#Any argument passed after the positional argument (*args or *) is going to be a keyword argument
#def fool(a, b, *, c, d):
    #print(a, b, c, d)

#fool(1, 2, c=3, d=4)


#def fool(*args, last):
    #for arg in args:
        #print(arg)
    #print(last)

#fool(1, 2, 3, last=100)


#Unpacking Arguments
#def fool(a, b, c):
    #print(a, b, c)

#my_list = [0, 1, 2]
#fool(*my_list)

#my_dict = {"a" : 1, "b":2, "c":3}
#fool(**my_dict)

#Global v Local variable

number = 0

#def fool():
    #x = number
    #print("Number inside function:", x)

#fool()

#Parameter passing(By value or By reference)
#def fool(x):
    #x = 5

#var = 10
#fool(var)
#print(var)

#def fool(a_list):
    #a_list.append(4)
    #a_list[0] = -100

#my_list = [1, 2, 3]
#fool(my_list)
#print(my_list)