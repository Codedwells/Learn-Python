# **30 days of Advanced Python Concepts**

## 4. Sets <br>

A **set** is a collection data type which is mutable and unlike lists , dictionaries or tuples it **does not allow duplicate** elements.

```py
mySet = {1, 2, 3, 4, 5, 6}
mySecondSet = {1, 2, 4, 3, 2, 1}
myThirdSet = set()
myFourthSet = set("Hello")
lastSet = set([1, 2, 3, 3, 4])

print(mySet)  # {1, 2, 3, 4, 5, 6}
print(mySecondSet)  # {1, 2, 3, 4}
print(type(myThirdSet))  # <class 'set'>
print(myFourthSet)  # {'e', 'H', 'o', 'l'}
print(lastSet)  # {1, 2, 3, 4}
```

You can also add items to your set using the **add** keyword

```py
emptySet = set()

emptySet.add(1)
emptySet.add(2)
emptySet.add(3)
emptySet.add(4)

print(emptySet)  # {1, 2, 3, 4}
```

To remove items use the **remove** or **discard** keywords

```py
mySet = {1, 2, 3, 4, 5, 6}

mySet.remove(2)  # removes one with key of 2
# mySet.remove(7)   this throws an error
mySet.discard(3)  # removes 3
mySet.discard(8)  # does not throw error


print(mySet)  # {1, 4, 5, 6}
```

To **clear** a set

```py
mySet = {1, 2, 3, 4, 5, 6}

mySet.clear()

print(mySet)  # set()
```

You can also use the **pop** method to remove the first element of a set this method returns the <br> removed item while mutating the set

```py
mySet = {1, 2, 3, 4, 5, 6}

print(mySet.pop())  # 1

print(mySet)  # {2, 3, 4, 5, 6}
```

We can also iterate through out set using a **for in** loop

```py
mySet = {1, 2, 3, 4, 5, 6}

for i in mySet:
    print(i)  # prints all elements of the set

```

To check if an item is in the set we can use an **if else** statement

```py
mySet = {1, 2, 3, 4, 5, 6}

if 2 in mySet:
    print("I'm here")
else:
    print("Not here")
```

## Unions and intersections <br>

First create 3 sets of odd, even prime numbers

```py
oddSet = {1, 3, 5, 7, 9}
evenSet = {0, 2, 4, 6, 8}
primeSet = {2, 3, 5, 7}
```

A **union** combines elements of two sets without duplication

```py
oddSet = {1, 3, 5, 7, 9}
evenSet = {0, 2, 4, 6, 8}
primeSet = {2, 3, 5, 7}

u = oddSet.union(evenSet)
u2 = oddSet.union(primeSet)

print(u)  # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
print(u2)  # {1, 2, 3, 5, 7, 9}
```

An **itersections** combines elements that are in both sets

```py
oddSet = {1, 3, 5, 7, 9}
evenSet = {0, 2, 4, 6, 8}
primeSet = {2, 3, 5, 7}

i = oddSet.intersection(evenSet)
i2 = oddSet.intersection(primeSet)
i3 = evenSet.intersection(primeSet)

print(i)  # set()
print(i2)  # {3, 5, 7}
print(i3)  # {2}
```

**Diffrence** this returns elements in the first set that are not in the second set

```py
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 11, 12, 13}

diff = setA.difference(setB)
diff2 = setB.difference(setA)

print(diff)  # {4, 5, 6, 7, 8, 9}
print(diff2)  # {11, 12, 13}
```

**symmetric_difference** returns a set with all elements that don't repeat in both sets

```py
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 11, 12, 13}

sym_diff = setA.symmetric_difference(setB)

print(sym_diff)  # {4, 5, 6, 7, 8, 9, 11, 12, 13}
```

To **update** a set

```py
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 11, 12, 13}

setA.update(setB)  # mutates intitial set

print(setA)  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13}
```

**intersection_update** this returns only items that are in both of the sets

```py
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 11, 12, 13}

setA.intersection_update(setB)

print(setA)  # {1, 2, 3}
```

**difference_update** updates a set by removing elements found in another set

```py
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 11, 12, 13}

setA.difference_update(setB)

print(setA)  # {4, 5, 6, 7, 8, 9}
```

**symmetric_diffrence_update** returns elements from both sets but not the ones found in both of the sets

```py
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 11, 12, 13}

setA.symmetric_difference_update(setB)

print(setA)  # {4, 5, 6, 7, 8, 9, 11, 12, 13}
```

**issubset** returns a Boolean . It checks if elements of the first set are all in the second set

```py
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3}

print(setA.issubset(setB))  # False
print(setB.issubset(setA))  # True
```

**issuperset** returns a Boolean. It checks if elements of second set are all in the first set

```py
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3}

print(setA.issuperset(setB))  # True
print(setB.issuperset(setA))  # False
```

**isdisjoint** returns a Boolean. It checks if the first set elements are not in the second set

```py
setA = {1, 2, 3, 4, 5, 6, 7}
setB = {1, 2, 3}
setC = {8, 9}

print(setA.isdisjoint(setB))  # False
print(setA.isdisjoint(setC))  # True
```
To copy a set we use **copy()** and **set()** methods
```py
setA = {1, 2, 3, 4, 5, 6, 7}
setB = setA.copy()
setC = set(setA)

print(setB)  # {1, 2, 3, 4, 5, 6, 7}
print(setC)  # {1, 2, 3, 4, 5, 6, 7}
```
##  Frozen set <br>
This is a set that is immutable.
```py
frozenSet = frozenset([1, 2, 3, 4, 5, 6, 7])

print(frozenSet)  # frozenset({1, 2, 3, 4, 5, 6, 7})
```

## Thanks for joining todays class
**Remember to practice all the learned concepts**