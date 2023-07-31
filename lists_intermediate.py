my_list = ["banana", "cherry", "apple"]

try:
    index = int(input("'Please enter a number :"))
    print(my_list[index])
except IndexError as err:
    print(err)
except ValueError as err2:
    print(err2)

integers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(integers[::2])
#The :: indicates the step in which you want your values to be printed
#If its 2 then it will only print out the indexes 0, 2, 4, 6 and so on
#The : indicates the slicing of the elements

my_list_2 = [1, 2, 3, 4, 5, 6, 7]
b = [i*i for i in my_list_2]


print(b)

#To create a list using iteration you first need your square brackets[] then in the square brackets you write your expression first
#After writing your expression you use the normal for loop


num_1 = [1, 3, 5, 10, 15, 20]
num_2 = [1, 2, 3, 4, 59, 25]

def multiply(a, b):
    count = 0
    list_mult = []
    while count< len(a) and len(b):
        result = a[count] * b[count]
        list_mult.append(result)
        count += 1
    return list_mult


print(multiply(num_1, num_2))

 

