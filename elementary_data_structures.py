""" Implementation and Analysis of Elementary Data Structures """

import timeit

class Array:
    """ Implementation of Array using Python lists """
    def __init__(self):
        self.array = []

    def insert(self, value):
        """ Insert value at the end of array """
        self.array.append(value)            # Takes O(1) time

    def delete(self, value):
        """ Delete the value from the array list """
        if value in self.array:
            self.array.remove(value)        # Remove the first occurrence (O(n)) worst case

    def access(self, index):
        """ Return the value at given index from the array """
        if 0 <= index < len(self.array):
            return self.array[index]        # Access element at given index (O(1))
        else:
            raise IndexError("Index out of bounds")

class Stack:
    """ Implementation of stack using array """
    def __init__(self):
        self.stack = []

    def push(self, value):
        """ Push the value in the end of stack """
        self.stack.append(value)        # Push operation (O(1))

    def pop(self):
        """ Pop the value from the end of stack and return it"""
        if len(self.stack) != 0:
            return self.stack.pop()     # Pop operation (O(1))
        else:
            raise IndexError("Stack is empty")

class Queue:
    """ Implementation of queue using array """
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        """ Add the value in the end of queue """
        self.queue.append(value)        # Add at the end of the list (O(1))

    def dequeue(self):
        """ Remove the value from the beginning of queue and return it"""
        if len(self.queue) != 0:
            return self.queue.pop(0)    # Remove the first element and shift rest of elements (O(n))
        else:
            raise IndexError("Queue is empty")

class Node:
    """ Single node class to be used in linked list """
    def __init__(self, data):
        self.data = data                # Store value in the data
        self.next = None                # Pointer to next node

class SinglyLinkedList:
    """ Implementation of singly linked list """
    def __init__(self):
        self.head = None

    def insert(self, value):
        """ Insert the new value at the beginning of the list """
        new_node = Node(value)          # Create new node with the given value
        new_node.next = self.head
        self.head = new_node            # Insert at the head of list (O(1))

    def delete(self, value):
        """ Delete the first node that contain the given value """
        current_node = self.head        # Start at the head of the list
        prev_node = None

        while current_node:
            if current_node.data == value:              # If the node is found
                if prev_node:
                    prev_node.next = current_node.next  # Skip the current node and point to next node
                else:
                    self.head = current_node.next       # Update the head if the value is in head node
                return
            prev_node = current_node
            current_node = current_node.next            # Move to next node if value is not found

    def traverse(self):
        """ Traverse through the entire linked list and return the value of all nodes """
        values = []
        current_node = self.head                # Start at the head of the list

        while current_node:
            values.append(current_node.data)    # Store the node values in the list
            current_node = current_node.next    # Move to next node until the end of the list

        return values

def print_execution_times(function, value):
    """ Function to print execution times """
    if value is not None:
        timer_stmt = '''{0}({1})'''
        times = timeit.repeat(stmt=timer_stmt.format(function, value), repeat=2, number=10000, globals=globals())
    else:
        timer_stmt = '''{0}()'''
        times = timeit.repeat(stmt=timer_stmt.format(function), repeat=2, number=10000, globals=globals())
    print('Total execution time: ' + str(min(times)))

array = Array()
stack = Stack()
queue = Queue()
linked_list = SinglyLinkedList()

# Performance Analysis of Elementary Data Structures
print("INSERTION TIME:")
print("Array Insertion Time", end= " --> ")
print_execution_times("array.insert", 36)
print("Stack Push Time", end= " --> ")
print_execution_times("stack.push", 36)
print("Queue Enqueue Time", end= " --> ")
print_execution_times("queue.enqueue", 36)
print("Linked List Insertion Time", end= " --> ")
print_execution_times("linked_list.insert", 36)

print("\nACCESSING TIME:")
print("Array Accessing Time", end= " --> ")
print_execution_times("array.access", 0)

print("\nDELETION TIME:")
print("Array Deletion Time", end= " --> ")
print_execution_times("array.delete", 36)
print("Stack Pop Time", end= " --> ")
print_execution_times("stack.pop", None)
print("Queue Dequeue Time", end= " --> ")
print_execution_times("queue.dequeue", None)
print("Linked List Deletion Time", end= " --> ")
print_execution_times("linked_list.delete", 36)
