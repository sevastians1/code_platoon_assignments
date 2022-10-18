class Bst:
  def __init__(self, parent=None):
    self.parent = Node(parent)

  def insert(self, parent, value):


    if parent is None:
      return Node(value)

    elif parent.data == value:
      return


    elif value > parent.data:
      if parent.right == None:
        parent.right = Node(value)
      else:
        return self.insert(parent.right, value)
    

    elif value < parent.data:
      if parent.left == None:
        parent.left = Node(value)
      else:
        return self.insert(parent.left, value)
      
    return parent


  def contains(self, parent, value):
    if parent.data == value:
      return True

    else:
      if value > parent.data:
        if parent.right == None:
          return False
        else:
          return self.contains(parent.right, value)
      
      else:
        if parent.left == None:
          return False
        else:
          return self.contains(parent.left, value)


  def remove(self, parent, value):
    pass


# ----- Node ------
class Node:
  # store your DATA and LEFT and RIGHT values here
  def __init__(self, data=None):
    self.left = None
    self.right = None
    self.data = data

  def __str__(self) -> str:
    return str(self.data)

new_bst = Bst(12)
new_bst.insert(new_bst.parent, 2)
new_bst.insert(new_bst.parent, 4)
new_bst.insert(new_bst.parent, 5)
new_bst.insert(new_bst.parent, 1)

print(new_bst.parent)
print(new_bst.parent.right)
print(new_bst.parent.left)
print(new_bst.parent.left.right)
print(new_bst.parent.left.right.right)
print(new_bst.parent.left.left)
print(new_bst.parent.left.left.right)

print(new_bst.contains(new_bst.parent, 4))
# print(new_bst.parent.left.left)
# print(new_bst.parent.left.left.right)


# print(new_bst.parent.value)





