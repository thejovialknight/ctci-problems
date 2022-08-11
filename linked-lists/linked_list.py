"""
This is an implementation of a linked list. Obviously.
"""

class Node:
    next_node = None
    data = 0

    def __init__(self, d):
        self.data = d

# Just a wrapper for a linked list node, in case the head is deleted
class LinkedList:
    head = None

    def __init__(self, d):
        self.head = Node(d)

    # Appends a new node to the tail end of the linked list
    def append(self, d):
        if head == None:
            head = Node(d)
            return

        # current iterates through list until it finds the end
        current = head
        while current.next_node != None:
            current = current.next_node

        current.next_node = Node(d)

    # Prepends a new node to the head of the linked list
    def prepend(self, d):
        new_head = Node(d)
        new_head.next = head
        head = new_head

    # Deletes the first node that matches the data value if it exists
    def delete_with_value(self, d):
        if head == None return
        if head.data == d:
            head = head.next_node
            return
        
        current = head
        while current.next_node != None:
            if current.next_node.data == d:
                current.next_node = current.next_node.next_node
                return
            current = current.next

