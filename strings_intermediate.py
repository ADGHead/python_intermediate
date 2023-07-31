my_string = "I'am a programmer"
print(my_string)

my_string = "      Hello World    "
#To remove the spaces from the string we use the strip function
my_string = my_string.strip()
print(my_string)

#To check weather the string starts with something use the startswith function
#print(my_string.startswith("H"))

#We can also check weather the string ends with something by using the endswith function
#print(my_string.endswith("World"))

#We can also replace things in a string using the replace function
#print(my_string.replace("World","Universe"))

#my_string_2 = "How are you doing"
#To turn into a list with different components we use the split function
#my_list = my_string_2.split()
#Then to turn it back into a string we use the join function
#new_string = " ".join(my_list)
#print(my_list)

#my_list = ["a"] * 6
#print(my_list)

#my_string_2 = " ".join(my_list)
#print(my_string_2)

#FORMATTING
#var = "Tom"
#my_string = "The variable is %s" %var
#print(my_string)

#var = 3
#my_integer = "The variable is %d" %var
#print(my_integer)

#var = 3.142
#my_float = "The variable is %f" %var
#print(my_float)
#You can specify the amount of numbers that are printed by using a decimal point then the number e.g %.2f

#var = 3.142
#my_float = "The variable is {}".format(var)
#print(my_float)
#You can also do the same thing but placing it in a braces and using a colon {:.2f}

#var = 3.142
#var_2 = 6
#my_string = f"The variable is {var+2} and {var_2}"
#print(my_string)