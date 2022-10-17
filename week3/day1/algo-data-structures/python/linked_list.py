class LinkList:
  # write your __init__ method here that should store a 'head' value which the first Node in the LinkedList and a 'length' value which is the total number of Nodes in the LinkedList
  def __init__(self, head=None):
    self.head = head
    self.length = 0


  def add(self, data):
    # write your code to ADD an element to the Linked List

    new_node = Node(data)
    if self.head is None:
      self.head = new_node
      return

    last = self.head

    while last.next:
      last = last.next
    last.next = new_node
    
      

  def remove(self, data):
    # write your code to REMOVE an element from the Linked List
    head_value = self.head

    if head_value is not None:
      if head_value.value == data:
        self.head == head_value.next
        head_value == None
        return
    while head_value is not None:
      if head_value.value == data:
          break
      previous = head_value
      head_value = head_value.next
    if head_value == None:
      return
    
    previous.next = head_value.next
    head_value = None


  def get(self, element_to_get):
    # write you code to GET and return an element from the Linked List
    current = self.head

    while current is not None:
      if current.value == element_to_get:
        return current.value
      current = current.next

  def print_list(self):

    while self.head is not None:
      print(self.head.value)
      self.head = self.head.next

# ----- Node ------
class Node:
  # store your DATA and NEXT values here
  def __init__(self, value):
    self.value = value
    self.next = None

  

linked_list = LinkList()
linked_list.add('1')
linked_list.add('7')
linked_list.add('6')
linked_list.add('2')
linked_list.remove('7')
# print(linked_list.remove())
print(linked_list.get('7'))
# print(linked_list.head.next.value)

# print(linked_list.head.next.next.next.value)
print(linked_list.print_list())