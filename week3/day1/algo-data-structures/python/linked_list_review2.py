# Linked list is a chain of node objects
# A 'node' is the name we use for a thing in the list


# What can we do with a linked list?
# Insert node / create new node
# Delete node
# Find a node --> traverse the list
# Replace a node
    # This is a more sophisticated operation


# Two special nodes in the linked list:
    # Head --> first node in the list
        # We need access to the head so we have access to the list
    # Tail --> last node in the list
        # We need to know which node is the tail so we know when to stop

# value
# pointer to the next node in the list


class Node:

    def __init__(self, val):
        self.val = val
        self.next = None


    def __str__(self):
        return self.val


    def set_next(self, next):
        self.next = next



# Add node
# Remove node
# Get specific node
# Print all nodes


class Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None

    
    def add_node(self, node):
        # print("Adding " + node.val)

        # Node is head
        if self.head == None:
            self.head = node
            self.tail = node
            # print(self.head.val)
        
        # Node is not head
        else:
            self.tail.next = node
            self.tail = node

    def print_nodes(self):
        current = self.head

        while current != None:
            print(current.val)
            current = current.next




list = Linked_List()
n = Node("hello")
list.add_node(n)
list.add_node(Node("world"))
list.add_node(Node("it's cold"))
list.add_node(Node("but sunny"))
list.print_nodes()


# def print_list_recursive(current_node):
#     # Base case
#     if current_node == None:
#         return


#     # Do the recursion
#     # Recurse with updated value
#     next = current_node.next

#     return print_list_recursive(next)
