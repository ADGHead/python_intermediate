#Lambda arguments: expression

add10 = lambda x: x + 10
print(add10(5))

mult = lambda x, y: x*y
print(mult(2,7))

#SORTED METHOD
points = [(1, 2), (15, 1), (5, -1), (10,4)]
point_sorted = sorted(points, key=lambda x: x[0] + x[1])
print(point_sorted)

#MAP
#map(func,seq)
#a = [1, 2, 3, 4, 5]
#print(list(map(lambda x: x*2, a)))


#FILTER
#filter(func, seq)
#a = [1, 2, 3, 4, 5, 6]
#print(list(filter(lambda x: x%2==0, a)))

#c =[x for x in a if x%2==0]
#print(c)

#REDUCE
#reduce(func,seq)
from functools import reduce
a = [1, 2, 3, 4, 5, 6]
prod_a = reduce(lambda x, y: x*y, a)
print(prod_a)