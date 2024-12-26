# Linked List Implementation in Python

This repository contains a Python implementation of a Singly Linked List, providing core functionalities such as adding, deleting, and accessing elements, as well as calculating the length of the list. 

## Features

The LinkedList class supports the following operations:

`Append:` Add a new element to the end of the linked list.
`Display:` Print the elements of the linked list.
`Length:` Calculate and return the total number of elements in the linked list.
`Get: `Retrieve the value of an element at a specified index.
`Delete:` Remove an element from the linked list by its value.

## Code Description

`Node Class`
Represents an individual element (node) in the linked list.

`LinkedList Class`
Handles operations on the linked list.

## Methods in `LinkedList`

`append(data)`

Adds a new element to the end of the linked list.
Parameters: data - the value to add.

`display()`

Prints the elements of the linked list in a readable format.

`length()`

Calculates and returns the total number of elements in the linked list.

`get(index)`

Retrieves the value of the element at a specified index.
Parameters: index - the position of the element to retrieve.

`delete(key)`

Removes an element from the linked list by its value.
Parameters: key - the value of the element to delete.

## Common Errors and Fixes
- Index Out of Range in get Method:

Ensure the length method properly calculates and returns the size of the list.
Fix: Ensure length has a return statement and is called correctly.
- Empty List Handling:
Methods like display and get handle cases where the list is empty by checking if self.head is None.