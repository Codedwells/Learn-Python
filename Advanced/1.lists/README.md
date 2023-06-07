# **30 days of Advanced Python Concepts**

## 1. Lists <br>

```py
first_list = ['mary', 'john', 'Kendrick', 'Tommy']

second_list = list()
```

Lists are mutable collection data types which can store diffrent data types.<br>
To **print items** of a list we can iterate through using a for loop.

```py
first_list = ['mary', 'john', 'Kendrick', 'Tommy']

for i in first_list:
    print(i)
```

To check for items in out list

```py
first_list = ['mary', 'john', 'Kendrick', 'Tommy']

if "mary" in first_list:
    print("yes")
else:
    print("No")

```

To check the **length** of out list

```py
first_list = ['mary', 'john', 'Kendrick', 'Tommy']

print(len(first_list))  # 4
```

To append i.e **add items** to the end of our list

```py
second_list = list()

second_list.append("Lemon")
print(second_list)  #['Lemon']
```

To **insert an item **into a list we use this syntax which specifies the
index to insert the item stated.

```py
first_list.insert(1, "Jayson")
print(first_list[1]) # This prints Jayson
```

To **remove elements** from a list

```py
first_list = ['mary', 'john', 'Kendrick', 'Tommy']
second_list = list()

first_list.pop()  # Removes the last element
first_list.remove("Mary")  # This removes Mary from the list
second_list.clear()  # This clears the whole list
```

To **reverse** a list

```py
first_list = ['mary', 'john', 'Kendrick', 'Tommy']
first_list.reverse()

print(first_list)  #['Tommy', 'Kendrick', 'john', 'mary']
```

To **sort** a list

```py
number_list = [2, 5, 32, 1, 24, 3, 25]
number_list.sort()
sorted_list = sorted(number_list)

print(number_list, sorted_list)  #[1, 2, 3, 5, 24, 25, 32] [1, 2, 3, 5, 24, 25, 32]
```

Shorthand to create a list with similar item

```py
more_item_list = ["item"]*5

print(more_item_list)  # ['item', 'item', 'item', 'item', 'item']
```

To **concatenate** two lists together

```py
more_item_list = ["item"]*5
concat_list = ["new"]*4

joined_list = more_item_list + concat_list
print(joined_list)  # ['item', 'item', 'item', 'item', 'item', 'new', 'new', 'new', 'new']
```

To print a section of a list you specify the start index and the stop index

```py
my_list = [1, 12, 3, 4, 6, 8]
a = my_list[1:4]

print(a)  #[12, 3, 4]
```

This prints from start index to end of the list since no stop index has been declared

```py
my_list = [1, 12, 3, 4, 6, 8]
a = my_list[1:]

print(a)  #[12, 3, 4, 6, 8]
```

You can also specify a step index and it picks item in the **stepped indices**

```py
my_list = [1, 12, 3, 4, 6, 8]
a = my_list[::2]

print(a)  # [1, 3, 6]
```

You can use step index as a trick to **reverse** you list

```py
my_list = [1, 12, 3, 4, 6, 8]
a = my_list[::-1]

print(a)  # [8, 6, 4, 3, 12, 1]
```

To make **copies** of a list

```py
list_org = [3, 4, 5, 6]
list_copy1 = list_org.copy()
list_copy2 = list(list_org)
list_copy3 = list_org[:]  # slice method

print(list_org, list_copy1, list_copy2, list_copy3)
# [3, 4, 5, 6] [3, 4, 5, 6] [3, 4, 5, 6] [3, 4, 5, 6]
```

**List comprehension** - create a mutated copy of the original list using a one liner

```py
list_org = [3, 4, 5, 6]
a = [i*2 for i in list_org]

print(a)  # [6, 8, 10, 12]

```

## Thanks for joining todays class 
**Remember to practice** *practice makes perfect
*