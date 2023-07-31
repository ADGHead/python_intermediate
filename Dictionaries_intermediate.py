my_dict = {"name":"max", "age":28, "city":"New York"}
print(my_dict) 

my_dict_2 = dict(name="mary", age=27, city="Boston")
print(my_dict_2)

#To create a new element in a dictionary
my_dict["email"] = "max@xyz.com"
print(my_dict)

#To delete new elements im a list
#del my_dict["name"]
#print(my_dict)

#Or you can pop elements in a list
#my_dict.pop("name")
#print(my_dict)

#Iterating through a dictionary
for key in my_dict.keys():
    print(key)

for value in my_dict.values():
    print(value)

for key, value in my_dict.items():
    print(key, value)

#Copying a dictionary
my_dict_cpy = my_dict.copy()
print(my_dict_cpy)

#Merging of dictionaries
my_dict_up = {"name":"Ahmed", "age":24, "email":"sample@gmail.com"}
my_dict_up_2 = dict(name = "mary", age = 27, city = "Boston")

my_dict_up.update(my_dict_up_2)
print(my_dict_up)
print(my_dict_up.get("sample@gmail.com", "That is not a key"))