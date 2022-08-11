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

# We create a hashtable that holds our found items, always set to true
# We iterate through the list, adding each data to the hashtable if not found
# and deleting it from the linked list if it is found (in the hashtable)
# This is a time complexity of O(n) and a worst case space complexity of O(n)
def remove_duplicates(l):
    if l.head == None return
    seen = {}
    current = l.head
    while current.next_node != None:
        next_data = current.next_node.data
        if next_data not in seen:
            seen[next_data] == None
        else
            current.next_node = current.next_node.next_node
        current = current.next_node

# We do two while loops to check every pair of items, removing duplicates as we go
# This is to avoid the space complexity of the previous solution, but it comes at a cost
# The time complexity is O(n^2) now, while the space complexity is nonexistent
def remove_duplicates_without_temp(l):
    if l.head == None return
    current = l.head
    while current.next_node != None:
        current_match = current
        while current_match.next_node != None:
            if current.next_node.data == current_match.next_node.data:
                current_match.next_node = current_match.next_node.next_node
            current_match = current_match.next_node

        current = current.next_node

# This is all unfinished I just don't want to think about it
