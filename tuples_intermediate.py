#To create a tuple with one element you have to put a comma at the end otherwise it will identify as a string type
my_tuple = ("Ahmed",)
print(type(my_tuple))

my_tuple_2 = tuple(["Ahmed", "school", "Classes"])
print(my_tuple_2)

#Unpacking of tuples
my_tuple = "Max", 28, "Boston"
name, age, city = my_tuple
print(name)
print(age)
print(city)

my_tuple_integer = 0, 1, 2, 3, 4, 5
i1, *i2, i3 = my_tuple_integer
print(i1)
print(i2)
print(i3)

#Comparison of a list and a tuple
import sys

My_list = [0, 1, 2, "hello", True]
my_tuple_comp = (0, 1, 2, "hello", True)

print(sys.getsizeof(My_list), "bytes")
print(sys.getsizeof(my_tuple_comp), "bytes")

import timeit
print(timeit.timeit(stmt = "[0, 1, 2, 3, 4, 5]", number = 1000000))
print(timeit.timeit(stmt = "(0, 1, 2, 3, 4, 5)", number=1000000))