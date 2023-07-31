#Errors and Exceptions
#Syntax Error, TypeError, ImportError, ModuleNotFoundError, NameError, FileNotFoundError, ValueError, IndexError, KeyError, ZeroDivisionError

#RAISING AN EXCEPTION
#x = -5
#if x < 0:
    #raise Exception("x should be positive")

#ASSERTION
#x = -5
#assert(x>=0), "x is not positive"

#TRY AND EXCEPT BLOCK
#try:
    #a = 5/0
#except Exception as err:
    #print(err)
#else:
    #print("Everything is fine")
#finally:
    #print("Cleaning up .....")


#DEFINING OUR OWN EXCEPTION
class ValueTooHighError(Exception):
    pass

class ValueTooSmallError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value


def test_value(x):
    if x > 100:
        raise ValueTooHighError("Value is too high")
    if x < 5:
        raise ValueTooSmallError("Value too small", x)

try:    
    test_value(1)
except ValueTooHighError as err:
    print(err)
except ValueTooSmallError as err_2:
    print(err_2.message, err_2.value)