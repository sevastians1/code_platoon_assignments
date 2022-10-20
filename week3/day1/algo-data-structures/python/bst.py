class Node:

  def __init__(self, val) -> None:
    self.left = None
    self.right = None
    self.value = val


# class BST:
  
#   def __init__(self) -> None:
#     self.root = None

def insert(root=None, val=None):
  
  # insert at root --> root = None
  if root is None:
    root = Node(val)
    return root


  else:
    # cur_node = root
    
    if val < root.value:
      root.left = insert(root.left, val)
    
    elif val > root.value:
      root.right = insert(root.right, val)

    # if exists, then just return
    else:
      return root

  return root

# 3 ways to traverse through the tree
# 1
def inorder(root):
  if root:
    inorder(root.left)
    print(root.value)
    inorder(root.right)

# 2
def preorder(root):
  if root:
    print(root.value)
    preorder(root.left)
    preorder(root.right)

# 3
def postorder(root):
  if root:
    postorder(root.left)
    postorder(root.right)
    print(root.value)

  # else
    # if val < root --> go left
    # if val > root --> go right



root = insert(None, 30)
# print(root.value)

root = insert(root, 39)

root = insert(root, 40)

root = insert(root, 41)

root = insert(root, 20)
# print(root.left.value)

root = insert(root, 21)
# print(root.left.left.value)

root = insert(root, 19)

print('inorder')
inorder(root)

print('preorder')
preorder(root)

print('postorder')
postorder(root)
