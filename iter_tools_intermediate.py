#itertools: product, permutations, combinations, combinations, accumulate, groupby and infinite iterators
from itertools import product
a = [1]
b = [3]
prod = product(a,b, repeat=2)
print(list(prod))

from itertools import permutations
a =[1, 2, 3]
per = permutations(a, 2)
print(list(per))
#You can specify the number of values you want to use for the permutations by inputing another argument

from itertools import combinations, combinations_with_replacement
b = [1, 2, 3, 4]
comb = combinations(b, 2)
print(list(comb))
comb_wr = combinations_with_replacement(b, 2)
print(list(comb_wr))
#You can specify weather you want the combinations to have replacement or not by using the combinations_with_replacement module

from itertools import accumulate
import operator
c = [1, 2, 3, 4]
acc = accumulate(c, func=operator.mul)
print(list(acc))

from itertools import groupby
def smaller_than_3(x):
    return x<3

d = [1, 2, 3, 4]
group_obj = groupby(d, key=smaller_than_3)
for key, value in group_obj:
    print(key, list(value))

persons = [{"name": "Tim", "age": 25}, {"name": "Dan", "age": 25},
           {"name": "Lisa", "age":27}, {"name": "claire", "age":28}]

group_persons = groupby(persons, key=lambda x: x["age"])
for key, value in group_persons:
    print(key, list(value))


from itertools import count, cycle, repeat
for i in count(10):
    print(i)
    if i == 15:
        break

e = [1, 2, 3]
#for i in cycle(e):
    #print(i)

for i in  repeat(1, 4):
    print(i)