# **30 days of Advanced Python Concepts**

## 6. Collections <br>

In collections we will be looking at five concepts<br>

- [**30 days of Advanced Python Concepts**](#30-days-of-advanced-python-concepts)
  - [6. Collections <br>](#6-collections-)
    - [Counter <br>](#counter-)
    - [namedtuple](#namedtuple)
    - [OrderedDict](#ordereddict)
    - [defaultdict](#defaultdict)
    - [deque](#deque)
  - [Thanks for joining todays class](#thanks-for-joining-todays-class)

---

---

### Counter <br>

It shows number of elements of a list as keys and the element as the value

```py
from collections import Counter

a = "aaaaabbbbccc"
my_counter = Counter(a)

print(my_counter.items())  # dict_items([('a', 5), ('b', 4), ('c', 3)])
print(my_counter.keys())  # dict_keys(['a', 'b', 'c'])
print(my_counter.values())  # dict_values([5, 4, 3])

print(my_counter.most_common(1)[0][0])   # a
print(my_counter.most_common(2))  # [('a', 5), ('b', 4)]
print(list(my_counter.elements())) # ['a', 'a', 'a', 'a', 'a', 'b', 'b', 'b', 'b', 'c', 'c', 'c']
```
### namedtuple
```py
from collections import namedtuple

Point = namedtuple('Point', 'x, y')
pt = Point(1, -4)
print(pt)  # Point(x=1, y=-4)
print(pt.x, pt.y)  # 1 -4
```
### OrderedDict
This became depreciated as at python3.7 as dictionary class also got the fuctionality to remember the order with which items have been added
```py
from collections import OrderedDict

ordered_dict = OrderedDict()
ordered_dict['a'] = 2
ordered_dict['b'] = 3
ordered_dict['c'] = 4
ordered_dict['d'] = 5

print(ordered_dict)  #OrderedDict([('a', 2), ('b', 3), ('c', 4), ('d', 5)])
```
### defaultdict
```py
from collections import defaultdict

d = defaultdict(int)

d['a'] = 1
d['b'] = 2


print(d['a'])  # 1
print(d['b'])  # 2
print(d['c'])  # 0 this would otherwise return a key error when used in a normal dictionary
```

### deque 
This is a double ended queue
```py
from collections import deque

d = deque()

d.append(2)
d.append(4)
d.appendleft(1)
print(d)  # deque([1, 2, 4])

d.pop()
print(d)  # deque([1, 2])
d.popleft()
print(d)  # deque([2])

d.clear()

d.extend([5, 4, 5, 6, 7])
d.extendleft([1, 2, 3])
print(d)  # deque([3, 2, 1, 5, 4, 5, 6, 7])

d.rotate(1)
print(d)  # deque([7, 3, 2, 1, 5, 4, 5, 6])
```

## Thanks for joining todays class
Remember to practice the concepts that you have learned