# This function creates an empty list and returns it to the calling function. The empty
# list will hold the queue items
def newQueue():
  queue = []
  return queue

# This function takes the queue and the item to be added to the queue as
# parameters. It then appends the item to the end of the list. This is a void function with no return
# value because the list is passed by reference and can be modified directly by the function.
def insert(queue, item):
  queue.append(item)

# This function removes the item at the beginning of the queue and returns it.
# The built-in Python list ADT pop function can again be used, except, pass it a parameter of 0 and
# it will return the item at the beginning of the list rather than from the end of the list
def remove(queue):
  return queue.pop(0)

# This function takes the queue as an input. It checks to see if the queue is
# empty and returns True if it is empty and False if it is not empty. You can use the Python built-n
# function len to get the length of the list. If it is 0, the queue is empty.
def isEmpty(queue):
  if len(queue) != 0:
    return False
  else:
    return True