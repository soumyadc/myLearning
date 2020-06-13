# string
---
string is like list[] with characters as its element of that list 

# list
---
list = [ ] 
list.append(<val>)
len(list)
slice_list = list [<start_idx> : <till_before_idx>]
idx = list.index(<val>)
list.insert(<idx>, <val>)
list.sort()
list.remove('val')
list.pop(<idx>)
del(list[idx])

# Dictionary
---
dict = {}
dict = {'key1': 1, 'key2': 2, 'key3': 3 }
lookup is done using the key instead of index

len(<dict>) 
number of keys-value pair in the dictionary

del dict['key']
delete a key-value pair from the dictionary

dict.keys()

for key in dict:
    print key
    value= dict[key]
    print value
