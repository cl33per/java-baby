# Cody Leeper aka CodyCodes
# CSC200 2020
# Palindrom Project

# Run and enter main() to start program

# Algorithm
# Import stack.py

import stack
import queue

def main():
  programIntroduction()
  # Create as stack and a queue
  myStack = stack.newStack()
  myQueue = queue.newQueue()
  # Get a word from input
  word = input('Enter a word:')
  # Set up a loop where you extract each character from the word
  for i in word:
    # Push the character onto the stack
    stack.push(myStack,i)
    # Insert the character into the queue
    queue.insert(myQueue,i)
  # Create a variable called isPalindrome and initialize it to True
  isPalindrome = True
  # Set up a second loop to extract characters from the stack and queue
  for i in word:
    # print (f'StackIsEmpty: {stack.isEmpty(myStack)}')
    # print (f'QueueIsEmpty: {stack.isEmpty(myQueue)}')
    if stack.isEmpty(myStack) or queue.isEmpty(myQueue) == False:
      stackChar = stack.remove(myStack)
      queueChar = queue.remove(myQueue)
      # print(f'Stack: {myStack}')
      # print(f'Queue: {myQueue}')
      if stackChar != queueChar:
        # Set the isPalindrome variable to false
        isPalindrome = False
      # print(f'isPlaindrome: {isPalindrome}')
  # Break out of the loop
  # If the isPalindrome variable is True
  if isPalindrome == True:
    # Print the message “is a palindrome”
    print(f'{word} is a palindrome')
  # else
  else:
    # Print the message “is not a palindrome”
    print(f'{word} is not a palindrome')
  # call introduction function

def programIntroduction():
  print("Welcome to the Palindrom Program \n ")
  print("Test Cases are as follows: ")
  print("dad, sad, bob, mom, mommy, car, racecar: ")
  print("dad is a palindrome,\n sad is not a palindrome,\nbob is a palindrome,\nmom is a palindrome,\nmommy is not a palindrome,\ncar is not a palindrome,\nracecar is a palindrome: ")