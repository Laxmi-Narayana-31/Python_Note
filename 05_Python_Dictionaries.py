mydict = {
    'Name':'Shiva',
    'Age':22,
    'City':'Berhampur'
}
print(mydict) # Output : {'Name': 'Shiva', 'Age': 22, 'City': 'Berhampur'}

# Dictionaries are used to store data in Key:Value pair
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates

'''
1. When we say that dictionaries are ordered, it means that the items have a defined order, and that order will not change.
2. Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.
3. It does allow duplicates.Dictionaries cannot have two items with the same key.
'''


# Dictionaries is also created by using dict() constructor
mydict = dict({
    'Name':'Shiva',
    'Age':22,
    'City':'Berhampur'
})
print(mydict)

# Access items by using Key name or using get() method
print("Key Name : ",mydict['Age'])  # Output: 22
print("Using Get Method : ",mydict.get('Name'))   # Output: Shiva

# Get Key of a dictionaries
x = mydict.keys()
print(x)


# Get Values of a dictionaries
y = mydict.values()
print(y)



# Change a dictionary item
mydict = dict({
    'Name':'Shiva',
    'Age':22,
    'City':'Berhampur'
})
mydict['Name'] = "Laxmi_Narayana"
print(mydict)


# Add a new iten
mydict = dict({
    'Name':'Shiva',
    'Age':22,
    'City':'Berhampur'
})
mydict['Country'] = "India"
print(mydict)


# del -> Delete an Item from Dictionary
del mydict['Age']
print(mydict)

# Note: del keyword also used to delete a dictionary completely
# del mydict
# print("Dictionary is:",mydict) # It gives an error because mydict is completed deleted from memory,so you cant print it 


# Check key is exist or not
if 'Name' in mydict:
    print("Yes")
else:
    print("No")


# update() -> Update the dictionary with the items from the given argument.
mydict = {
    'Name':'Shiva',
    'Age':22,
    'City':'Berhampur'
}
mydict.update({'Age':23})
print(mydict)


# pop() -> This method removes the item with the specified key name
mydict.pop('Name')
print(mydict)


# popitem() -> It removes the last inserted item 
mydict = {
    'Name':'Shiva',
    'Age':22,
    'City':'Berhampur'
}
mydict.popitem()
print(mydict)


# clear() -> Remove all items from a dictionary,only empties
'''mydict.clear()
print(mydict) # Output: {}'''


# Iteration
mydict = {
    'Name':'Shiva',
    'Age':22,
    'City':'Berhampur'
}
for i in mydict:
  print(i) # It will print the keys of the dictionary

for j in mydict:
    print(mydict[j])  # # It will print the values of dictionary
  
# values() -> to get all values 
# keys() -> to get all keys 
# items() -> to get both keys and value

for x in mydict.keys():
  print(x) # Output: Name Age City

for y in mydict.values():
  print(y) # Output: Shiva 22 Berhampur

for z in mydict.items():
    print(z) #Output: ('Name', 'Shiva') ('Age', 22) ('City', 'Berhampur')
                     


# Copy a dictionary 
new_dict = mydict.copy() # By using copy() method 
print(new_dict)

new_dict2 = dict(mydict) # By using dict() function 
print(new_dict2)


# Nested Dictionaries
nested_dict = {
    'person1': {'name': 'Shiva', 'age': 22},
    'person2': {'name': 'Sonu', 'age': 20},
    'person3': {'name': 'Amit', 'age': 23}
}
print(nested_dict['person1']['age'])  # Output: 22 (accessing the age of person1)


# fromkeys -> The fromkeys() method returns a dictionary with the specified keys and the specified value.
x = ('key1', 'key2', 'key3')
y = 0
thisdict = dict.fromkeys(x, y)
print(thisdict)