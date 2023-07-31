import random

#This is used to print a random float from 0-1
#a = random.random()
#print(a)

#This is used to print a random float from the range specified
#b = random.uniform(1, 10)
#print(b)

#This is used to print a random integer from the range specified
#c = random.randint(1, 10)
#print(c)

#This does the samething as the one above but the difference is that it can never print out the last value
#d = random.randrange(1,10)
#print(d)

#e = random.normalvariate(0, 1)
#print(e)

#SEQUENCES
#This prints out a randomly selected element
#mylist = list("ABCDEFGH")
#a = random.choice(mylist)
#print(a)

#This is used to pick out a unique element and the number of elements selected can be specified but it cannot pick the same elements twice
#mylist = list("ABCDEFGHI")
#a = random.sample(mylist, 3)
#print(a)

#This is used to pick out a unique element and the number of elements can be specified but it can select the same element twice
#mylist = list("ABCDEFGH")
#a = random.choices(mylist, k=3)
#print(a) 

#This is used to shuffle the items in a list
#mylist = list("ABCDEFGH")
#a = random.shuffle(mylist)
#print(mylist)

#random.seed(1)
#print(random.random())
#print(random.randint(1, 10))
#random.seed(2)
#print(random.random())
#print(random.randint(1, 10))

#random.seed(1)
#print(random.random())
#print(random.randint(1, 10))
#random.seed(2)
#print(random.random())
#print(random.randint(1, 10))

import secrets
#The randbelow function is used to get a random number between the range specified but the last number is not included
#a = secrets.randbelow(10)
#print(a)

#The randbits function is used to pick a random number between 0 and the binary equivalent
#b = secrets.randbits(4)
#print(b)

#The choice function is used to pick a random element in a list
#mylist = list("ABCDEFGH")
#c = secrets.choice(mylist)
#print(c)

import numpy as np

#a = np.random.rand(3,3)
#print(a)

#b = np.random.randint(0,10,(3,4))
#print(b)

#c = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
#print(c)
#np.random.shuffle(c)
#print(c)

#np.random.seed(1)
#print(np.random.rand(3,3))
#np.random.seed(1)
#print(np.random.rand(3,3))


#Getting 3 numbers that are between 100 and 999 and are divisble by 5
print("Getting 3 random numbers between 100 and 999 that are divisible by 5")
for i in range(3):
    num = random.randrange(100,999,5)
    print(num)

#CREATING A LOTTERY TICKET SELECTOR
lottery_tickets = []

for i in range(100):
    lottery_tickets.append(random.randrange(1000000000, 9999999999))

winners = random.sample(lottery_tickets,2)
print(winners)

#Creating an OTP
secrets_generator = secrets.SystemRandom()

otp = secrets_generator.randrange(100000,999999)

print(otp)


#Generating a random string of length 5
import string

def random_string(StringLength):
    letters = string.ascii_letters
    return "".join(random.choice(letters) for i in range(StringLength))


print(random_string(5))


#Password Generator
import random
import string

def randomPassword():
    randomSource = string.ascii_letters + string.digits + string.punctuation
    password = random.sample(randomSource, 6)
    password += random.sample(string.ascii_uppercase, 2)
    password += random.choice(string.digits)
    password += random.choice(string.punctuation)

    passwordList = list(password)
    random.SystemRandom().shuffle(passwordList)
    password = ''.join(passwordList)
    return password

print ("Password is ", randomPassword())

#Token
print("Random secure Hexadecimal token is ", secrets.token_hex(64))
print("Random secure URL is ", secrets.token_urlsafe(64))

