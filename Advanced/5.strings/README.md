# **30 days of Advanced Python Concepts**

## 5. Strings <br>

This are immutable collection data types that are used to represent words.

```py
my_string = "Hello world!"

my_multiline_string = """
    Hello world this is a multiline string
    It spans more than a single line
    It is sometimes used for documentations
"""
my_other_string = """ Hello  other \
    world!
"""
print(my_string)
print(my_multiline_string)
print(my_other_string)  # Prints on a single line
```

You can get a single character from a string by indexing it

```py
my_string = "Hello world!"

print(my_string[0]) # H
```

You can also **iterate** through a string

```py
my_string = "Hello world!"

for i in my_string:
    print(i)  # this prints each character onto a new line
```

To check if a character is in a string

```py
my_string1 = "Hello World"

if 'H' in my_string1:
    print("True")
else:
    print("False")

if 'Hell' in my_string1:
    print("True")
else:
    print("False")
```

**Substrings** can be printed by splitting the string

```py
my_string = "Hello world!"

print(my_string[:])  # Hello World!
print(my_string[2:])  # llo world!
print(my_string[:6])  # Hello
print(my_string[2:6])  # llo
print(my_string[:-3])  # Hello wor
print(my_string[2:-3])  # llo wor
print(my_string[::-2])  # !lo le
print(my_string[::2])  # Hlowrd
print(my_string[::-1])  # !dlrow olleH
```

To **concatenate strings** we use the **+** operator

```py
my_string1 = "Hello "
my_string2 = "World!"
name = "Tom"

joined_string = my_string1+my_string2

print(joined_string)  # Hello World!
print(my_string1 + " " + name + ".")  # Hello  Tom.
```

**strip()** removes **trailing whitespaces** in a string. It does not mutate the string but returns <br> a new string with no trailing whitespaces

```py
my_string1 = "   Hello World    "

my_string1.strip()
print(my_string1)  #    Hello World

my_string1 = my_string1.strip()
print(my_string1)  # Hello World
```

**Lower, UpperCase and Capitalize**

```py
lowerString = "hello"
upperString = "HELLO"

print(lowerString.upper())  # HELLO
print(upperString.lower())  # hello
print(lowerString.capitalize())  # Hello
```

Other string methods

```py
string = "Hello World"

print(string.startswith("Hello"))  # True
print(string.endswith("World"))  # True
print(string.find('W'))  # 6  index of W
print(string.find('z'))  # -1  did not find the character in the string
print(string.count('o'))  # 2
print(string.replace("World", "Universe"))  # Hello Universe

```

Converting a **string to a list and vice** versa

```py
string = "Hello World Im new here"
myList = ['Hello', 'World', 'Im', 'new', 'here']

print(string.split(" "))  # ['Hello', 'World', 'Im', 'new', 'here']
print(' '.join(myList))  # Hello World Im new here

```

Creating a **string** by iterating using a **for loop** This is not recommended you should <br> use the **join()** method above instead

```py
myList = ['a']*6
print(myList)  # ['a', 'a', 'a', 'a', 'a', 'a']

myString = ""
for i in myList:
    myString += i

print(myString)  # aaaaaa
```

The above can be proven by using a very large list

```py
from timeit import default_timer as timer

myList = ['a']*1000000
myString = ""

start = timer()
for i in myList:
    myString += i

stop = timer()
print(stop-start)  # 0.1461673449994123

newtime = timer()
myString = "".join(myList)
endtime = timer()

print(endtime-newtime)  # 0.010144050998860621
```

String formating using **modulus** operator, **.formart()** method and **f string**

```py
var = "John"
my_string = "My name is %s" % var

print(my_string)  # My name is John
print("My name is {}".format(var))  # My name is John

num = 19
my_other_string = "I'm %d years old" % num

print(my_other_string)  # I'm 19 years old
print(f"I'm {num} years old.")  # I'm 19 years old

floating_num = 3.14367544
print("This number to two decimal places is {:.2f} ".format(floating_num)) # 3.14

print("Several varibles {} {}".format(var, my_other_string))  # Several varibles John I'm 19 years old
```
## Thanks for joining todays class
**Remember to practice the concepts you learned today**