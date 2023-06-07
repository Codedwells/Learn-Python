# **30 days of Advanced Python Concepts**

## 3. Dictionaries <br>

Dictionary is a collection data type that consists of key-value pairs and is mutable

```py
myDict = {
    "name": "Jayson",
    "location": "Nairobi",
    "age": 19
}

myOtherDict = dict(name="Jayson", location="Nairobi", age=19)

print(myDict)  # {'name': 'Jayson', 'location': 'Nairobi', 'age': 19}
print(myOtherDict)  # {'name': 'Jayson', 'location': 'Nairobi', 'age': 19}
```

To get a Value you use its key

```py
myDict = {
    "name": "Jayson",
    "location": "Nairobi",
    "age": 19
}

print(myDict['name'])  # Jayson
```

To add a new Key-Value pair

```py
myDict = {
    "name": "Jayson",
    "location": "Nairobi",
    "age": 19
}

myDict["email"] = "jaysonmail@gmail.com"
print(myDict['email'])  # jaysonmail@gmail.com

```

To delete a key and its value in the dictionary we use the **del** or **pop** keyword

```py
myDict = {
    "name": "Jayson",
    "location": "Nairobi",
    "age": 19,
    "email": "jaysonmail@gmail.com",
    "occupation": "software engineer",
    "rank": "juniur"
}

del myDict["email"]
myDict.pop("name")
myDict.popitem()  # removes the last element

print(myDict)  # {'location': 'Nairobi', 'age': 19, 'occupation': 'software engineer'}
```

To check if an item is present in our dictionary

```py
myDict = {
    "name": "Jayson",
    "location": "Nairobi",
    "age": 19,
    "email": "jaysonmail@gmail.com",
    "occupation": "software engineer",
    "rank": "juniur"
}

if "name" in myDict:
    print(myDict["name"])  # Jayson

try:
    print(myDict["height"])
except:
    print("Key not found in specified dictionary")  # Key not found in specified dictionary
```

To print key and values of a dictionary using a for loop

```py
myDict = {
    "name": "Jayson",
    "location": "Nairobi",
    "age": 19,
    "email": "jaysonmail@gmail.com",
    "occupation": "software engineer",
    "rank": "junior"
}

for key, value in myDict.items():
    print(key, '-', value)
```

To make a copy of a dictionary

```py
myDict = {
    "name": "Jayson",
    "location": "Nairobi",
    "age": 19,
    "email": "jaysonmail@gmail.com",
    "occupation": "software engineer",
    "rank": "junior"
}

mySecondDict = myDict.copy()
myThirdDict = dict(myDict)

print(mySecondDict)
print(myThirdDict)
```

To update a key value in a dictionary we use **update** key word

```py
myDict = {
    "name": "Jayson",
    "location": "Nairobi",
    "age": 19,
}

mySecondDict = {"name": "Adeola"}
myDict.update(mySecondDict)

print(myDict)  #{'name': 'Adeola', 'location': 'Nairobi', 'age': 19}

```
You can also use numbers as key and use these numbers when accessing their values
```py
myDict = {
    1: "Jayson",
    2: "Nairobi",
    3: 19,
}

print(myDict[2])  # Nairobi
```

## Thank you for joining todays class
**Don't forget to practice**
