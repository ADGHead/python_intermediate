my_tuple = (1, 2, 3)
my_list = [4, 5, 6]

new_list = [*my_tuple, *my_list]
print(new_list)

dict_a = {"a" : my_tuple, "b" : 2}
dict_b = {"c" : 3, "d" : 4}
my_dict = {**dict_a, **dict_b}
print(my_dict)