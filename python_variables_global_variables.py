# Global Variables
# # Create a variable outside of a function, and use it inside the function
x = "awesome"


def myfunc():
    print("Python is " + x)


myfunc()  # Python is awesome

# # Create a variable inside a function, with the same name as the global variable
x = "awesome"


def myfunc():
    x = "fantastic"
    print("Python is " + x)


myfunc()  # Python is fantastic

print("Python is " + x)  # Python is awesome

# The global Keyword
# # If you use the global keyword, the variable belongs to the global scope:


def myfunc():
    global x
    x = "fantastic"


myfunc()

print("Python is " + x)  # Python is fantastic

# # To change the value of a global variable inside a function, refer to the variable by using the global keyword:
x = "awesome"


def myfunc():
    global x
    x = "fantastic"


myfunc()

print("Python is " + x)  # Python is fantastic
