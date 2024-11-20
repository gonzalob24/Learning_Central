class Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None


class BST:
  
  def __init__(self):
    self.root = None
    
  def insert(self, value):
    new_node = Node(value)
    # edge case: root is None
    if self.root == None:
      self.root = new_node
      return self.root
    
    current_node = self.root
    
    while True:
      if (current_node.value > value):
        if not current_node.left:
          current_node.left = new_node
          return self.root
        else:
          current_node = current_node.left
      else:
        if not current_node.right:
          current_node.right = new_node
          return self.root
        else:
          current_node = current_node.right
  
  def lookup(self, value):
    current_node = self.root
    
    if current_node == None:
      return None
    
    while current_node:
      if current_node.value == value:
        return current_node
      elif current_node.value < value:
        current_node = current_node.right
      else:
        current_node = current_node.left
    return None
  
  def remove(self):
    pass
  
  def traverse_helper(self, node):
          
    tree = {'value': node.value}

    if node.left == None:
      tree['left'] = None
    else:
      tree['left'] = self.traverse_helper(node.left)
    
    if node.right == None:
      tree['right'] = None
    else: 
      tree['right'] = self.traverse_helper(node.right)
    
    return tree
  
  def traverse(self):
    return self.traverse_helper(self.root)


bst1 = BST()
bst1.insert(9)
bst1.insert(4);
bst1.insert(20);
bst1.insert(1);
bst1.insert(6);
bst1.insert(8);
bst1.insert(10);
bst1.insert(15);
bst1.insert(170);
print(bst1.traverse())
print(bst1.lookup(11))
print(bst1.lookup(1))

def search(nums, target):
  left = 0
  right = len(nums) - 1
  mid = left + ((right - left) // 2) 
  while left <= right:
    if nums[mid] == target:
      return mid
    elif nums[mid] < target:
      left = mid + 1
    else: 
      right = mid - 1
    mid = left + ((right - left) // 2) 
  return -1
    
  

print(search([-1,0,3,5,9,12], 9))
