# **30 days of Advanced Python Concepts**

## 2. Tuples <br>

This is a collection data type that is immutable "cannot be changed" <br>
A tuple must always end with a comma or it may not be recognised as tuple

```py
myTuple = ("Max", "John", "Mary",)

print(type(myTuple))  # <class 'tuple'>
```

To create a tuple from a list

```py
myList = ["Max", "John", "Mary"]
myTuple = tuple(myList)

print(myTuple)  # ('Max', 'John', 'Mary')
```

Printing an element from a tuple

```py
myList = ["Max", "John", "Mary"]
myTuple = tuple(myList)

print(myTuple[1])  # John
```

To print all elements from a tuple

```py
myTuple = ("Max", "John", "Mary",)

for i in myTuple:
    print(i)
```

To check the length of your tuple

```py
myTuple = ("Max", "John", "Mary",)

print(len(myTuple))  # 3
```

**count()** method in a tuple tells us how many times an element has been repeated <br>
**index()** method tells us the index of the passed argument

```py
myTuple = ('a', 'p', 'p', 'l', 'e', 's')

count = myTuple.count('p')
index = myTuple.index('p')

print(index)  # 1
print(count)  # 2
```

To copy a tuple we utilise the slicing functions seen earlier

```py
myTuple = (2, 3, 4, 5, 6, 7, 8, 9)

newTuple = myTuple[0:4]

print(newTuple)  # (2, 3, 4, 5)
```

Destructuring and assignment of tuple values

```py
myTuple = ("Mason", "Nairobi", 19)

name, location, age = myTuple

print(name)  # Mason
print(location)  # Nairobi
print(age)  # 19
```

Unpacking more than one value of a tuple into a variable using \*

```py
myTuple = ("Mason", "Nairobi",  "Boston", "Berlin", 19)

name, *location, age = myTuple

print(name)  # Mason
print(location)  # ['Nairobi', 'Boston', 'Berlin']
print(age)  # 19
```
Tuples are much more light weight than lists. This increases their efficiency when <br>
we run complex functions on them
```py
import sys
myTuple = ("Mason", "Nairobi",  "Boston", "Berlin", 19)
myList = ["Mason", "Nairobi",  "Boston", "Berlin", 19]

print(sys.getsizeof(myTuple), "Bytes")  # 80 Bytes
print(sys.getsizeof(myList), "Bytes")  # 104 Bytes
```
This complexity can be seen when we use the timeit module
```py
import timeit
myTuple = ("Mason", "Nairobi",  "Boston", "Berlin", 19)
myList = ["Mason", "Nairobi",  "Boston", "Berlin", 19]

print(timeit.timeit(stmt='("Mason", "Nairobi",  "Boston", "Berlin", 19)', number=1000000))  # 0.012786923995008692 s
print(timeit.timeit(stmt='("Mason", "Nairobi",  "Boston", "Berlin", 19)', number=1000000))  # 0.012422145999153145 s
```
## Thank you for joining todays class
**Don't forget to practice.**