from collections import Counter

a = "aaaaabbbbccc"
my_counter = Counter(a)

print(my_counter.items())  # dict_items([('a', 5), ('b', 4), ('c', 3)])
print(my_counter.keys())  # dict_keys(['a', 'b', 'c'])
print(my_counter.values())  # dict_values([5, 4, 3])

print(my_counter.most_common(1)[0][0])   # a
print(my_counter.most_common(2))  # [('a', 5), ('b', 4)]
print(list(my_counter.elements())) # ['a', 'a', 'a', 'a', 'a', 'b', 'b', 'b', 'b', 'c', 'c', 'c']