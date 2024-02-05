my_tuple = ('A','B','C','D','E','A','B')
print(my_tuple)

# it also created by using tupke constructor
tuple_ = tuple(('shiva','sonu','sumit','amit'))
print(type(tuple_))

# Duplicates are allowed in tuple
# It is index (0 based) based data types

# Tuples can contain different datatypes like string, integer etc.
# But it cannot be changed once created

# Tuple elements are immutable i.e., they cannot be modified after creation

print(my_tuple[1:6])

print(len(my_tuple))  # Length was 7
print(my_tuple[3])  # D
print(type(my_tuple))  # <class 'tuple'>

tuple = ("shiva")
print(type(tuple))  #  <class 'str'>

tuple = ("shiva",) # if you store a single elemnt in a tuple, just add a comma after element otherwise it treated as string in pyhton
print(type(tuple))   #  --> <class 'tuple'>


# check a specific present in the tuple or not (same in list)
new_tuple = ('a','b','c','d','e','f')
if('b' in new_tuple):
    print("Yes b exists in the tuple")
else:
    print("No b does not exist in the tuple")   


# Update the tuples -> if cant directly change tuples becaus eof immutability. if you want to change tuple are converted to lists then change the value again list is converted to tuples

x = ('A','B','C','D')
y = list(x)
y[1] = "Hello"
x = tuple(y)
print(x)


# Add items
# 1. Using append
# 2. Add two tuples 
# 1. Using append
demo_tuple = ('shiva','sonu','sumit','amit')
tuple_to_list = list(demo_tuple) # Type casting -> Tuple to List
print(type(tuple_to_list))  # class 'list'> -> List are mutable you change any items
print(tuple_to_list)

tuple_to_list.append('LaxmiNarayana')  # Add a new item in a list
print(tuple_to_list)

list_to_tuple = tuple(tuple_to_list)
print(list_to_tuple)


# 2. Add two tuples 
tuple1 = ('a','b','c','d','e')
tuple2 = ('hello','world')
new_tuple = tuple1 + tuple2
print(new_tuple)

# similarly you can delete any item from list using first method



# for item in demo_tuple:
#     if len(item)>4:
#         print(f"{item} has more than four letters.")
#     else:
#         print(f"{item} has less than or equal to four letters.") 


# Unpacking a tuple:

fruits = ("apple", "banana", "cherry")

(shiva, sonu, amit) = fruits

print(shiva)
print(sonu)
print(amit)


# Nested Tuples
nested_tuples = (("Apple","Banana"),("Cherry","Durian"))
for tup in nested_tuples:
    print(tup[0])
    print(tup[1])
    # Accessing elements of nested tuples
    print(tup[0][0],tup[0][1])
    print(tup[1][0],tup[1][1])


# Iterate a Tuple
my_tuple = (1,2,3,4,5)
print(len(my_tuple))
for i in my_tuple:
    print(i)

for j in range(len(my_tuple)):
    print(j)



# Multiply Tuples
Tuple = ('shiva','sumit','amit')
new_Tuple = Tuple * 2
print(new_Tuple) # ('shiva', 'sumit', 'amit', 'shiva', 'sumit', 'amit')

print(new_Tuple.count('shiva')) # It returns number of times a specified value appears

print(new_Tuple.index('sumit'))

# Nesting Tuples
nested_tuple = ((1, 2), (3, 4), (5, 6))
print(nested_tuple[1][0])  # Output: 3 (accessing the first element of the second inner tuple)


# Tuple Method
# count(): Returns the number of occurrences of the specified element
my_tuple = (1, 2, 3, 1, 4, 1, 5)
count_of_1 = my_tuple.count(1)
print(count_of_1)  # Output: 3

# index(): Returns the index of the first occurrence of the specified element 
my_tuple = (10, 20, 30, 20, 40)
index_of_20 = my_tuple.index(20)
print(index_of_20)  # Output: 1