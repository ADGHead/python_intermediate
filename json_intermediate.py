# dictionary - object
# list, tuple - array
# string - string
# int, long, float - number
# True - true
#False - false
# none - null

import json
#person = {"name": "John", "age": 30, "city" : "New York", "hasChildren" : False, "titles" : ["engineer", "programmer"]}
#personJSON = json.dumps(person, indent=4)
#print(personJSON)
# The json.dumps function is to convert the selected data type into json format of that data type

#with open("person.json", "w") as file:
    #json.dump(person, file, indent=4)
#These lines of code is used to create a json file with the selected data type stored in the variable

#person = json.loads(personJSON)
#print(person)
#This is used to convert the data type in json format back to python format

#with open("person.json", "r") as file:
    #person = json.load(file)
    #print(person)
# This is used to convert the code in the json file back to python format


class User:

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
user = User("max", 27)

#This is used to change the class data type to json
#def encode_user(o):
    #if isinstance(o, User):
        #return {"name" : o.name, 'age' : o.age, o.__class__.__name__ : True}
    #else:
        #raise TypeError("Object of type User is not JSON serializable")
    
from json import JSONEncoder
#class UserEncoder(JSONEncoder):
    
    #def default(self, o):
        #if isinstance(o, User):
            #return {"name" : o.name, 'age' : o.age, o.__class__.__name__ : True}
        #return JSONEncoder.default(self, o)
    
class UserEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__

userJSON = json.dumps(user, indent= 4, cls= UserEncoder)
print(userJSON)
    


#userJSON = json.dumps(user, cls = UserEncoder)
#print(userJSON)

#userJSON = UserEncoder().encode(user)
#print(userJSON)


#This is used to decode back to python after being converted to json
#def decode_user(dct):
    #if User.__name__ in dct:
        #return User(name =dct["name"], age =dct["age"])
    #return dct


#user = json.loads(userJSON, object_hook= decode_user)
#print(type(user))
#print(user.name)

import json

#data = {"key1" : "value1", "key2" : "value2"}
#dataJSON = json.dumps(data)
#print(dataJSON)
#print(type(dataJSON))


#First convert it back to a dictionary
#sampleJson = """ {"key1" : "value1", "key2" : "value2"}"""
#print(sampleJson)
#sampleJSON = json.loads(sampleJson)
#print(sampleJSON["key2"])

#sampleJson = {"key1" : "value1", "key2" : "value2"}
#sampleJSON = json.dumps(sampleJson, indent= 2, separators=(",", "="))
#print(sampleJSON)

#sampleJson = {"id" : 1, "name" : "value2" , "age" : 29}
#sampleJSON = json.dumps(sampleJson, sort_keys= True, indent= 2)
#print(sampleJSON)

#sampleJson = """{
#"company" : {
#"employee" : {
#"name" : "emma",
#"payable" : {
#"salary" : 7000,
#"bonus" : 800
#}
#}
#}
#}
#"""
#sampleJSON = json.loads(sampleJson)
#print(sampleJSON["company"]["employee"]["payable"]["salary"])

#class Vehicle:
    #def __init__(self, name, engine, price):
        #self.name = name
        #self.engine = engine
        #self.price = price

#vehicle = Vehicle("Toyota Rav4", "2.5L", 32000)

#from json import JSONEncoder

#class VehicleEncoder(JSONEncoder):
    #def default(self, o):
        #return o.__dict__
    
#vehicle = Vehicle("Toyota Rav4", "2.5L", 32000)
#print("Encode Vehcile Object into JSON")
#vehicleJson = json.dumps(vehicle, indent=4, cls= VehicleEncoder)
#print(vehicleJson)

#Converting back to a class
{"name" : "Toyota Rav4", "engine" : "2.5L", "price" : 32000}

class Vehicle:
    def __init__(self, name, engine, price):
        self.name = name
        self.engine = engine
        self.price = price

def vehicleDecoder(o):
    return Vehicle(o["name"], o["engine"], o["price"])

vehicleObj = json.loads("""{"name" : "Toyota Rav4", "engine" : "2.5L", "price" : 32000}""", object_hook=vehicleDecoder)

print(type(vehicleObj))
print(vehicleObj.name, vehicleObj.engine, vehicleObj.price)