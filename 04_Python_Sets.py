#Set = {1,2,3,4,5,6,7}
# It does not allow duplicate values
# Set items are unchangeable, but you can remove items and add new items
# Sets are unordered, so you cannot be sure in which order the items will appear

#thisset = {'a','B','abc', 10, 10.7, True} # it contain differnt data types
#print(thisset)

# Set is also created by suing set() constructor
'''myset = set((1,2,3,4,5,6))
print(type(myset))'''

# Set are not index based
# You cannot access elements of a set using an index like list or tuple

'''Once a set is created, you cannot change its items, but you can add new items.'''

'''Prgra_Lang = {'Java','C','JavaScript','C#','C++'}
Prgra_Lang.add('Python')
print(Prgra_Lang)'''

# update() -> To add items from another set into the current set
'''name = {'shiva','amit','sonu','sumit'} 
name1 = {'LaxmiNarayana', 'Ram','Krishna'}
name.update(name1)
print(name)'''

# update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.)
'''name = {'shiva','amit','sonu','sumit'} 
name1 = ['LaxmiNarayana', 'Ram','Krishna']
name.update(name1)
print(name)
'''

#remove() or discard() -> to remove item from set. If the item to remove does not exist, remove() will raise an KeyError.But discard() will not raise any error
'''name2 = {'a','b','c','d','e'}
name2.remove('c')
print(name2)'''

# pop() -> Remove a random item from the set
'''name3 = {'shiva','amit','sonu','sumit'} 
item = name3.pop()
print(item)
print(name3)'''

# clear() -> remove all element from a set
'''name3.clear()
print(name3)  # Output: set()'''

# Iterate a set 
'''city = {'BBSR','Delhi','Hyderbad','Mumbai','Banglore'}
for citynames in city:
    print(citynames)'''


# Join sets
'''set1 = {1,2,3}
set2 = {3,4,5}
set3 = set1.union(set2)   # Union operation returns a new set with unique elements from both sets
print(set3)  # Output: {1, 2, 3, 4, 5}'''


# Update set
'''set1.update({6,7})
print(set1)  # Output: {1, 2, 3, 6, 7}'''


# Intersection of two sets
'''set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}
set3 = set1.intersection(set2)  # Returns a new set that contains common items between two or more sets
print(set3)  # Output: {4, 5}


# Difference of two sets
set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}
set3 = set1.difference(set2)  # Returns a new set that contains items that are only in first set and not present
print(set3)  # Output: {1, 2, 3}'''


# symmetric_difference : This method will keep only the elements that are NOT present in both sets.
'''set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}
set3 = set1.symmetric_difference(set2)
print(set3)  # Output: {1, 2, 3, 6, 7, 8}

set4 = set1.symmetric_difference_update(set2)
print(set4)  # Output: {}'''


# Note: The values True and 1 are considered the same value in sets, and are treated as duplicates
'''set1 = {'A','B','ABC',True}
set2 = {'B','C','Hello',1}
set3 = set1.symmetric_difference(set2)
print(set3)

# isdisjoint -> True if no common item and returns false if common item are there 
print(set1.isdisjoint(set2)) ''' 


# Checking subset and superset
set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}
print(set1.issubset(set2)) # True if set1 is completely contained within set2

print(set1.issuperset(set2)) # True if set1 contains all the elements present in set2



# Nested sets
nested_set = {frozenset({1, 2}), frozenset({3, 4}), frozenset({5, 6})}
for inner_set in nested_set:
    print(inner_set)
# Output: frozenset({1, 2})
#         frozenset({3, 4})
#         frozenset({5, 6})


# Frozen set
'''frozenset is an immutable, hashable set. Unlike regular sets, frozenset objects cannot be modified once they are created. This immutability allows frozenset objects to be used as keys in dictionaries and elements in other sets, providing a hashable and unchangeable representation of a set of values.'''
fs = frozenset([1, 2, 3, 4, 5])
print(fs)  # Output: frozenset({1, 2, 3, 4, 5})


'''frozenset objects are immutable, so you cannot perform operations that modify the set. However, you can perform various non-modifying set operations on frozenset'''

# Create two frozensets
fs1 = frozenset([1, 2, 3, 4, 5])
fs2 = frozenset([3, 4, 5, 6, 7])

# Intersection of frozensets
intersection = fs1 & fs2
print("Intersection:", intersection)  # Output: frozenset({3, 4, 5})


# Union of frozensets
union = fs1 | fs2
print("Union:", union)  # Output: frozenset({1, 2, 3, 4, 5, 6, 7})


# Difference of frozensets
difference = fs1 - fs2
print("Difference:", difference)  # Output: frozenset({1, 2})


# Check if fs1 is a subset of fs2 and if fs2 is a superset of fs1
is_subset = fs1.issubset(fs2)
is_superset = fs2.issuperset(fs1)
print("Is fs1 a subset of fs2?", is_subset)  # Output: True
print("Is fs2 a superset of fs1?", is_superset)  # Output: True
