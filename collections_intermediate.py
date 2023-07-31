#collections: counter, namedtuple, orderedDict, defaultdict, deque
from collections import Counter
a ="aaaaabbbccc"
my_counter = Counter(a)
print(my_counter)
print(my_counter.most_common(1)[0][0])
#The counter function stores the string as a dictionary with the corresponding variable as the key and their value as the value
#To access the tuple of the list after the most common function input a square bracket and the index you want to output
#Then if you want to access the element in the tuple you use another square bracket after the second square bracket 

from collections import namedtuple
point = namedtuple("point","*")
pt = point(1, 2 ,3, 4, 5, 6, 7)
print(pt)

from collections import OrderedDict
ordered_dict = OrderedDict()
ordered_dict["a"] = 1
ordered_dict["b"] = 2
ordered_dict["c"] = 3
ordered_dict["d"] = 4
print(ordered_dict)

from collections import defaultdict
d = defaultdict(int)
d["a"] = 1
d["b"] = 2
print(d)

from collections import deque
d = deque()
d.append(1)
d.append(2)
d.append(3)
d.appendleft(3)
d.extend([4,5,6])
d.extendleft([7,8,9])
d.rotate(4)
print(d)

