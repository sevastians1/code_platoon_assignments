class Stack:
  # write your __init__ method here that should store a 'total' value which is the total number of elements in the Stack and a 'stack' value which is an array of stored values in the Stack
  def __init__(self):
    self.stack = []
    self.total = None

  def push(self, data):
    # write your code to add data following LIFO and return the Stack
    
    self.stack.append(data)

  def pop(self):
    # write your code to removes the data following LIFO and return the Stack
    self.stack.pop()

  def size(self):
    # write your code that returns the size of the Stack
    self.total = len(self.stack)


new_stack = Stack()

new_stack.push(9)
new_stack.push(2)
new_stack.push(3)
new_stack.push(1)
new_stack.pop()

print(new_stack.stack)
print(new_stack.total)