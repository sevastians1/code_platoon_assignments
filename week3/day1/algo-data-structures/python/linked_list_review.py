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

    

    # Check if self.next has a value or not
    # def is_tail(self):
    #     return self.next == None

        # if self.next != None:
        #     return True
        # else:
        #     return False

        


head = Node("hello")

# print(head.is_tail())

temp_node = Node("world")

head.set_next(temp_node)
# print(head.next)
# print(head.is_tail())

head.next.set_next(Node("its sunny"))
head.next.next.set_next(Node("but its cold"))

# print(head.next.next)

current_node = head

# while current_node.is_tail() == False:

while current_node != None:
    print("Current node: " + current_node.val)

    # When we are at the tail, this throws an error because `next` does not exist
    if current_node.next != None:
        print("Next node: " + current_node.next.val)
        
    else:
        print("This is the tail")
        
    print(" ")

    current_node = current_node.next # For tails, current_node.next == None
