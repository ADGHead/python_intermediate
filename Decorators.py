#def decorator(func):

    #def wrapper():
        #print("Start")
        #func()
        #print("End")
    #return wrapper



#def print_name():
    #print("Alex")

#print_name = decorator(print_name)
#print_name()

import functools
from typing import Any

#def decorator(func):
    #@functools.wraps(func)
    #def wrapper():
        #print("Start")
        #func()
        #print("End")
    #return wrapper

#@decorator
#def print_name():
    #print("Alex")

#print_name();
#print(help(print_name))
#print(print_name.__name__)



#def decorator(func):
    #@functools.wraps(func)
    #def wrapper( *args,**kwargs):
        #print("Start")
        #result = func(*args,**kwargs)
        #print(result)
        #print("End")
    #return wrapper

#@decorator
#def add_num(x):
    #return x + 5

#print(add_num(10))
#print(help(add_num))
#print(add_num.__name__)


def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args,**kwargs):
            for i in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat

@repeat(num_times=4) 
def greet(name):
    print(f"Hello {name}")

greet("Alex")

#def decorator(func):

    #@functools.wraps(func)
    #def wrapper(*args, **kwargs):
        #print("Start")
        #result = func(*args, **kwargs)
        #print("End")
        #return result
    #return wrapper


#def debug(func):
    #@functools.wraps(func)
    #def wrapper(*args, **kwargs):
        #args_repr = [repr(a) for a in args]
        #kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        #signature = ", ".join(args_repr + kwargs_repr)
        #print(f"calling {func.__name__}({signature})")
        #result = func(*args, **kwargs)
        #print(f"{func.__name__!r} returned {result!r}")
        #return result
    #return wrapper

#@debug
#@decorator
#def say_hello(name):
    #greeting = f"Hello {name}"
    #print(greeting)
    #return greeting

#say_hello("Alex")

#class CountCalls:

    #def __init__(self, func):
        #self.func = func
        #self.num_calls = 0

    #def __call__(self, *args, **kwargs):
        #self.num_calls += 1
        #print(f'This is executed {self.num_calls} times')
        #return self.func(*args, **kwargs)




#@CountCalls
#def say_hello():
    #print("Hello")

#say_hello()

#Implement a timer decorator to calculate the execution time of a function
#You can implement a debug decorator to know more about the function
#You can use a check decorator to see weather the arguments will fulfill its requirements
