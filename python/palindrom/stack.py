  # Cody Leeper aka CodyCodes
# CSC200 2020
# Palindrom Project

# This is a supporting file. stack.py is called in main.py

# This function creates an empty list and returns it to the calling function. The empty
# list will hold the stack items.
def newStack():
  stack = []
  return stack

# This function takes the stack and the item to be added to the stack as
# parameters. It then appends the item to the end of the list. This is a void function with no return
# value because the list is passed by reference and can be modified directly by the function.
def push(stack, item):
  stack.append(item)

# This function removes the item at the top of the stack and returns it. The built-in
# Python list ADT has a function called pop, when called with no parameters, it returns the last
# item in the list. This is the behavior we want from the stack.
def remove(stack):
  return stack.pop()

# This function takes the stack as an input. It checks to see if the stack is empty
# and returns True if it is empty and False if it is not empty. You can use the Python built-n
# function len to get the length of the list. If it is 0, the stack is empty.
def isEmpty(stack):
  if len(stack) != 0:
    return False
  else:
    return True

# Document your module using comments that list each function and briefly describes what input
# the function needs (preconditions) and what the function returns (the postcondition).