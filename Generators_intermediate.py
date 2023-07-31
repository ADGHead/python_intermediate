import sys

def mygenerator():
    yield 1
    yield 2
    yield 3

g = mygenerator()
print(g)

#for i in g:
    #print(i)

#value = next(g)
#print(value)

#value = next(g)
#print(value)

#value = next(g)
#print(value)

print(sum(g))
print(sorted(list((g))))

#def countdown(num):
    #print("starting")
    #while num > 0:
        #yield num
        #num -= 1

#cd = countdown(10)
#print(list(cd))

#for i in cd:
    #print(i)

#value = next(cd)
#print(value)

#print(next(cd))

#def first(n):
    #nums =[]
    #num = 0
    #while num < n:
        #nums.append(num)
        #num += 1
    #return nums

#def first_generator(n):
    #num = 0
    #while num < n:
        #yield num
        #num += 1

#print(sys.getsizeof(first(10)), "bytes")
#print(sys.getsizeof(first_generator(10)), "bytes")

#def fibonacci(limit):
    #a, b = 0, 1
    #while a < limit:
        #yield a
        #a, b = b, a+b

#fib = fibonacci(30)
#for i in fib:
    #print(i)


#mygenerator = (i for i in range(10) if i%2 == 0)
#print(mygenerator)
#When using normal brackets instead of square brackets to iterate it is termed as a generator 
#While when using square brackets instead is termed as a list



