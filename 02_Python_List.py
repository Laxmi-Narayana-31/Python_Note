# List is one of data type in python that enclose with square brackets.

"""Python Collections (Arrays)
There are four collection data types in the Python programming language:

List -> It is a collection which is ordered and changeable. Allows duplicate members.

Tuple -> It is a collection which is ordered and unchangeable. Allows duplicate members.

Set -> It is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.

Dictionary -> It is a collection which is ordered** and changeable. No duplicate members."""


# It can store multiple values of same or different types.
#list = [1,9.7,'a','b'] # list contains 4 elements which are integers and strings respectively.

"""     list =         ['shiva','sonu','amit','shiva'] 
    Indexing =              0      1      2       3
Negative Indexing =        -4     -3     -2      -1"""

# list = ['shiva','sonu','amit','shiva'] 
# print(list)
# print(type(list))
# print(f"List : {list}")  # Output-> List : ['shiva', 'sonu', 'amit', 'shiva]

# Nested Lists
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(nested_list[0][1])  # Output: 2 (accessing the element at index 1 of the first inner list)


# List follow Indexing that starts from 0
# List allow duplicate values.
# List does not have a fixed size like array but it has dynamic size.
# List are follow Ordered means item have a defined order, and that order wil not change, if you add a new elemnt in list placed at end.abs

# List length
"""
list = ['shiva','sonu','amit','shiva'] 
print("Length of the list: ",len(list))
# Access element by index
print("Element at index 1:",list[1])
print("Element at index -2:",list[-4])

# Range
print('Elements between indices 1(included) & 3(excluded): ',list[1:3])  

# name existance
if "sonu" in list:
    print("name exists")
    index = list.index('sonu')
    print("name index was",index)
else:
    print("name doesn't Exist!")
"""


# change item
mylist = ['a','b','c','d','e']
mylist[2] = 'shiva'
print(mylist)



# append() -> add an element to the end of a list.
fruits = ["apple", "banana", "orange"] 
fruits.append("mango") 
print(fruits)


# copy() -> used to create a shallow copy of a list.
my_list = [1, 2, 3, 4, 5] 
new_list = my_list.copy() 
print(new_list)  # Output: [1, 2, 3, 4, 5]


# count() -> used to count the number of occurrences of a specific element in a list
my_list = [1, 2, 2, 3, 4, 2, 5, 2] 
count = my_list.count(2) 
print(count)  # Output: 4

# del() -> removes the element at the specified index.
my_list = [10, 20, 30, 40, 50] 
del my_list[2] # Removes the element at index 2 print(my_list) 
# Output: [10, 20, 40, 50]


# insert() -> insert an element | my_list.insert(index,element)
my_list = [1, 2, 3, 4, 5] 
my_list.insert(2, 6) 
print(my_list)


# extend() -> used to add multiple elements to a list.
fruits = ["apple", "banana", "orange"] 
more_fruits = ["mango", "grape"] 
fruits.extend(more_fruits) 
print(fruits)

# pop() -> It removes and returns the element at the specified index. If you don't provide an index to the `pop()` method, it will remove and return the last element of the list by default
my_list = [10, 20, 30, 40, 50] 
removed_element = my_list.pop() # -> defaultly remove the last element of the list.
print(removed_element)
print(my_list)


my_list = [10, 20, 30, 40, 50] 
removed_element1 = my_list.pop(2) # Removes and returns the element at index 2 
print(removed_element1) 
# Output: 30 

print(my_list) 
# Output: [10, 20, 40, 50] 


#remove() -> removes the first occurrence of the specified value.
my_list = [10, 20, 30, 40, 50] 
my_list.remove(30) # Removes the element 30 
print(my_list) 
# Output: [10, 20, 40, 50]


# reverse() -> reverse the order of elements of the list
my_list = [10, 20, 30, 40, 59 ]
my_list.reverse()
print(my_list)


# slicing -> You can use slicing to access a range of elements from a list.
my_list1 = ['A', 'B', 'C', 'D', 'E'] 
print(my_list1[1:4]) 
# Output: [B, C, D] (elements from index 1 to 3)

print(my_list1[:3]) 
# Output: [A, B, C] (elements from the beginning up to index 2) 

print(my_list1[2:]) 
# Output: [C, D, E] (elements from index 2 to the end) 

print(my_list1[::2]) 
# Output: [A, C, E] (every second element)


# sort() -> sort the list elements in ascending or descending order
# Ascending rder
my_list = [5, 2, 8, 1, 9] 
my_list.sort() 
print(my_list)   # Output: [1, 2, 5, 8, 9] 


# Descending order
my_list = [5, 2, 8, 1, 9] 
my_list.sort(reverse=True) 
print(my_list)   # Output: [9, 8, 5, 2, 1]








