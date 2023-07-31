#def symmetrical_palindrome(x):
    #'''This is a function used to check if the word is symmetric or a palindrome'''
    #list = []
    #count = 0
    #if count <= len(x):
        #for words in x:
            #list.insert(count, words)
            #count += 1
    #symmetry = int((len(list)/2)-1)
    #symmetry_2 = int(len(list)-1)
    #list_1 = ""
    #list_2 = ""
    #while symmetry_2 != symmetry and symmetry !=0:
        #list_1 += list[symmetry]
        #list_2 += list[symmetry_2]
        #symmetry_2 -= 1
        #symmetry -= 1
    #if list_1 == list_2:
        #print("This word is symmetrical")
    #else:
        #print("This word is not symmetrical")
    #list.reverse()
    #palindrome = "".join(list)
    #palindrome.lower()
    
    #if palindrome == x:
        #print("This word is a palindrome")
    #else:
        #print("This word is not a palindrome")
    
#symmetrical_palindrome("amaama")


#def checking_dictionary(x,d):
    #if x in d:
        #print("Present, value = "  + str(d.get(x)))
    #else:
        #print("Not present")

#d = {"a" : 100, "b": 200, "c": 300}
#b = input('Please input a letter: ')

#checking_dictionary(b,d)

#def converting_numbers(s):
    #numbers = {
        #"zero" : 0,
        #"one" : 1,
        #"two" : 2,
        #"three" : 3,
        #"four" : 4,
        #"five" : 5,
        #"six" : 6,
        #"seven" : 7,
        #"eight" : 8,
        #"nine" : 9
    #}
    #listings = s.split()
    #count = 0
    #result = "" 
    #while len(listings) != count:
        #result += str(numbers.get(listings[count]))
        #count += 1
    #print(result)

#words = "zero four zero one"
#converting_numbers(words)

#import sys

#set_a = {1, 2, 3, 4, 5, 6, 7}
#set_b = {"A", "h", "m", "e", "d"}
#set_c = {1, "a", "c", "f"}

#print(sys.getsizeof(set_a), "bytes")
#print(sys.getsizeof(set_b), "bytes")
#print(sys.getsizeof(set_c), "bytes")



class Vehicle():

    color = "white"

    def __init__(self, name, max_speed, mileage, capacity):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        self.capacity = capacity

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"
    
    def fare(self):
        return self.capacity * 100

class Bus(Vehicle):
    def fare(self):
        amount = super().fare()
        amount += amount * 10/100
        return amount

class Car(Vehicle):
    pass

bus = Bus("school Volvo Speed", 180, 12, 50)

def instance(o):
    if isinstance(o, Vehicle):
        return True





#print(bus.name)
#print(bus.max_speed)
#print(bus.mileage)
#print(bus.seating_capacity("50"))
print(bus.fare())
print(instance(bus))

