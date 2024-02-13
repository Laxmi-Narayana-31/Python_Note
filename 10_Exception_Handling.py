'''Exception : A unwanted or unexpected event which occurs during the execution of prograom that is run time.
in Python, we use try and except block to handle the exception.


Syntax:
try:
    //code segment where an exception can occur
except [Exception type]:
    //code segment to be executed if there is an exception in the code above'''
    
try:
    x = 10 / 2
    print(x)
except:
    print("An error occurred")
finally:
    print("hello")


# You also use Else block with try except block.
try:
    x = 10 / 0
except:
    print("Raise an exception")
else:
    print("It always executed")



try:
    # some code that may raise an exception
    x = 1 / 0
except Exception as e:
    # print the type of the exception
    print(type(e))




# finally block:  if specified, will be executed regardless if the try block raises an error or not.
try:
    x = 10 / 2
    y = 5 / 0
except ZeroDivisionError as e:
        print('A division by zero occurred')
finally:
        print('This is the end!')



# You can manually throw or raise an exception by using the "raise" keyword.
a = -10
if a < 0:
    raise Exception("The no is negative number")