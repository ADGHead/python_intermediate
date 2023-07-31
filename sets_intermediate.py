my_set = {1, 2, 3}
print(my_set)
#A set does not allow duplicate elements

my_set_2 = set("Hello")
print(my_set_2)

#If you want to create an empty set you have to use the set function unless it will identify as a dictionary
my_empty = set()

#To add elements into a set
my_empty.add(1)
my_empty.add(2)
my_empty.add(3)

#To remove elements in a set
#my_empty.remove(3)
#my_empty.discard(2)

#To clear elements
#my_empty.clear()


#print(my_empty)

#To iterate over a set
for i in my_empty:
    print(i)

#Set Theory
odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}

#UNION
u = odds.union(evens)
print(u)

#INTERSECTION
i = odds.intersection(evens)
print(i)

#DIFFERENCE
set_a = {1, 2, 3, 4, 5, 6}
set_b = {1, 2, 3, 4, 6, 7}
set_c = {7,8}

#diff = set_a.difference(set_b)
#print(diff)

#diff_2 = set_a.symmetric_difference(set_b)
#print(diff_2)

#UPDATE
#set_a.update(set_b)
#print(set_a)

#set_a.intersection_update(set_b)
#print(set_a)

#set_a.difference_update(set_b)
#print(set_a)

#set_a.symmetric_difference_update(set_b)
#print(set_a)

#SUBSETS
#print(set_a.issubset(set_b))
#print(set_b.issubset(set_a))

#SUPERSETS
#print(set_b.issuperset(set_a))
#print(set_a.issuperset(set_b))

#DISJOINT
#print(set_a.isdisjoint(set_b))
#print(set_a.isdisjoint(set_c))

#Copying of sets
set_copy = {1, 2, 3, 4, 5}
set_copy_2 = set(set_copy)

#Frozen Set
a = frozenset([1, 2, 3, 4])
print(a)
