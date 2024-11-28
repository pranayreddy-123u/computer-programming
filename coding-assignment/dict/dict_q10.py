# How do you sort a dictionary by its keys or values?
my_dict = {'b': 3, 'a': 1, 'c': 2}
sorted_by_keys = dict(sorted(my_dict.items()))
print(sorted_by_keys) 
sorted_by_values = dict(sorted(my_dict.items(), key=lambda item: item[1]))
print(sorted_by_values) 

